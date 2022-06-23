from NewToUk.shared.models.BaseResponse import BaseResponse
from auth_app.auth.JWT import token
from auth_app.dto.UserDto import LoginResponseModel
from auth_app.providers import auth_providers


def authenticate(username: str, password: str) -> LoginResponseModel | BaseResponse:
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
