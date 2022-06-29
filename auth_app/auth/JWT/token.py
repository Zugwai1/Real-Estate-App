import datetime
import json
import logging
from os import getenv
from cryptography.hazmat.primitives import serialization
from auth_app.dto.user_dto import Login
import jwt


def get_token(payload: Login) -> str:
    try:
        exp = datetime.datetime.now() + datetime.timedelta(seconds=float(getenv("EXPIRY_TIME")))
        nbf = datetime.datetime.now()
        iss = getenv("ISS")
        aud = getenv("AUD")
        iat = datetime.datetime.now()
        algorithm = getenv("ALGORITHM")
        key = getenv("SECRET_KEY")
        data = payload.__dict__
        return jwt.encode(payload={
            "data": data,
            "exp": exp,
            "iss": iss,
            "aud": aud,
            "iat": iat
        }, algorithm=algorithm, key=key)
    except (OSError, Exception) as ex:
        logging.error(f"{ex} occurred while generating token")
        raise ex


def decode(token: str) -> Login:
    try:
        audience = getenv("AUD")
        secret = getenv("SECRET_KEY")
        algorithm = getenv("ALGORITHM")
        data = jwt.decode(token, key=secret, audience=audience, options={
            "require": ["exp", "iss", "aud", "iat"], "verify_signature": True
        }, algorithms=algorithm)
        user_info = data["data"]
        user = Login(
            full_name=user_info["full_name"],
            email=user_info["email"],
            username=user_info["username"],
            roles=user_info["roles"]
        )
        return user
    except OSError as error:
        print(error)
    except jwt.exceptions.DecodeError as ex:
        logging.error(f"{ex} occurred while generating token")
        raise ex


def __get_key(is_private: bool = True):
    if is_private:
        path = getenv("PATH_TO_PRI")
        key = open(path, "r").read()
        passphrase = getenv("PASSPHRASE")
        return serialization.load_ssh_private_key(key.encode(), password=passphrase.encode())
    else:
        path = getenv("PATH_TO_PUB")
        key = open(path, "r").read()
        return serialization.load_ssh_public_key(key.encode())
