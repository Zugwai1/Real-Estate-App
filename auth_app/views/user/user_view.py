from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from auth_app.dto.user_dto import CreateUserRequestModel
from auth_app.providers import auth_providers
from auth_app.dto.user_dto import CreateDto
from auth_app.views.view_decorators import is_authenticated, authorize
from auth_app.serializers.use_serializer import ListUserSerializer, UserResponseSerializer, CreateUserSerializer


class UserView(APIView):
    token_parameter = openapi.Parameter(name="Authorization", in_="header", type=openapi.TYPE_STRING, required=True)

    @swagger_auto_schema(operation_id="List Users", responses={"200": ListUserSerializer(many=False)},
                         manual_parameters=[token_parameter])
    @is_authenticated
    @authorize(["Admin"])
    def get(self, request):
        response = auth_providers.user_service().list()
        serializer = ListUserSerializer(response).data
        return Response(data=serializer,
                        status=status.HTTP_200_OK if response.status else status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_id="Create User",
                         responses={"200": UserResponseSerializer(many=False),
                                    "400": AppBaseSerializer(many=False)},
                         request_body=CreateUserSerializer)
    def post(self, request):
        model = self.__set_attribute(request)
        if isinstance(model, BaseResponse):
            return Response(data=AppBaseSerializer(model).data,
                            status=status.HTTP_400_BAD_REQUEST)
        user_dto = CreateDto(
            username=model.username,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name,
            phone_number=model.phone_number,
            nationality=model.nationality,
            middle_name=model.middle_name,
            password=model.password,
            DOB=model.DOB,
            groups=model.groups,
            state=model.state,
            country=model.country,
            city=model.city,
            postal_code=model.postal_code,
            number_line=model.number_line,
            street=model.street
        )
        response = UserResponseSerializer(auth_providers.user_service().create(user_dto)).data
        return Response(data=response,
                        status=status.HTTP_200_OK if response["status"] else status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __set_attribute(request):
        try:
            model = CreateUserRequestModel(
                username=request.data["email"],
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
