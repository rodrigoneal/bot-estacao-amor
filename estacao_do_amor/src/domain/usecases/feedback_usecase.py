from estacao_do_amor.src.domain.repositories.feedback_repository import \
    FeedBackRepository
from estacao_do_amor.src.domain.schemas.feedback_schema import FeedBack, FeedBackRead


async def create(repository: FeedBackRepository, feedback: FeedBack):
    await repository.create(feedback)

async def read(repository: FeedBackRepository):
    feedbacks_model = await repository.read()
    for feedback in feedbacks_model:
        yield FeedBackRead.model_validate(feedback)

