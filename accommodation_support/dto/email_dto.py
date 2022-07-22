import dataclasses

from NewToUk.shared.models.message_dto import MailModel


@dataclasses.dataclass
class PropertyEmailModel(MailModel):
    property: str

