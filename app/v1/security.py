from os import getenv

from dotenv import load_dotenv

from argon2 import PasswordHasher

from pydantic import StrictBool, BaseModel, constr

from typing import Set, Union


class PassWord(BaseModel):
    load_dotenv()
    password: constr(min_length=int(getenv('PASSWORD_MIN_SIZE')))
    hash_kdf: constr(min_length=97, max_length=97)


def create_kdf_hash(_password: str) -> str:
    return PasswordHasher().hash(_password)


def check_password(_kdf_hash: str, _password: str) -> Union[Exception, StrictBool]:
    try:
        PasswordHasher().verify(_kdf_hash, _password)
        return True
    except Exception as e:
        return e


def check_invalid_characters(string: str) -> str:
    invalid_characters: Set[str] = {'\'\"@#$%&*(){}[]!£¢§=+\\|?/'}
    for _ in invalid_characters:
        if _ not in string:
            continue
        raise ValueError('Just letters and numbers are and '
                         '\".\" are permitted')
    return string


panda = PassWord(
    password='onco',
    hash_kdf='asdfsdfafsfsdffpoewfsdçlfjksdfjakldsfjslkfjlsjfslfjslkjafsdkfjsdfalksajfksdjflskdflskflsakjflksdf'
)

print(panda)
