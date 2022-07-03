import uuid
from dataclasses import dataclass
from typing import List
from NewToUk.shared.models.base_response import BaseResponse


@dataclass
class CreateDto:
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int


@dataclass
class ListDto:
    id: uuid.UUID
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int


@dataclass
class EditDto:
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int


@dataclass
class GetDto:
    id: uuid.UUID
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int


@dataclass
class CreateAddressResponseModel(BaseResponse):
    id: uuid.UUID | None


@dataclass
class EditAddressResponseModel(BaseResponse):
    id: uuid.UUID | None


@dataclass
class ListAddressResponseModel(BaseResponse):
    address: List[ListDto]


@dataclass
class GetAddressResponseModel(BaseResponse):
    address: GetDto | None
