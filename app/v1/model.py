from typing import Optional, List

from uuid import uuid4

from datetime import datetime

from pydbantic import DataBaseModel, PrimaryKey  # type: ignore

from pydantic import (EmailStr, Json, HttpUrl, StrictBool,validator)

from email_validator import validate_email, EmailNotValidError  # type: ignore


def get_id():
    return str(uuid4())


class Login(DataBaseModel):
    username: str = PrimaryKey()
    hash_kdf: str
    email_verified: StrictBool = False
    login_is_blocked: StrictBool = False

    @validator('username')
    def username_cant_have_space(cls, value: str) -> str:
        """Username can't have empty space"""
        if ' ' in value:
            raise ValueError('Address can\'t contain empty space')
        return value


class Address(DataBaseModel):
    address_id: str = PrimaryKey(default=get_id)
    address: str
    second_address: Optional[str]
    city: str
    postal_code: str
    state: str
    country: str
    country_iso_code: Optional[str]
    country_unsd_code: Optional[str]
    notes: Optional[str]

    @validator('address')
    def address_need_space(cls, value: str) -> str:
        """Address must contain a space """
        if ' ' not in value:
            raise ValueError('Address must contain empty space')
        return value

    @validator('second_address')
    def second_address_need_space(cls, value: str) -> str:
        """Address must contain a space """
        if ' ' not in value:
            raise ValueError('Address must contain empty space')
        return value


class Contacts(DataBaseModel):
    contact_id: str = PrimaryKey(default=get_id)
    phone: str
    secondary_phone: Optional[str]
    e_mail: str
    secondary_email: Optional[str]
    website: HttpUrl
    notes: Optional[str]

    @validator('e_mail')
    def email_must_be_valid(cls, value: EmailStr) -> EmailStr:
        """E-mail if given must be valid """
        try:
            return validate_email(value).email

        except EmailNotValidError as e:
            raise ValueError(e)


class Persona(DataBaseModel):
    identification: str = PrimaryKey()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    login: Login
    address: Address
    organization: Optional['Organization']
    contacts: Contacts
    notes: Optional[str]


class Partner(Persona):
    signature_api_key: Optional[str]


class Organization(DataBaseModel):
    organization_id: str = PrimaryKey(default=get_id)
    business_name: str
    trade_name: str
    identification: str
    address: Address
    contacts: Contacts
    notes: Optional[str]


class Reports(DataBaseModel):
    report_id: str = PrimaryKey(default=get_id)
    generated_date: datetime = datetime.now()
    scheduled_next_report: Optional[datetime]
    responsible_engineer: Partner
    report_requester: Persona
    client_score: Optional[float]
    partner_score: Optional[float]
    info_payload: str
    is_signed: StrictBool = False
    signed_file_id: Optional[str]
    signature_date: Optional[datetime]
    partner_notes: Optional[str]
    client_notes: Optional[str]


def tables_list():
    """
    Create a list of all models to be used in other modules
    @return: List of all models except Persona
    """
    import sys
    import inspect
    return [name for name, obj in
            inspect.getmembers(sys.modules[__name__],
            inspect.isclass) if obj.__module__ is __name__
            if name != 'Persona']
