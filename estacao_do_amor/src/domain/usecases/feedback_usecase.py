from estacao_do_amor.src.domain.repositories.feedback_repository import \
    FeedBackRepository
from estacao_do_amor.src.domain.schemas.feedback_schema import FeedBack


async def create(repository: FeedBackRepository, feedback: FeedBack):
    await repository.create(feedback)
