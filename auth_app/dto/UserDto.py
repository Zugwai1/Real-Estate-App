from dataclasses import dataclass
from datetime import date
from typing import List
import uuid
from auth_app.dto import AddressDto
from NewToUk.shared.models.BaseResponse import BaseResponse


@dataclass
class CreateDto:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    nationality: str
    DOB: date
    middle_name: str
    address_id: uuid.UUID
    username: str
    groups: List[str]


@dataclass
class EditDto:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    nationality: str
    DOB: date
    middle_name: str
    address: object
    username: str


@dataclass
class GetDto:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    nationality: str
    DOB: date
    middle_name: str
    address: AddressDto.GetDto
    username: str
    id: uuid.UUID


@dataclass
class Login:
    full_name: str
    email: str
    username: str
    roles: List[str]


# Response Model
@dataclass
class CreateUserResponseModel(BaseResponse):
    user_id: uuid.UUID | None


@dataclass
class ListUserResponseModel(BaseResponse):
    users: List[GetDto]


@dataclass
class GetUserResponseModel(BaseResponse):
    user: GetDto | None | dict

    def dict(self):
        self.user.address = self.user.address.__dict__
        self.user = self.user.__dict__
        return self.__dict__


@dataclass
class EditUserResponseModel(BaseResponse):
    user_id: uuid.UUID | None


@dataclass
class LoginResponseModel(BaseResponse):
    token: str


# Request Models
@dataclass
class LoginRequestModel:
    username: str
    password: str


@dataclass
class CreateUserRequestModel:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    nationality: str
    DOB: date
    middle_name: str
    username: str
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    groups: List[str]
