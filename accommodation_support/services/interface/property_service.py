import uuid
from abc import abstractmethod, ABCMeta
from typing import List

from NewToUk.shared.models.BaseResponse import BaseResponse
from accommodation_support.dto.property_dto import CreateDto, EditDto, CreatePropertyResponseModel, \
    GetPropertyResponseModel, EditPropertyResponseModel, ListPropertyResponseModel


class PropertyService(metaclass=ABCMeta):
    @abstractmethod
    def create(self, model: CreateDto) -> CreatePropertyResponseModel | BaseResponse:
        """Create a property Object"""
        raise NotImplementedError

    def search(self, filter: str) -> ListPropertyResponseModel | BaseResponse:
        """Search property object"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, model: EditDto) -> EditPropertyResponseModel:
        """Edit a property object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> ListPropertyResponseModel:
        """List property objects"""
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID) -> GetPropertyResponseModel:
        """Get property object"""
        raise NotImplementedError
