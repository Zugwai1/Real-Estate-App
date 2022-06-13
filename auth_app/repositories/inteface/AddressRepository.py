import uuid
from abc import ABCMeta, abstractmethod
from typing import List
from auth_app.dto.AddressDto import GetDto, EditDto, CreateDto, ListDto


class AddressRepository(metaclass=ABCMeta):
    """Address Abstract class for any class that needs to implement address data access"""

    @abstractmethod
    def create(self, address: CreateDto) -> uuid.UUID:
        """Creates an address object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListDto]:
        """List Address objects"""
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID) -> GetDto:
        """Gets an address Object by id"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, updated_address: EditDto) -> uuid.UUID:
        """Edits Address object"""
        raise NotImplementedError
