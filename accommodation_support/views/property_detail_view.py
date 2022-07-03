from uuid import UUID

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk import AppBaseSerializer, FileStorage, BaseResponse
from accommodation_support.dto.property_dto import CreatePropertyRequestModel
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import GetPropertySerializer
from auth_app.views.view_decorators import is_authenticated, authorize


class PropertyDetailView(APIView):
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
        ...

    def delete(self, request, id: UUID):
        ...

    def __set_attribute(self, request):
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
                images=list(map(FileStorage().save, self.__get_files(request)))
            )
            return property_request_model
        except KeyError as ex:
            return BaseResponse(
                status=False,
                message=f"fill data for {ex}"
            )