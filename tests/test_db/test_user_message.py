from asyncio import sleep

from estacao_do_amor.src.domain.usecases.user_message_usecase import (
    insert_if_not_exist, read, update)


async def test_se_cria_um_novo_usuario_se_nao_existe(get_repository):
    repositories = get_repository
    result = await insert_if_not_exist(repositories.user_message_repository, 1)
    assert result.created_at


async def test_se_atualiza_o_usuario_se_existe(get_repository):
    repositories = get_repository
    first_query = await insert_if_not_exist(
        repositories.user_message_repository, 2
    )
    await sleep(5)
    await update(repositories.user_message_repository, 2)
    second_query = await read(repositories.user_message_repository, 2)
    assert not first_query.updated_at == second_query.updated_at
