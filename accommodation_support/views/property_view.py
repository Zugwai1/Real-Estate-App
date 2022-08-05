from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import ListPropertySerializer, \
    CreatePropertyResponseSerializer, CreatePropertySerializer
from auth_app.views.view_decorators import is_authenticated, authorize
from accommodation_support.dto.property_dto import CreatePropertyRequestModel, CreateDto
from NewToUk.shared.Utilies.file_storage import FileStorage
from auth_app.auth.JWT.token import get_payload


class PropertyView(APIView):
    parser_classes = (MultiPartParser,)
    file_storage = FileStorage()
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="List Properties",
                         responses={"200": ListPropertySerializer(many=False), "404": AppBaseSerializer(many=False)})
    def get(self, request):
        response = accommodation_app_provider.property_service().list()
        if response.status:
            data = ListPropertySerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_id="Create Property",
                         responses={"200": CreatePropertyResponseSerializer(many=False),
                                    "400": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter], request_body=CreatePropertySerializer)
    @is_authenticated
    @authorize(["PropertyOwner"])
    def post(self, request):
        request_data = self.__set_attributes(request)
        if isinstance(request_data, BaseResponse):
            return Response(data=request_data.__dict__, status=status.HTTP_400_BAD_REQUEST)
        request_data.images = list(map(FileStorage().save, self.file_storage.get_files(request, "image")))
        response = accommodation_app_provider.property_service().create(model=CreateDto(
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
            user_id=get_payload(request)["id"],
            number_of_bathrooms=request_data.number_of_bathrooms,
            number_of_bedrooms=request_data.number_of_bathrooms,
            price=request_data.price,
            status=request_data.status
        ))
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def __set_attributes(request):
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
                images=None
            )
            return property_request_model
        except KeyError as ex:
            return BaseResponse(
                status=False,
                message=f"fill data for {ex}"
            )
