from typing import Callable
from dependency_injector import containers, providers
from auth_app.repositories.implementations.DjangoORMAddressRepository import DjangoORMAddressRepository
from auth_app.repositories.implementations.DjangoORMUserRepository import DjangoORMUserRepository
from auth_app.repositories.inteface.AddressRepository import AddressRepository
from auth_app.repositories.inteface.UserRepository import UserRepository
from auth_app.services.implementations.DefaultAddressService import DefaultAddressService
from auth_app.services.implementations.DefaultUserService import DefaultUserService
from auth_app.services.interface.AddressService import AddressService
from auth_app.services.interface.UserService import UserService


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
