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

    def create(self, user: CreateDto) -> uuid.UUID:
        try:
            groups = self.__get_or_create_group(user.groups)
            user = User.objects.create(
                id=uuid.uuid4(),
                first_name=user.first_name,
                last_name=user.last_name,
                middle_name=user.middle_name,
                email=user.email,
                phone_number=user.phone_number,
                nationality=user.nationality,
                address_id=user.address_id,
                username=user.username,
                password=make_password(password=user.password),
                DOB=user.DOB
            )
            user.groups.set(groups)
            return user.id
        except (IntegrityError, Exception) as ex:
            logging.error(f"{ex} ,occurred while creating user")
            raise ex

    def list(self) -> List[GetDto]:
        result: List[GetDto] = []
        users = list(User.objects.values(
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "username",
            "DOB",
            "nationality",
            "phone_number",
            "address"
        ))
        for user in users:
            item = GetDto(
                id=user["id"],
                first_name=user["first_name"],
                last_name=user["last_name"],
                middle_name=user["middle_name"],
                DOB=user["DOB"],
                address=user["address"],
                nationality=user["nationality"],
                email=user["email"],
                phone_number=user["phone_number"],
                username=user["username"]
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
            user.username = updated_user.username,
            user.DOB = updated_user.DOB,
            user.first_name = updated_user.first_name,
            user.last_name = updated_user.last_name,
            user.middle_name = updated_user.middle_name,
            user.email = updated_user.email,
            user.nationality = updated_user.nationality,
            user.address = updated_user.address,
            user.phone_number = updated_user.phone_number
            user.save()
            return user.id
        except (ObjectDoesNotExist, MultipleObjectsReturned, Exception) as ex:
            logging.error(f"{ex} Occurred while creating user")
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
