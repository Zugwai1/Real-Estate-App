from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from NewToUk.shared.models.BaseResponse import BaseResponse
from auth_app.auth.JWT import token
from auth_app.dto.user_dto import LoginResponseModel
from auth_app.providers import auth_providers
from auth_app.viewmodels.login_request_model import LoginRequestModel


class AuthView(APIView):
    """Auth View class"""

    def post(self, request):
        model = self.__get_attribute_from_request(request)
        response = self.__authenticate(username=model.username, password=model.password)
        return Response(data=response.__dict__,
                        status=status.HTTP_200_OK if response.status else status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __authenticate(username: str, password: str) -> LoginResponseModel | BaseResponse:
        try:
            user = auth_providers.user_repository().authenticate(username=username, password=password)
            if user:
                return LoginResponseModel(
                    token=token.get_token(user),
                    status=True,
                    message="Successful"
                )
            else:
                return BaseResponse(
                    status=False,
                    message="Unsuccessful"
                )
        except (Exception,) as ex:
            return BaseResponse(
                status=False,
                message="Username or password Incorrect"
            )

    @staticmethod
    def __get_attribute_from_request(request) -> LoginRequestModel:
        login_request_model = LoginRequestModel(
            username=request.data.get("username", ""),
            password=request.data.get("password", "")
        )
        return login_request_model
