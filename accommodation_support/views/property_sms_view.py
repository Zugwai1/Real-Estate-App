from uuid import UUID

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from NewToUk.shared.models.message_dto import SMSModel
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import PropertySMSSerializer
from auth_app.views.view_decorators import is_authenticated
from accommodation_support.dto.email_dto import PropertyEmailModel
from auth_app.auth.JWT.token import get_payload
from NewToUk.messaging.messaging_service import MessageService
from auth_app.providers import auth_providers


class PropertySMSView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Send SMS To Property Owner",
                         responses={"200": AppBaseSerializer(many=False),
                                    "400": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter], request_body=PropertySMSSerializer)
    @is_authenticated
    def post(self, request):
        model = self.__set_attribute(request)
        result = MessageService().send_sms(model)
        data = AppBaseSerializer(result).data
        if result.status:
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __set_attribute(request):
        user = auth_providers.user_repository().get_by_id(get_payload(request)["id"])
        return SMSModel(
            sender=user.phone_number,
            recipient=request.data.get("recipient", ""),
            message=request.data.get("message", "")
        )
