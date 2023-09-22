from estacao_do_amor.src.domain.model import PodcastModel
from estacao_do_amor.src.domain.repositories.podcast_repository import \
    PodcastRepository
from estacao_do_amor.src.domain.schemas.podcast_schema import Podcast
from estacao_do_amor.src.feed.feed_rss import AnchorFeed


async def create(repository: PodcastRepository, podcast_schema: Podcast) -> PodcastModel:
    podcast_model = await repository.create(podcast_schema)
