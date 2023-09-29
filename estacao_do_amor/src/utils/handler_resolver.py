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
                    "utter_resposta_correio_relatorio"
                ].text.format(
                    remetente=correio.remetente,
                    destinatario=correio.destinatario,
                    mensagem=correio.mensagem,
                )
            )

    async def confesso_resolver(self):
        confissoes = usecases.confesso_usecase.read(
            repository=self.repository.confesso_repository
        )
        async for confesso in confissoes:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_confissao_relatorio"
                ].text.format(
                    usuario=confesso.user_name,
                    mensagem=confesso.mensagem,
                )
            )

    async def cerveja_resolver(self):
        cervejas = usecases.cerveja_usecase.read(
            repository=self.repository.cerveja_repository
        )
        async for cerveja in cervejas:
            await self.message.reply(
                self.utter_message[
                    "utter_resposta_cerveja_relatorio"
                ].text.format(
                    usuario=cerveja.user_name,
                    data=cerveja.data
                )
            )

    async def cancelar_resolver(self):
        await self.message.reply(
            self.utter_message["utter_cancelar_operacao"].text
        )

    async def resolver(self, message_type: str):
        match message_type:
            case "feedback":
                await self.feedback_resolver()
            case "correio":
                await self.correio_resolver()
            case "confissao":
                await self.confesso_resolver()
            case "cerveja":
                await self.cerveja_resolver()
            case _:
                await self.cancelar_resolver()

class CorreioResolver:
    def __init__(
        self,
        repository: Repository,
        message: Message,
        utter_message: UtterMessage,
    ):
        self.repository = repository
        self.message = message
        self.utter_message = utter_message

    async def by_text_resolver(self):
        pass