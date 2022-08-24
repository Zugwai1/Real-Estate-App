from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.models.base_response import BaseResponse
from accommodation_support.dto.property_dto import SearchDto
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import ListPropertySerializer
from auth_app.views.view_decorators import is_authenticated


class PropertySearchView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Search Property",
                         responses={"200": ListPropertySerializer(many=False),
                                    "400": ListPropertySerializer(many=False)},
                         manual_parameters=[token_parameter])
    def post(self, request):
        model = self.__get_attribute_from_request(request)
        response = accommodation_app_provider.property_service().search(model)
        data = ListPropertySerializer(response).data
        if response.status:
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __get_attribute_from_request(request):
        model = SearchDto(
            number_of_bathrooms=request.data.get("number_of_bathrooms", 0),
            number_of_bedrooms=request.data.get("number_of_bedrooms", 0),
            status=request.data.get("status", ""),
            price=request.data.get("", 0),
            property_type=request.data.get("property_type", ""),
            location=request.data.get("location", ""),
            keyword=request.data.get("keyword", "")
        )
        return model
