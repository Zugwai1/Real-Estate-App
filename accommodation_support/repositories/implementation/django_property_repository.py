import logging
import uuid
from typing import List
from accommodation_support.dto.PropertyDto import ListDto, EditDto, CreateDto, GetDto
from accommodation_support.models import Property, Image
from accommodation_support.repositories.interface.property_repository import PropertyRepository
from auth_app.repositories.inteface.UserRepository import UserRepository
from auth_app.models import Address


class DjangoPropertyRepository(PropertyRepository):
    user_repository: UserRepository

    def __init__(self, user_repository):
        self.user_repository = user_repository

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
        except (Exception,) as ex:
            logging.error(f"{ex} ,occurred while updating property")
            raise ex

    def list(self) -> List[ListDto]:
        objects: List[ListDto] = []
        properties = Property.objects.all()
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
                images=property.image_set.all(),
                user=self.user_repository.get_by_id(id=property.user_id)
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
                user=self.user_repository.get_by_id(id=property.user_id),
                description=property.description
            )
            return result
        except (Exception,) as ex:
            logging.error(f"{ex} ,occurred while getting property")
            raise ex

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
        except (Exception,) as ex:
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
        except (Exception,) as ex:
            logging.error(f"{ex} ,occurred while updating images")
            raise ex
