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
    status: str
    number_of_bedrooms: int
    number_of_bathrooms: int
    price: float
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
    status: str
    number_of_bedrooms: int
    number_of_bathrooms: int
    price: float
    images: List[str]


@dataclass
class ListDto:
    id: UUID
    name: str
    type: str
    status: str
    price: float
    number_of_bedrooms: int
    number_of_bathrooms: int
    user: user_dto.GetDto
    address: address_dto.GetDto
    images: List[str]
    description: str


@dataclass
class GetDto:
    id: UUID
    name: str
    type: str
    description: str
    user: user_dto.GetDto
    status: str
    number_of_bedrooms: int
    number_of_bathrooms: int
    price: float
    images: List[str]
    address: address_dto.GetDto


@dataclass
class SearchDto:
    keyword: str
    price: float
    number_of_bedrooms: int
    number_of_bathrooms: int
    status: str
    location: str
    property_type: str


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
    status: str
    number_of_bedrooms: int
    number_of_bathrooms: int
    price: float
    images: List[str] | None
