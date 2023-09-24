from estacao_do_amor.src.domain.usecases.podcast_usecase import create


async def test_se_insere_no_banco(first_episode, get_cursor, get_repository):
    repositories = get_repository
    await create(repositories.podcast_repository, first_episode)
    cursor = get_cursor
    result = cursor.execute("SELECT * FROM podcasts").fetchone()

    assert result[0] == 1
