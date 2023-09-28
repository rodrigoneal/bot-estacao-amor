from estacao_do_amor.src.domain import usecases
from estacao_do_amor.src.domain.repositories.repositories import Repository
from pyrogram.types import Message
from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.domain import usecases


class RelatosResolver:
    def __init__(
        self,
        repository: Repository,
        message: Message,
        utter_message: UtterMessage,
    ):
        self.repository = repository
        self.message = message
        self.utter_message = utter_message

    async def feedback_resolver(self):
        feedbacks = usecases.feedback_usecase.read(
            repository=self.repository.feedback_repository
        )
        async for feedback in feedbacks:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_feedback_relatorio"
                ].text.format(
                    usuario=feedback.user_name,
                    feedback=feedback.feedback,
                    tipo=feedback.tipo_sugestao,
                    contato=feedback.pode_contato,
                )
            )

    async def correio_resolver(self):
        correios = usecases.correio_usecase.read(
            repository=self.repository.correio_repository
        )
        async for correio in correios:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_feedback_relatorio"
                ].text.format(
                    usuario=correio.user_name,
                    feedback=correio.feedback,
                    tipo=correio.tipo_sugestao,
                    contato=correio.pode_contato,
                )
            )

    async def confesso_resolver(self):
        confessos = usecases.confesso_usecase.read(
            repository=self.repository.confesso_repository
        )
        async for confesso in confessos:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_feedback_relatorio"
                ].text.format(
                    usuario=confesso.user_name,
                    feedback=confesso.feedback,
                    tipo=confesso.tipo_sugestao,
                    contato=confesso.pode_contato,
                )
            )

    async def confesso_resolver(self):
        confessos = usecases.confesso_usecase.read(
            repository=self.repository.confesso_repository
        )
        async for confesso in confessos:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_feedback_relatorio"
                ].text.format()
            )

    async def cerveja_resolver(self):
        cervejas = usecases.cerveja_usecase.read(
            repository=self.repository.cerveja_repository
        )
        async for cerveja in cervejas:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_feedback_relatorio"
                ].text.format()
            )
