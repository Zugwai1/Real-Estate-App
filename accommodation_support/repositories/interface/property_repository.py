import uuid
from abc import abstractmethod, ABCMeta
from typing import List
from accommodation_support.dto.property_dto import CreateDto, EditDto, ListDto, GetDto, SearchDto


class PropertyRepository(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateDto) -> uuid.UUID:
        """Create a property Object"""
        raise NotImplementedError

    def search(self, model: SearchDto) -> List[ListDto]:
        """Search property object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, model: EditDto) -> uuid.UUID:
        """Edit a property object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[ListDto]:
        """List property objects"""
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID) -> GetDto:
        """Get property object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: uuid.UUID) -> bool:
        """Delete Property object"""
        raise NotImplementedError
