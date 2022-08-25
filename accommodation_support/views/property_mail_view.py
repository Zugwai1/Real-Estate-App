import os
from uuid import UUID

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import PropertyEmailSerializer
from auth_app.views.view_decorators import is_authenticated
from accommodation_support.dto.email_dto import PropertyEmailModel
from auth_app.auth.JWT.token import get_payload
from NewToUk.messaging.messaging_service import MessageService


class PropertyMailView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Send Email To Property Owner",
                         responses={"200": AppBaseSerializer(many=False),
                                    "400": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter], request_body=PropertyEmailSerializer)
    @is_authenticated
    def post(self, request):
        model = self.__set_attribute(request)
        result = MessageService().send_mail(model, "property_mail.html")
        data = AppBaseSerializer(result).data
        if result.status:
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def __set_attribute(self, request):
        user: dict = get_payload(request)
        return PropertyEmailModel(
            message=request.data.get("message", ""),
            property=self.__get_property_details(request.data.get("property_id", "")),
            name=user["full_name"],
            email=user["email"],
            receiver=request.data.get("receiver", ""),
            sender=user["email"],
            subject=request.data.get("subject", "Contact Mail"),
            others=f'{os.getenv("APP_BASE_URL")}property/single/{request.data.get("property_id", "")}'
        )

    @staticmethod
    def __get_property_details(property_id: UUID):
        property = accommodation_app_provider.property_service().get(property_id).property
        return f"Name: {property.name}, Type: {property.type}, Description: {property.description}"
