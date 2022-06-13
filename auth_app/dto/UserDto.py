from dataclasses import dataclass
from datetime import date
from typing import List
import uuid

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
class GetUserDto:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    nationality: str
    DOB: date
    middle_name: str
    address: object
    username: str
    id: uuid.UUID


@dataclass
class CreateUserResponseModel(BaseResponse):
    user_id: uuid.UUID | None


@dataclass
class ListUserResponseModel(BaseResponse):
    users: List[GetUserDto]


@dataclass
class GetUserResponseModel(BaseResponse):
    user: GetUserDto | None


@dataclass
class EditUserResponseModel(BaseResponse):
    user_id: uuid.UUID | None
