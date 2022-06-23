import logging
import uuid
from typing import List
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import *
from auth_app.dto import AddressDto
from auth_app.dto.UserDto import CreateDto, GetDto, EditDto, Login
from auth_app.models import User
from auth_app.repositories.inteface.UserRepository import UserRepository


class DjangoORMUserRepository(UserRepository):
    def authenticate(self, username: str, password: str) -> Login | None:
        try:
            user = User.objects.get(username=username)
            if not user or not check_password(password=password, encoded=user.password):
                return None
            return Login(
                full_name=f"{user.last_name} {user.first_name} {user.middle_name}",
                email=user.email,
                roles=[group.name for group in user.groups.all()],
                username=user.username
            )
        except (ObjectDoesNotExist, MultipleObjectsReturned, Exception) as ex:
            logging.error(f"{ex} ,occurred while getting user")
            raise ex

    def check_if_exist(self, email: str) -> bool:
        return User.objects.filter(email__exact=email).exists()

    def create(self, user_dto: CreateDto) -> uuid.UUID:
        try:
            groups = self.__get_or_create_group(user_dto.groups)
            user = User()

            # User Information
            user.id = uuid.uuid4(),
            user.first_name = user_dto.first_name,
            user.last_name = user_dto.last_name,
            user.middle_name = user_dto.middle_name,
            user.email = user_dto.email,
            user.phone_number = user_dto.phone_number,
            user.nationality = user_dto.nationality,
            user.username = user_dto.username,
            user.password = make_password(password=user_dto.password),
            user.DOB = user_dto.DOB

            # add user Address
            user.address.id = uuid.uuid4(),
            user.address.country = user_dto.country,
            user.address.state = user_dto.state,
            user.address.city = user_dto.city,
            user.address.postal_code = user_dto.postal_code,
            user.address.number_line = user_dto.number_line,
            user.address.street = user_dto.street

            # add user Group
            user.groups = groups
            user.save()
            return user.id[0]
        except (IntegrityError, Exception) as ex:
            logging.error(f"{ex} ,occurred while creating user")
            raise ex

    def list(self) -> List[GetDto]:
        result: List[GetDto] = []
        users = User.objects.all()
        for user in users:
            item = GetDto(
                id=user.id,
                username=user.username,
                DOB=user.DOB,
                first_name=user.first_name,
                last_name=user.last_name,
                middle_name=user.middle_name,
                email=user.email,
                nationality=user.nationality,
                address=user.address,
                phone_number=user.phone_number
            )
            result.append(item)
        return result

    def get_by_id(self, id: uuid.UUID) -> GetDto | None:
        try:
            result = User.objects.filter(id=id).get()
            address = AddressDto.GetDto(
                id=result.address.id,
                number_line=result.address.number_line,
                street=result.address.street,
                city=result.address.city,
                country=result.address.country,
                postal_code=result.address.postal_code,
                state=result.address.state
            )
            user = GetDto(
                id=result.id,
                username=result.username,
                DOB=result.DOB,
                first_name=result.first_name,
                last_name=result.last_name,
                middle_name=result.middle_name,
                email=result.email,
                nationality=result.nationality,
                address=address,
                phone_number=result.phone_number
            )
            return user
        except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            logging.error(f"{ex} Occurred while creating user")
            raise ex

    def get_by_email(self, email: str) -> GetDto | None:
        try:
            result = User.objects.get(email=email)
            user = GetDto(
                id=result.id,
                username=result.username,
                DOB=result.DOB,
                first_name=result.first_name,
                last_name=result.last_name,
                middle_name=result.middle_name,
                email=result.email,
                nationality=result.nationality,
                address=result.address,
                phone_number=result.phone_number
            )
            return user
        except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            logging.error(f"{ex} Occurred while creating user")
            raise ex

    def edit(self, id: uuid.UUID, updated_user: EditDto) -> uuid.UUID:
        try:
            user = User.objects.get(id=id)
            user.DOB = updated_user.DOB,
            user.first_name = updated_user.first_name,
            user.last_name = updated_user.last_name,
            user.middle_name = updated_user.middle_name,
            user.email = updated_user.email,
            user.nationality = updated_user.nationality,
            user.address.street = updated_user.street,
            user.address.city = updated_user.city,
            user.address.number_line = updated_user.number_line,
            user.address.state = updated_user.state,
            user.phone_number = updated_user.phone_number
            user.save()
            return user.id
        except (ObjectDoesNotExist, MultipleObjectsReturned, Exception) as ex:
            logging.error(f"{ex} Occurred while edit user")
            raise ex

    def delete(self, id: uuid.UUID):
        try:
            User.objects.get(id=id).delete()
        except (ObjectDoesNotExist, MultipleObjectsReturned, Exception) as ex:
            logging.error(f"{ex} Occurred while deleting user")
            raise ex

    @staticmethod
    def __get_or_create_group(groups: List[str]) -> List[str] | None:
        if not groups:
            return None
        try:
            result = []
            for group in groups:
                obj, created = Group.objects.get_or_create(name=group)
                result.append(obj)
            return result
        except (ObjectDoesNotExist, MultipleObjectsReturned, Exception) as ex:
            logging.error(f"{ex} Occurred while creating user")
            raise ex
