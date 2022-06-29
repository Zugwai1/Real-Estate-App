from typing import Callable
from dependency_injector import containers, providers
from auth_app.repositories.implementation.django_orm_address_repository import DjangoORMAddressRepository
from auth_app.repositories.implementation.django_orm_user_repository import DjangoORMUserRepository
from auth_app.repositories.inteface.address_repository import AddressRepository
from auth_app.repositories.inteface.user_repository import UserRepository
from auth_app.services.implementation.default_address_service import DefaultAddressService
from auth_app.services.implementation.default_user_service import DefaultUserService
from auth_app.services.interface.address_service import AddressService
from auth_app.services.interface.user_service import UserService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository: Callable[[], UserRepository] = providers.Factory(
        DjangoORMUserRepository
    )

    user_service: Callable[[], UserService] = providers.Factory(
        DefaultUserService,
        repository=user_repository
    )

    address_repository: Callable[[], AddressRepository] = providers.Factory(
        DjangoORMAddressRepository
    )

    address_service: Callable[[], AddressService] = providers.Factory(
        DefaultAddressService,
        repository=address_repository
    )


auth_providers = Container()
