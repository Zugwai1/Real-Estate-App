import uuid

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import IntegrityError

from auth_app.dto.address_dto import GetAddressResponseModel, EditDto, EditAddressResponseModel, \
    ListAddressResponseModel, CreateDto, CreateAddressResponseModel
from auth_app.repositories.inteface.address_repository import AddressRepository
from auth_app.services.interface.address_service import AddressService


class DefaultAddressService(AddressService):
    repository: AddressRepository

    def __init__(self, repository: AddressRepository):
        self.repository = repository

    def create(self, address: CreateDto) -> CreateAddressResponseModel:
        try:
            result = self.repository.create(address)
            return CreateAddressResponseModel(
                id=result,
                status=True,
                message="Successful"
            )
        except(Exception, IntegrityError):
            return CreateAddressResponseModel(
                id=None,
                status=False,
                message="An error occurred while creating address"
            )

    def list(self) -> ListAddressResponseModel:
        addresses = self.repository.list()
        return ListAddressResponseModel(
            address=addresses,
            status=True,
            message="Successful"
        )

    def edit(self, id: uuid.UUID, updated_address: EditDto) -> EditAddressResponseModel:
        try:
            result = self.repository.edit(id=id, updated_address=updated_address)
            return EditAddressResponseModel(
                id=result,
                status=True,
                message="Successful"
            )
        except(ObjectDoesNotExist, MultipleObjectsReturned):
            return EditAddressResponseModel(
                id=None,
                status=False,
                message="An error occurred while creating address"
            )

    def get(self, id: uuid.UUID) -> GetAddressResponseModel:
        try:
            result = self.repository.get(id=id)
            return GetAddressResponseModel(
                address=result,
                status=True,
                message="Successful"
            )
        except(ObjectDoesNotExist, MultipleObjectsReturned):
            return GetAddressResponseModel(
                address=None,
                status=False,
                message="An error occurred while creating address"
            )
