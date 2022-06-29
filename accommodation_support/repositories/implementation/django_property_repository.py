import logging
import uuid
from typing import List

from django.db.models import Q
from auth_app.dto import user_dto
from accommodation_support.dto.property_dto import ListDto, EditDto, CreateDto, GetDto
from accommodation_support.models import Property, Image
from accommodation_support.repositories.interface.property_repository import PropertyRepository
from auth_app.models import Address


class DjangoPropertyRepository(PropertyRepository):
    def create(self, model: CreateDto) -> uuid.UUID:
        try:
            property = Property()
            property.name = model.name
            property.description = model.description
            property.user_id = model.user_id
            property.address = Address(number_line=model.number_line, city=model.city, street=model.street,
                                       state=model.state, country=model.country, postal_code=model.postal_code)
            property.type = model.type
            property.save()
            self.__create_images(property_id=property.id, images=model.images)
            return property.id
        except (Exception,) as ex:
            logging.error(f"{ex} ,occurred while creating property")
            raise ex

    def edit(self, id: uuid.UUID, model: EditDto) -> uuid.UUID:
        try:
            property = Property.objects.get(id=id)
            property.name = model.name
            property.description = model.description
            property.type = model.type
            property.address.number_line = model.number_line
            property.address.city = model.city
            property.address.street = model.street
            property.address.state = model.state
            property.address.country = model.country
            property.address.postal_code = model.postal_code
            self.__update_images(property.objects.all(), model.images)
            property.objects.update()
            return property.id
        except (Exception, Property.DoesNotExist, Property.MultipleObjectsReturned) as ex:
            logging.error(f"{ex} ,occurred while updating property")
            raise ex

    def list(self) -> List[ListDto]:
        objects: List[ListDto] = []
        properties = Property.objects.select_related("address", "user").get()
        for property in properties:
            item = ListDto(
                id=property.id,
                city=property.address.city,
                street=property.address.street,
                state=property.address.state,
                country=property.address.country,
                number_line=property.address.number_line,
                type=property.type,
                postal_code=property.address.postal_code,
                name=property.name,
                images=property.image_set.only("image").all(),
                user=user_dto.GetDto(
                    id=property.user.id,
                    username=property.user.username,
                    DOB=property.user.DOB,
                    first_name=property.user.first_name,
                    last_name=property.user.last_name,
                    middle_name=property.user.middle_name,
                    email=property.user.email,
                    nationality=property.user.nationality,
                    address=property.user.address,
                    phone_number=property.user.phone_number
                )
            )
            objects.append(item)
        return objects

    def get(self, id: uuid.UUID) -> GetDto:
        try:
            property = Property.objects.get(id=id)
            result = GetDto(
                id=property.id,
                city=property.address.city,
                street=property.address.street,
                state=property.address.state,
                country=property.address.country,
                number_line=property.address.number_line,
                type=property.type,
                postal_code=property.address.postal_code,
                name=property.name,
                images=property.image_set.all(),
                description=property.description,
                user=user_dto.GetDto(
                    id=property.user.id,
                    username=property.user.username,
                    DOB=property.user.DOB,
                    first_name=property.user.first_name,
                    last_name=property.user.last_name,
                    middle_name=property.user.middle_name,
                    email=property.user.email,
                    nationality=property.user.nationality,
                    address=property.user.address,
                    phone_number=property.user.phone_number
                )
            )
            return result
        except (Exception, Property.DoesNotExist, Property.MultipleObjectsReturned) as ex:
            logging.error(f"{ex} ,occurred while getting property")
            raise ex

    def search(self, filter: str) -> List[ListDto]:
        properties = Property.objects.select_related("user", "address").filter(
            Q(name__search=filter) | Q(description__contains=filter) | Q(type__search=filter)
        )
        objects: List[ListDto] = []
        for property in properties:
            item = ListDto(
                id=property.id,
                city=property.address.city,
                street=property.address.street,
                state=property.address.state,
                country=property.address.country,
                number_line=property.address.number_line,
                type=property.type,
                postal_code=property.address.postal_code,
                name=property.name,
                images=property.image_set.only("image").all(),
                user=user_dto.GetDto(
                    id=property.user.id,
                    username=property.user.username,
                    DOB=property.user.DOB,
                    first_name=property.user.first_name,
                    last_name=property.user.last_name,
                    middle_name=property.user.middle_name,
                    email=property.user.email,
                    nationality=property.user.nationality,
                    address=property.user.address,
                    phone_number=property.user.phone_number
                )
            )
            objects.append(item)
        return objects

    @staticmethod
    def __create_images(property_id: uuid.UUID, images: List[str]):
        try:
            objects: List[Image] = []
            for image in images:
                item = Image()
                item.property_id = property_id
                item.image = image
                objects.append(item)
            Image.objects.bulk_create(objects)
        except(Exception, Image.DoesNotExist, Image.MultipleObjectsReturned) as ex:
            logging.error(f"{ex} ,occurred while creating images")
            raise ex

    @staticmethod
    def __update_images(images, updated_images):
        try:
            position = 0
            while position < len(images):
                images[position].image = updated_images[0]
                position += 1
            Image.objects.bulk_update(images)
        except (Exception, Image.DoesNotExist, Image.MultipleObjectsReturned) as ex:
            logging.error(f"{ex} ,occurred while updating images")
            raise ex