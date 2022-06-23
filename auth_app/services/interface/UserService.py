from abc import ABCMeta, abstractmethod
from auth_app.dto.UserDto import *


class UserService(metaclass=ABCMeta):
    """User Management Service to manage the activities of users"""

    @abstractmethod
    def create(self, user_dto: CreateDto) -> CreateUserResponseModel:
        """Create user object"""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> ListUserResponseModel:
        """List User objects"""
        raise NotImplementedError

    @abstractmethod
    def get(self, id: uuid.UUID = None, email: str = None) -> GetUserResponseModel:
        """Gets User Object either with id or email which are both unique"""
        raise NotImplementedError

    @abstractmethod
    def edit(self, id: uuid.UUID, updated_user_dto: EditDto):
        """Edit user object"""
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: uuid.UUID):
        """Delete user object"""
        raise NotImplementedError
