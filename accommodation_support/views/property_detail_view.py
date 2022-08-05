from uuid import UUID

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.Utilies.file_storage import FileStorage
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from accommodation_support.dto.property_dto import CreatePropertyRequestModel, EditDto
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import GetPropertySerializer, EditPropertyResponseSerializer, \
    EditPropertySerializer
from auth_app.views.view_decorators import is_authenticated, authorize


class PropertyDetailView(APIView):
    parser_classes = (MultiPartParser,)
    file_storage = FileStorage()
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Get Property",
                         responses={"200": GetPropertySerializer(many=False), "404": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    def get(self, request, pk: UUID):
        response = accommodation_app_provider.property_service().get(pk)
        if response.status:
            data = GetPropertySerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Edit Property",
                         responses={"200": EditPropertyResponseSerializer(many=False),
                                    "404": AppBaseSerializer(many=False),
                                    "400": EditPropertyResponseSerializer(many=False)},
                         manual_parameters=[token_parameter], request_body=EditPropertySerializer)
    @is_authenticated
    @authorize(["PropertyOwner"])
    def put(self, request, pk: UUID):
        request_data = self.__set_attribute(request)
        if isinstance(request_data, BaseResponse):
            data = AppBaseSerializer(request_data).data
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        request_data.images = list(map(FileStorage().save, self.file_storage.get_files(request, "image")))
        response = accommodation_app_provider.property_service().edit(id=pk, model=EditDto(
            description=request_data.description,
            postal_code=request_data.postal_code,
            state=request_data.state,
            city=request_data.city,
            street=request_data.street,
            country=request_data.country,
            number_line=request_data.number_line,
            name=request_data.name,
            type=request_data.type,
            images=request_data.images,
            number_of_bathrooms=request_data.number_of_bathrooms,
            number_of_bedrooms=request_data.number_of_bedrooms,
            status=request_data.status,
            price=request_data.price,
        ))
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_id="Delete Property",
                         responses={"200": AppBaseSerializer(many=False),
                                    "404": AppBaseSerializer(many=False),
                                    "400": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    @authorize(["PropertyOwner"])
    def delete(self, request, pk: UUID):
        response = accommodation_app_provider.property_service().delete(pk)
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __set_attribute(request):
        try:
            property_request_model = CreatePropertyRequestModel(
                description=request.data["description"],
                postal_code=request.data["postal_code"],
                state=request.data["state"],
                city=request.data["city"],
                street=request.data["street"],
                country=request.data["country"],
                number_line=request.data["number_line"],
                name=request.data["name"],
                type=request.data["type"],
                number_of_bathrooms=request.data["number_of_bathrooms"],
                number_of_bedrooms=request.data["number_of_bedrooms"],
                status=request.data["status"],
                price=request.data["price"],
                images=None
            )
            return property_request_model
        except KeyError as ex:
            return BaseResponse(
                status=False,
                message=f"fill data for {ex}"
            )
