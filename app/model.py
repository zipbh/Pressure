from typing import Optional, Set, List

from uuid import uuid4

from datetime import datetime

from os import getenv

from pydbantic import DataBaseModel, PrimaryKey  # type: ignore

from pydantic import (EmailStr, Json, HttpUrl, constr, StrictBool,
                      confloat, validator)

from email_validator import validate_email, EmailNotValidError  # type: ignore

from dotenv import load_dotenv


load_dotenv()


def get_id():
    return str(uuid4())


class Reports(DataBaseModel):
    report_id: str = PrimaryKey(default=get_id)
    generated_date: datetime = datetime.now()
    scheduled_next_report: Optional[datetime]
    responsible_engineer: Partner
    report_requester: Client
    info_payload: Json
    is_signed: StrictBool = False
    signed_file_id: Optional[str]
    signature_date: Optional[datetime]
    partner_notes: Optional[constr(max_length=600)]
    client_notes: Optional[constr(max_length=600)]


class Persona(DataBaseModel):
    identification: str = PrimaryKey()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    login: Login
    address: Address
    organization: Optional['Organization']
    contacts: Contacts
    notes: Optional[constr(max_length=600)]


class Partner(Persona):
    partner_score: List[Optional['Score']] = []
    signature_api_key: Optional[str]


class Client(Persona):
    client_score: List[Optional['Score']] = []


class Organization(DataBaseModel):
    organization_id: str = PrimaryKey(default=get_id)
    business_name: str
    trade_name: str
    identification: str
    address: Address
    contacts: Contacts
    notes: Optional[constr(max_length=600)]


class Address(DataBaseModel):
    address_id: str = PrimaryKey(default=get_id)
    address: constr(max_length=60)
    second_address: Optional[constr(max_length=60)]
    city: constr(max_length=20)
    postal_code: constr(min_length=8, max_length=8)
    state: constr(max_length=20)
    country: constr(max_length=30)
    country_iso_code: Optional[constr(min_length=3, max_length=3)]
    country_unsd_code: Optional[constr(min_length=3, max_length=3)]
    notes: Optional[constr(max_length=600)]

    @validator('address')
    def address_need_space(cls, value: str) -> str:
        """Address must contain a space """
        if ' ' not in value:
            raise ValueError('Address must contain empty space')
        return value

    @validator('address')
    def address_invalid_characters(cls, value: str) -> str:
        """ Just letters and numbers are permitted """
        invalid_characters: Set[str] = {'\'\"@#$%&*(){}[]!£¢§=+\\|?/'}
        for _ in invalid_characters:
            if _ not in value:
                continue
            raise ValueError('Just letters and numbers are permitted')
        return value

    @validator('second_address')
    def second_address_need_space(cls, value: str) -> str:
        """Address must contain a space """
        if ' ' not in value:
            raise ValueError('Address must contain empty space')
        return value

    @validator('second_address')
    def second_address_invalid_characters(cls, value: str) -> str:
        """ Just letters and numbers are permitted """
        invalid_characters: Set[str] = {'\'\"@#$%&*(){}[]!£¢§=+\\|?/'}
        for _ in invalid_characters:
            if _ not in value:
                continue
            raise ValueError('Just letters and numbers are permitted')
        return value


class Contacts:
    contact_id: str = PrimaryKey(default=get_id)
    phone: constr(min_length=11, max_length=11)
    secondary_phone: Optional[constr(min_length=11, max_length=11)]
    e_mail: constr(strip_whitespace=True, to_lower=True, max_length=30)
    secondary_email: Optional[str]
    website: HttpUrl
    notes: Optional[constr(max_length=600)]

    @validator('e_mail')
    def email_must_be_valid(cls, value: EmailStr) -> EmailStr:
        """E-mail if given must be valid """
        try:
            return validate_email(value).email

        except EmailNotValidError as e:
            raise ValueError(e)


class Login:
    username: constr(strip_whitespace=True, to_lower=True,
                     max_length=int(
                         getenv('USERNAME_MAX_SIZE'))) = PrimaryKey()
    hash_kdf: constr(min_length=97, max_length=97)
    email_verified: StrictBool = False
    login_is_blocked: StrictBool = False


class Score:
    score_id: str = PrimaryKey(default=get_id)
    score_value: confloat(ge=0.0, le=5.0)


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
