from uuid import UUID
from dataclasses_serialization.json import JSONSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_app.dto import AddressDto
from NewToUk.shared.models.BaseResponse import BaseResponse
from auth_app.dto.UserDto import CreateUserRequestModel
from auth_app.providers import auth_providers
from auth_app.dto import UserDto

from auth_app.services.implementations.AuthService import is_authenticated, authorize


class UserView(APIView):
    JSON_SERIALIZER = JSONSerializer

    @is_authenticated
    @authorize(["Admin"])
    def get(self, request, pk: UUID):
        response = auth_providers.user_service().get(id=pk)
        data = response.dict()
        return Response(data=data, status=status.HTTP_200_OK if response.status else status.HTTP_404_NOT_FOUND)

    def post(self, request):
        model = self.__set_attribute(request)
        if isinstance(model, BaseResponse):
            return Response(data=model.__dict__,
                            status=status.HTTP_400_BAD_REQUEST)
        address_response = auth_providers.address_service().create(AddressDto.CreateDto(
            street=model.street,
            state=model.state,
            country=model.country,
            city=model.city,
            postal_code=model.postal_code,
            number_line=model.number_line
        ))
        if not address_response.status:
            return address_response
        if address_response.status:
            user_dto = UserDto.CreateDto(
                username=model.username,
                email=model.email,
                first_name=model.first_name,
                last_name=model.last_name,
                phone_number=model.phone_number,
                nationality=model.nationality,
                middle_name=model.middle_name,
                password=model.password,
                DOB=model.DOB,
                address_id=address_response.id,
                groups=model.groups,
            )
            user_response = auth_providers.user_service().create(user_dto)
            data = user_response.__dict__
            return Response(data=data,
                            status=status.HTTP_200_OK if user_response.status else status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __set_attribute(request):
        try:
            model = CreateUserRequestModel(
                username=request.data["username"],
                email=request.data["email"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                phone_number=request.data["phone_number"],
                nationality=request.data["nationality"],
                middle_name=request.data["middle_name"],
                password=request.data["password"],
                DOB=request.data["dob"],
                country=request.data["country"],
                city=request.data["city"],
                postal_code=request.data["postal_code"],
                number_line=request.data["number_line"],
                street=request.data["street"],
                state=request.data["state"],
                groups=str(request.data["groups"]).split(","),
            )
            return model
        except (Exception,) as ex:
            return BaseResponse(
                status=False,
                message=f"Fill data for {ex}"
            )
