import dataclasses


@dataclasses.dataclass
class LoginRequestModel:
    username: str
    password: str
