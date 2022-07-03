import functools
import logging
from jwt import *
from rest_framework import status
from rest_framework.response import Response
from NewToUk.shared.models.base_response import BaseResponse
from auth_app.auth.JWT.token import decode, get_token


def is_authenticated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token: str = get_token(args[1])
        if token is None or token == "":
            return Response(BaseResponse(
                status=False,
                message="No token provided"
            ).__dict__, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                decode(token)
                return func(*args, **kwargs)
            except (Exception, ImmatureSignatureError, InvalidTokenError, InvalidSignatureError, InvalidAudienceError,
                    InvalidIssuerError, InvalidAlgorithmError, ExpiredSignatureError, InvalidIssuedAtError,
                    MissingRequiredClaimError) as message:
                logging.error(f"{message}, occurred while validating token")
                return Response(BaseResponse(
                    status=False,
                    message=str(message),
                ).__dict__, status=status.HTTP_401_UNAUTHORIZED)

    return wrapper


def authorize(roles: list):
    def wrapper_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token: str = get_token(args[1])
            if token is None or token == "":
                return Response(BaseResponse(
                    status=False,
                    message="No token provided"
                ).__dict__, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    user = decode(token)
                    user_roles = user.roles
                    for role in roles:
                        return func(*args, **kwargs) if role in user_roles else Response(BaseResponse(
                            status=False,
                            message="Not Authorized to access this resource",
                        ).__dict__, status=status.HTTP_403_FORBIDDEN)
                except (
                        Exception, ImmatureSignatureError, InvalidTokenError, InvalidSignatureError,
                        InvalidAudienceError,
                        InvalidIssuerError, InvalidAlgorithmError, ExpiredSignatureError, InvalidIssuedAtError,
                        MissingRequiredClaimError) as message:
                    logging.error(f"{message}, occurred while validating token")
                    return Response(BaseResponse(
                        status=False,
                        message=str(message),
                    ).__dict__, status=status.HTTP_401_UNAUTHORIZED)

        return wrapper

    return wrapper_func



