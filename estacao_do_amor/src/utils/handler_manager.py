from functools import wraps
from typing import Coroutine

from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.domain.repositories.repositories import Repository
from estacao_do_amor.src.infra import db


def handler_manager(func: Coroutine):
    utter_message = UtterMessage()
    class_repository = func.__annotations__.get("repository")
    if class_repository:
        repository = Repository(db.async_session_maker)
        _temp_dict = {"repository": repository, "utter_message": utter_message}
    else:
        _temp_dict = {"utter_message": utter_message}

    @wraps(func)
    async def inner(*args, **kwargs):
        kwargs |= _temp_dict
        return await func(*args, **kwargs)

    return inner
