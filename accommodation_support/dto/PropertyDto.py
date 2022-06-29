from dataclasses import dataclass
from typing import List
from uuid import UUID

from auth_app.dto import user_dto


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
    user: UserDto.GetDto
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str]


@dataclass
class GetDto:
    id: UUID
    name: str
    type: str
    description: str
    user: UserDto.GetDto
    number_line: int
    street: str
    city: str
    state: str
    country: str
    postal_code: int
    images: List[str]
