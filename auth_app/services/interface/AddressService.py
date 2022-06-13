from abc import ABCMeta, abstractmethod
from auth_app.dto.AddressDto import *


class AddressService(metaclass=ABCMeta):
    """Address Service"""

    @abstractmethod
    def create(self, address: CreateDto) -> CreateAddressResponseModel:
        """Create Address Object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> ListAddressResponseModel:
        """List Address Objects"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, updated_address: EditDto) -> EditAddressResponseModel:
        """Edit address object"""
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID) -> GetAddressResponseModel:
        """Get address object"""
        raise NotImplementedError
