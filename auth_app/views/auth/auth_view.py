from coreapi.compat import force_text
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from NewToUk.shared.models.base_response import BaseResponse
from NewToUk.shared.models.base_serializer import AppBaseSerializer
from auth_app.auth.JWT import token
from auth_app.auth.token_generator import account_activation_token
from auth_app.dto.user_dto import LoginResponseModel
from auth_app.providers import auth_providers
from auth_app.serializers.use_serializer import LoginResponseSerializer, LoginRequestSerializer, ResponseSerializer
from auth_app.viewmodels.login_request_model import LoginRequestModel


class AuthView(APIView):
    """Auth View class"""

    @swagger_auto_schema(operation_id="Get Token",
                         responses={"200": LoginResponseSerializer(many=False), "404": AppBaseSerializer(many=False)},
                         request_body=LoginRequestSerializer)
    def post(self, request):
        model = self.__get_attribute_from_request(request)
        response = self.__authenticate(username=model.username, password=model.password)
        data = LoginResponseSerializer(response).data
        if response.user is None:
            return Response(data=data,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data,
                        status=status.HTTP_200_OK if response.status else status.HTTP_401_UNAUTHORIZED)



    @staticmethod
    def __authenticate(username: str, password: str) -> LoginResponseModel | BaseResponse:
        try:
            result = auth_providers.user_repository().authenticate(username=username, password=password)
            if result[0]:
                return LoginResponseModel(
                    token=token.generate_token(result[1]),
                    status=True,
                    message="Successful",
                    user=result[1]
                )
            elif not result[0]:
                return LoginResponseModel(
                    token="",
                    status=False,
                    message="Account not yet verified",
                    user=result[1]
                )
            else:
                return LoginResponseModel(
                    token="",
                    status=False,
                    message="Username or password Incorrect",
                    user=result[1]
                )
        except (Exception,) as ex:
            return LoginResponseModel(
                token="",
                status=False,
                message="Username or password Incorrect",
                user=None
            )

    @staticmethod
    def __get_attribute_from_request(request) -> LoginRequestModel:
        login_request_model = LoginRequestModel(
            username=request.data.get("username", ""),
            password=request.data.get("password", "")
        )
        return login_request_model
