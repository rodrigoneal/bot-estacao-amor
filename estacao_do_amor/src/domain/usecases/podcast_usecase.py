from estacao_do_amor.src.domain.model import PodcastModel
from estacao_do_amor.src.domain.repositories.podcast_repository import (
    PodcastRepository,
)
from estacao_do_amor.src.domain.schemas.podcast_schema import Podcast


async def create(
    repository: PodcastRepository, podcast_schema: Podcast
) -> PodcastModel:
    await repository.create(podcast_schema)
