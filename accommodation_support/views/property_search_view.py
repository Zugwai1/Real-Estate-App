from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.models.base_response import BaseResponse
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import ListPropertySerializer
from auth_app.views.view_decorators import is_authenticated


class PropertySearchView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Search Property",
                         responses={"200": ListPropertySerializer(many=False),
                                    "400": ListPropertySerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    def get(self, request, filter: str):
        response = accommodation_app_provider.property_service().search(filter)
        data = ListPropertySerializer(response).data
        if response.status:
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
