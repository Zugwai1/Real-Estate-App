import dataclasses


@dataclasses.dataclass
class MailModel:
    message: str
    name: str
    email: str
    sender: str
    receiver: str
    subject: str


@dataclasses.dataclass
class SMSModel:
    message: str
    sender: str
    recipient: str
