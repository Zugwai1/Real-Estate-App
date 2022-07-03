import logging
import uuid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import IntegrityError

from NewToUk.shared.models.base_response import BaseResponse
from auth_app.dto.user_dto import EditDto, GetUserResponseModel, ListUserResponseModel, CreateDto, \
    CreateUserResponseModel, EditUserResponseModel, DeleteUserResponseModel
from auth_app.repositories.inteface.user_repository import UserRepository
from auth_app.services.interface.user_service import UserService


class DefaultUserService(UserService):
    repository: UserRepository

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, user_dto: CreateDto) -> BaseResponse:
        try:
            exists = self.repository.check_if_exist(email=user_dto.email)
            if not exists:
                result = self.repository.create(user_dto)
                logging.info(f"User with Id {result} created")
                return CreateUserResponseModel(
                    user_id=result,
                    status=True,
                    message="User Object Created Successfully"
                )
            else:
                return CreateUserResponseModel(
                    user_id=None,
                    status=False,
                    message="Email Already exist, Please check email and try again"
                )
        except (Exception, IntegrityError):
            return CreateUserResponseModel(
                user_id=None,
                status=False,
                message="An error occurred"
            )

    def list(self) -> BaseResponse:
        users = self.repository.list()
        return ListUserResponseModel(
            users=users,
            status=True,
            message="Successful"
        )

    def get(self, id: uuid.UUID = None, email: str = None) -> BaseResponse:
        try:
            user = None
            if id is not None:
                user = self.repository.get_by_id(id)
            elif email is not None:
                user = self.repository.get_by_email(email)
            if user:
                return GetUserResponseModel(
                    user=user,
                    status=True,
                    message="Successful"
                )
            else:
                return GetUserResponseModel(
                    status=False,
                    message=f"User with id: {id} not found" if id is not None else f"Usr with email: {email} not found",
                    user=None
                )
        except ObjectDoesNotExist:
            return GetUserResponseModel(
                status=False,
                message=f"User with id: {id} not found" if id is not None else f"Usr with email: {email} not found",
                user=None
            )
        except MultipleObjectsReturned:
            return GetUserResponseModel(
                status=False,
                message=f"Multiple User with id: {id} found" if id is not None else f"Usr with email: {email} not found",
                user=None
            )
        except (Exception,) as ex:
            return GetUserResponseModel(
                status=False,
                message=ex,
                user=None
            )

    def edit(self, id: uuid.UUID, updated_user_dto: EditDto):
        try:
            result = self.repository.edit(id, updated_user_dto)
            return EditUserResponseModel(
                user_id=result,
                status=True,
                message="User Object Updated Successfully"
            )
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return CreateUserResponseModel(
                user_id=None,
                status=False,
                message="An error occurred"
            )

    def delete(self, id: uuid.UUID):
        try:
            self.repository.delete(id)
            return DeleteUserResponseModel(
                message="Use Object Successfully Delete",
                status=True
            )
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return DeleteUserResponseModel(
                message="An error occurred",
                status=False
            )
