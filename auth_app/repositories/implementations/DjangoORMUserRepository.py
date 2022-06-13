import logging
import uuid
from typing import List
from django.db import *

from auth_app.dto.UserDto import CreateDto, GetUserDto, EditDto
from auth_app.models import User
from auth_app.repositories.inteface.UserRepository import UserRepository
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class DjangoORMUserRepository(UserRepository):
    def check_if_exist(self, email: str) -> bool:
        return User.objects.filter(email__exact=email).exists()

    def create(self, user: CreateDto) -> uuid.UUID:
        try:
            result = User.objects.create(
                id=uuid.uuid4(),
                first_name=user.first_name,
                last_name=user.last_name,
                middle_name=user.middle_name,
                email=user.email,
                phone_number=user.phone_number,
                nationality=user.nationality,
                address_id=user.address_id,
                username=user.username,
                password=user.password,
                DOB=user.DOB
            )
            return result.id
        except (IntegrityError, Exception) as ex:
            logging.error(f"{ex} ,occurred while creating user")
            raise ex

    def list(self) -> List[GetUserDto]:
        result: List[GetUserDto] = []
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
            item = GetUserDto(
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

    def get_by_id(self, id: uuid.UUID) -> GetUserDto | None:
        try:
            result = User.objects.get(id=id)
            user = GetUserDto()
            user.username = result.username,
            user.DOB = result.DOB,
            user.first_name = result.first_name,
            user.last_name = result.last_name,
            user.middle_name = result.middle_name,
            user.email = result.email,
            user.nationality = result.nationality,
            user.address = result.address,
            user.phone_number = result.phone_number
            return user
        except (ObjectDoesNotExist, MultipleObjectsReturned) as ex:
            logging.error(f"{ex} Occurred while creating user")
            raise ex

    def get_by_email(self, email: str) -> GetUserDto | None:
        try:
            result = User.objects.get(email=email)
            user = GetUserDto(
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
