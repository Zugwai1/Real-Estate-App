import datetime
import json
import logging
from os import getenv
from cryptography.hazmat.primitives import serialization
from auth_app.dto.UserDto import Login
import jwt


def get_token(payload: Login) -> str:
    try:
        exp = datetime.datetime.now() + datetime.timedelta(seconds=float(getenv("EXPIRY_TIME")))
        nbf = exp + datetime.timedelta(seconds=float(getenv("NBF")))
        iss = getenv("ISS")
        aud = getenv("AUD")
        iat = datetime.datetime.now()
        algorithm = getenv("ALGORITHM")
        key = __get_key()
        data = json.dumps(payload.__dict__)
        return jwt.encode(payload={
            "data": data,
            "exp": exp,
            "iss": iss,
            "aud": aud,
            "iat": iat,
            "nbf": nbf
        }, algorithm=algorithm, key=key)
    except (OSError, Exception) as ex:
        logging.error(f"{ex} occurred while generating token")
        raise ex


def decode(token: str) -> Login:
    try:
        audience = getenv("AUD")
        secret = __get_key(False)
        algorithm = getenv("ALGORITHM")
        leeway = getenv("LEEWAY")
        data = jwt.decode(token, key=secret, audience=audience, options={
            "require": ["exp", "iss", "aud", "iat"], "verify_signature": True,
            "verify_aud": "verify_signature", "verify_exp": "verify_signature",
            "verify_iss": "verify_signature", "verify_nbf": "verify_signature",
            "verify_iat": "verify_signature",
        }, algorithms=algorithm,
                          leeway=datetime.timedelta(seconds=float(leeway)))
        data = json.loads(data["data"])
        user = Login(
            full_name=f"{data['last_name']} {data['first_name']} {data['middle_name']}",
            email=data["email"],
            username=data["username"],
            roles=data["roles"]
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
