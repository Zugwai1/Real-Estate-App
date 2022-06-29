from typing import Callable

from dependency_injector import containers, providers

from accommodation_support.repositories.implementation.django_property_repository import DjangoPropertyRepository
from accommodation_support.repositories.interface.property_repository import PropertyRepository
from accommodation_support.services.implementation.default_property_service import DefaultPropertyService
from accommodation_support.services.interface.property_service import PropertyService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    property_repository: Callable[[], PropertyRepository] = providers.Factory(
        DjangoPropertyRepository
    )

    property_service: Callable[[], PropertyService] = providers.Factory(
        DefaultPropertyService,
        repository=property_repository
    )


accommodation_app_provider = Container()
