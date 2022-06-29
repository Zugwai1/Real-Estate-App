import logging
import uuid
from typing import List
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import IntegrityError
from auth_app.models import Address
from auth_app.repositories.inteface.address_repository import AddressRepository
from auth_app.dto.address_dto import GetDto, EditDto, CreateDto, ListDto


class DjangoORMAddressRepository(AddressRepository):
    def create(self, address: CreateDto) -> uuid.UUID:
        try:
            result = Address.objects.create(
                id=uuid.uuid4(),
                country=address.country,
                state=address.state,
                city=address.city,
                postal_code=address.postal_code,
                number_line=address.number_line,
                street=address.street
            )
            return result.id
        except (IntegrityError, Exception) as ex:
            logging.error(f"{ex} occurred while saving address")
            raise ex

    def list(self) -> List[ListDto]:
        result: List[ListDto] = []
        query_set = list(Address.objects.values(
            "id",
            "number_line",
            "city",
            "state",
            "postal_code",
            "country",
            "street"
        ))
        for address in query_set:
            item = ListDto()
            item.id = address["id"]
            item.number_line = address["number_line"]
            item.city = address["city"]
            item.state = address["state"]
            item.country = address["country"]
            item.postal_code = address["postal_code"]
            result.append(item)
        return result

    def get(self, id: uuid.UUID) -> GetDto:
        try:
            address = Address.objects.filter(id=id).values(
                "id",
                "number_line",
                "city",
                "state",
                "postal_code",
                "country",
                "street").get()
            return GetDto(
                id=address["id"],
                number_line=address["number_line"],
                city=address["city"],
                state=address["state"],
                country=address["country"],
                postal_code=address["postal_code"],
                street=address["street"]
            )
        except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            logging.error(f"{ex} occurred while getting address")

    def edit(self, id: uuid.UUID, updated_address: EditDto) -> uuid.UUID:
        try:
            address = Address.objects.get(id=id)
            address.street = updated_address.street
            address.city = updated_address.city
            address.country = updated_address.country
            address.postal_code = updated_address.postal_code
            address.state = updated_address.state
            address.number_line = updated_address.number_line
            address.save()
            return address.id
        except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            logging.error(f"{ex} occurred while getting address")
