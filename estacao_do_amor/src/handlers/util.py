from functools import wraps
from typing import Coroutine
from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage

from estacao_do_amor.src.domain.repositories.abstract_repository import (
    AbstractReposity,
)
from estacao_do_amor.src.domain.repositories.repositories import Repository


def get_repository(class_repository: AbstractReposity) -> Repository:
    for atributo in dir(Repository):
        if atributo.startswith("_"):
            continue
        atributo_real = getattr(Repository, atributo)
        if isinstance(atributo_real, class_repository):
            return atributo_real


def handler_bot(func: Coroutine):
    utter_message = UtterMessage()
    class_repository = func.__annotations__.get("repository")
    if class_repository:
        repository = get_repository(class_repository)
        if repository:
            _temp_dict = {"repository": repository, "utter_message": utter_message}
    else:
        _temp_dict = {"utter_message": utter_message}


    @wraps(func)
    async def inner(*args, **kwargs):        
        kwargs |= _temp_dict
        return await func(*args, **kwargs)

    return inner
