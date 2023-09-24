from estacao_do_amor.src.domain.repositories.user_menssage_repository import (
    UserMessageRepository,
)


async def insert_if_not_exist(repository: UserMessageRepository, user_id: int):
    return await repository.get_or_create(user_id)


async def update(repository: UserMessageRepository, user_id: int):
    return await repository.update(user_id)


async def read(repository: UserMessageRepository, user_id: int):
    return await repository.read(user_id)
