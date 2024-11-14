#!/usr/bin/python3
"""Module to send emails"""

from app.config import settings
from typing import Any, Dict, List
from pydantic import BaseModel, EmailStr
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema


class Mail(BaseModel):
    """Class that defines email instances"""

    email: List[EmailStr]
    content: Dict[str, Any]

    class Config:
        allow_extra = True


conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_FROM="admin@knowafrika.com",
        MAIL_PORT=465,
        MAIL_SERVER="sandbox.smtp.mailtrap.io",
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True
        )


async def simple_send(mail: Mail, template):
    """Function to send an email"""

    message = MessageSchema(
        subject=mail.content.get('subject') or 'Clickinsure API Team',
        recipients=mail.email,
        body=template.format(**mail.content),
        subtype="html")
    fm = FastMail(conf)
    await fm.send_message(message)


async def send_in_background(background_tasks, mail: Mail, template: str):
    """Function to send an email in the background"""

    message = MessageSchema(
        subject=mail.content.get('subject') or 'Clickinsure API Team',
        recipients=mail.email,
        body=template.format(**mail.content),
        subtype="html")
    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)
