from dataclasses import dataclass
from typing import List
from uuid import UUID

from NewToUk.shared.models.base_response import BaseResponse
from auth_app.dto import user_dto, address_dto


@dataclass
class CreateDto:
    name: str
    type: str
    description: str
    user_id: UUID
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str]


@dataclass
class EditDto:
    name: str
    type: str
    description: str
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str]


@dataclass
class ListDto:
    id: UUID
    name: str
    type: str
    user: user_dto.GetDto
    address: address_dto.GetDto
    images: List[str]


@dataclass
class GetDto:
    id: UUID
    name: str
    type: str
    description: str
    user: user_dto.GetDto
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str]


# response models

@dataclass
class CreatePropertyResponseModel(BaseResponse):
    property_id: UUID | None


@dataclass
class ListPropertyResponseModel(BaseResponse):
    properties: List[ListDto]


@dataclass
class GetPropertyResponseModel(BaseResponse):
    property: GetDto | None


@dataclass
class EditPropertyResponseModel(BaseResponse):
    property_id: UUID | None


# request model
@dataclass
class CreatePropertyRequestModel:
    name: str
    type: str
    description: str
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str] | None
