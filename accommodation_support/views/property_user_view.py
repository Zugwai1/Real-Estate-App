from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.models.base_serializer import AppBaseSerializer
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import ListPropertySerializer
from auth_app.auth.JWT.token import get_payload


class PropertyUserView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="List Properties",
                         responses={"200": ListPropertySerializer(many=False), "404": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter])
    def get(self, request):
        response = accommodation_app_provider.property_service().get_by_user_id(get_payload(request)["id"])
        if response.status:
            data = ListPropertySerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
