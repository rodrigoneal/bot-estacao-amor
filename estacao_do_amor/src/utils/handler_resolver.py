from tempfile import NamedTemporaryFile
from typing import TypeVar
from estacao_do_amor.src.audio_video.voice_message import text_to_voice
from estacao_do_amor.src.domain import usecases
from estacao_do_amor.src.domain.repositories.repositories import Repository
from pyrogram.types import Message
from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.domain import usecases
from pyrogram.types.messages_and_media.message import Message as MessageResponse

from estacao_do_amor.src.domain.schemas.confesso_schema import Confesso


T = TypeVar("T", bound=Confesso)

# TODO: Fazer com que mensagens longas fiquem salvas, pois o ask só pega uma mensagem.

class RelatosResolver:
    def __init__(
        self,
        repository: Repository,
        message: Message,
        utter_message: UtterMessage,
    ):
        self.repository = repository
        self.message: Message = message
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

    async def long_message(self, mensagem: T):
        await self.message.reply(
            self.utter_message[
                "utter_resposta_confissao_longa_relatorio"
            ].text.format(usuario=mensagem.user_name)
        )
        for i in range(0, len(mensagem.mensagem), 300):
            await self.message.reply(mensagem.mensagem[i : i + 300])
        await self.message.reply(f"FIM DA MENSAGEM DE {mensagem.user_name}")

    async def confesso_resolver(self):
        confissoes = usecases.confesso_usecase.read(
            repository=self.repository.confesso_repository
        )
        async for confesso in confissoes:
            if len(confesso.mensagem) > 300:
                await self.long_message_resolver(mensagem=confesso)
                continue

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
                ].text.format(usuario=cerveja.user_name, data=cerveja.data)
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

    async def progress_send_audio(self, current:int, total:int, message: MessageResponse):
        enviado = (current / total) * 100
        text = f"Enviando audio: {round(enviado, 2)}% Concluído."
        await message.edit_text(text)

    async def long_message_audio(self, mensagem: T):
        _mensagem = mensagem.mensagem
        mensagens:list[str] = _mensagem.replace("...", ".").strip().split(".")
        mensagens.insert(0, f"Mensagem de {mensagem.user_name}")
        for i in range(0, len(mensagens), 10):
            _m = ". ".join(mensagens[i : i + 10])
            with NamedTemporaryFile(suffix=".mp3", delete=True) as f:
                message = await self.message.reply(
                    self.utter_message["utter_mensagem_aviso_audio"]
                )
                text_to_voice(text=_m, file_name=f.name)
                await self.message.reply_voice(voice=f.name, progress=self.progress_send_audio, progress_args=(message,))
            await message.delete()

    async def long_message_resolver(self, mensagem: T):
        tipo_response = await self.message.reply(
            **self.utter_message["utter_mensagem_muito_longa"].to_dict()
        )
        click_response = await tipo_response.wait_for_click()
        await click_response.message.edit_text(
            f"{click_response.message.text} = {click_response.data}"
        )
        if click_response.data == "audio":
            await self.long_message_audio(mensagem=mensagem)
        elif click_response.data == "texto":
            await self.long_message(mensagem=mensagem)
        else:
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
