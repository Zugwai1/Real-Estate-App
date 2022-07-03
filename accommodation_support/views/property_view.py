from typing import List

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from NewToUk.shared import BaseResponse
from NewToUk.shared import AppBaseSerializer
from accommodation_support.providers import accommodation_app_provider
from accommodation_support.serializers.property_serializer import ListPropertySerializer
from auth_app.views.view_decorators import is_authenticated, authorize
from accommodation_support.dto.property_dto import CreatePropertyRequestModel, CreateDto, CreatePropertyResponseModel
from NewToUk.shared.Utilies import FileStorage
from auth_app.auth.JWT.token import decode


class PropertyView(APIView):
    def get(self, request):
        response = accommodation_app_provider.property_service().list()
        if isinstance(response, BaseResponse):
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if response.status:
            data = ListPropertySerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data = AppBaseSerializer(response).data
            return Response(data=data, status=status.HTTP_200_OK)

    @is_authenticated
    @authorize(["PropertyOwner"])
    def post(self, request):
        request_data, = self.__set_attributes(request),
        if isinstance(request_data, BaseResponse):
            data = AppBaseSerializer(request_data).data
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
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
            user_id=decode(request).id
        ))
        if response.status:
            return Response(data=response.__dict__, status=status.HTTP_200_OK)
        return Response(data=response.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def __set_attributes(self, request):
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

    def __get_files(self, request) -> List:
        stop: bool = False
        count: int = 1
        files: List = []
        while not stop:
            try:
                file = request.data[f"image{count}"]
                files.append(file)
            except KeyError:
                stop = True
        return files
