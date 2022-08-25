from __future__ import print_function

import os
import sib_api_v3_sdk
from certifi import contents
from sib_api_v3_sdk import SendSmtpEmailSender, SendSmtpEmailTo
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.template.loader import render_to_string
from NewToUk.shared.models.base_response import BaseResponse

from NewToUk.shared.models.message_dto import MailModel, SMSModel


class MessageService:
    configuration = sib_api_v3_sdk.Configuration()

    def __init__(self):
        self.configuration.api_key['api-key'] = os.getenv("API_KEY")

    def send_mail(self, model: MailModel, html_file: str):
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(self.configuration))
        html_content = render_to_string(html_file, context={"model": model})
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            sender=SendSmtpEmailSender(name=model.name, email=model.sender),
            to=[SendSmtpEmailTo(name="Man", email=model.receiver)],
            subject=model.subject,
            html_content=html_content
        )

        try:
            api_instance.send_transac_email(send_smtp_email)
            return BaseResponse(
                message="Email Sent Successfully",
                status=True
            )
        except ApiException as e:
            message = "Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e
            return BaseResponse(
                message=message,
                status=False
            )

    def send_sms(self, model: SMSModel):
        api_instance = sib_api_v3_sdk.TransactionalSMSApi(sib_api_v3_sdk.ApiClient(self.configuration))
        send_sms = sib_api_v3_sdk.SendTransacSms(
            sender=model.sender, content=model.message, recipient=model.recipient
        )

        try:
            api_instance.send_transac_sms(send_sms)
            return BaseResponse(
                message="SMS Sent Successfully",
                status=True
            )
        except ApiException as e:
            message = "Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e
            return BaseResponse(
                message=message,
                status=False
            )
