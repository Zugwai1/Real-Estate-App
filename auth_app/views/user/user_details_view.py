import datetime
from uuid import UUID

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from auth_app.dto.user_dto import EditUserRequestModel, EditDto
from auth_app.providers import auth_providers
from auth_app.views.view_decorators import is_authenticated
from auth_app.serializers.use_serializer import GetUserSerializer, UserResponseSerializer, EditUserSerializer


class UserDetailsView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="Get User",
                         responses={"200": GetUserSerializer(many=False), "404": GetUserSerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    def get(self, request, pk: UUID):
        response = auth_providers.user_service().get(id=pk)
        serializer = GetUserSerializer(response)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK if response.status else status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Edit User",
                         responses={"400": AppBaseSerializer(many=False), "200": UserResponseSerializer(many=False),
                                    "404": UserResponseSerializer(many=False)},
                         manual_parameters=[token_parameter], request_body=EditUserSerializer)
    @is_authenticated
    def put(self, request, pk: UUID):
        model = self.__set_attribute(request)
        if isinstance(model, BaseResponse):
            return Response(data=model.__dict__, status=status.HTTP_400_BAD_REQUEST)
        response = auth_providers.user_service().edit(
            id=pk,
            updated_user_dto=EditDto(
                email=model.email,
                first_name=model.first_name,
                last_name=model.last_name,
                phone_number=model.phone_number,
                nationality=model.nationality,
                middle_name=model.middle_name,
                DOB=model.DOB,
                state=model.state,
                country=model.country,
                city=model.city,
                postal_code=model.postal_code,
                number_line=model.number_line,
                street=model.street
            )
        )
        data = UserResponseSerializer(response).data
        return Response(data,
                        status=status.HTTP_200_OK if response.status else status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Delete User",
                         responses={"400": AppBaseSerializer(many=False), "200": AppBaseSerializer(many=False),
                                    "404": AppBaseSerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    def delete(self, request, pk: UUID):
        response = auth_providers.user_service().delete(id=pk)
        data = AppBaseSerializer(response).data
        return Response(data=data,
                        status=status.HTTP_200_OK if response.status else status.HTTP_404_NOT_FOUND)

    @staticmethod
    def __set_attribute(request):
        try:
            model = EditUserRequestModel(
                email=request.data["email"],
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                phone_number=request.data["phone_number"],
                nationality=request.data["nationality"],
                middle_name=request.data["middle_name"],
                DOB=datetime.datetime.strptime(request.data["dob"], "%Y-%m-%d"),
                country=request.data["country"],
                city=request.data["city"],
                postal_code=request.data["postal_code"],
                number_line=request.data["number_line"],
                street=request.data["street"],
                state=request.data["state"]
            )
            return model
        except (Exception,) as ex:
            return BaseResponse(
                status=False,
                message=f"Fill data for {ex}"
            )
