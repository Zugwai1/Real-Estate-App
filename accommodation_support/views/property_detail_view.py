from uuid import UUID

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared.Utilies.file_storage import FileStorage
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from accommodation_support.dto.property_dto import CreatePropertyRequestModel, EditDto
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import GetPropertySerializer
from auth_app.views.view_decorators import is_authenticated, authorize


class PropertyDetailView(APIView):
    file_storage = FileStorage()

    @is_authenticated
    def get(self, request, id: UUID):
        response = accommodation_app_provider.property_service().get(id)
        if response.status:
            data = GetPropertySerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    @is_authenticated
    @authorize(["PropertyOwner"])
    def put(self, request, id: UUID):
        request_data = self.__set_attribute(request)
        if isinstance(request_data, BaseResponse):
            data = AppBaseSerializer(request_data).data
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        request_data.images = list(map(FileStorage().save, self.file_storage.get_files(request)))
        response = accommodation_app_provider.property_service().edit(id=id, model=EditDto(
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
        ))
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_400_BAD_REQUEST)

    @is_authenticated
    @authorize(["PropertyOwner"])
    def delete(self, request, id: UUID):
        response = accommodation_app_provider.property_service().delete(id)
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
                images=None
            )
            return property_request_model
        except KeyError as ex:
            return BaseResponse(
                status=False,
                message=f"fill data for {ex}"
            )
