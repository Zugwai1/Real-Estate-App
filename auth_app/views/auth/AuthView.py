from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_app.services.implementations.AuthService import authenticate
from auth_app.viewmodels.LoginRequestModel import LoginRequestModel


class AuthView(APIView):
    """Auth View class"""

    def post(self, request):
        model = self.__get_attribute_from_request(request)
        response = authenticate(username=model.username, password=model.password)
        return Response(data=response.__dict__, status=status.HTTP_200_OK if response.status else status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def __get_attribute_from_request(request) -> LoginRequestModel:
        login_request_model = LoginRequestModel(
            username=request.data.get("username", ""),
            password=request.data.get("password", "")
        )
        return login_request_model
