from sqlalchemy.ext.asyncio import async_sessionmaker

from estacao_do_amor.src.domain.repositories.abstract_repository import \
    AbstractReposity
from estacao_do_amor.src.domain.repositories.cerveja_repository import \
    CervejaRepository
from estacao_do_amor.src.domain.repositories.confesso_repository import \
    ConfessoRepository
from estacao_do_amor.src.domain.repositories.correio_repository import \
    CorreioRepository
from estacao_do_amor.src.domain.repositories.feedback_repository import \
    FeedBackRepository
from estacao_do_amor.src.domain.repositories.podcast_repository import \
    PodcastRepository
from estacao_do_amor.src.domain.repositories.user_menssage_repository import \
    UserMessageRepository


class Repositories:
    """
    Classe responsável por agrupar os repositórios utilizados pela aplicação.

    Atributos:
        async_session_maker (async_sessionmaker): O objeto `async_sessionmaker`
         utilizado para criar sessões assíncronas.

    Métodos:
        _reflection() -> None:
            Método interno que associa o objeto `async_session_maker`
             a todos os repositórios presentes na instância da classe.

    """

    def __init__(self, async_session_maker: async_sessionmaker) -> None:
        self.async_session_maker = async_session_maker
        self._reflection()

    def _reflection(self):
        """
        Método interno que associa o objeto `async_session_maker`
          a todos os repositórios presentes na instância da classe.

        Returns:
            None

        """
        for atributo in dir(self):
            if atributo.startswith("_"):
                continue
            atributo_real = getattr(self, atributo)
            if isinstance(atributo_real, AbstractReposity):
                setattr(
                    atributo_real,
                    "async_session_maker",
                    self.async_session_maker,
                )  # type: ignore


class Repository(Repositories):
    """
    Classe que representa o Repositório.

    Esta classe é responsável por agrupar os\
          repositórios utilizados pela aplicação.

    Atributos:
        podcast_repository (PodcastRepository): \
            O repositório para gerenciar os dados de podcasts.
        correio_repository (CorreioRepository): \
            O repositório para gerenciar os dados de correio.
        user_message_repository (UserMessageRepository):\
              O repositório para gerenciar os dados de mensagens de usuário.
        confesso_repository (ConfessoRepository):\
              O repositório para gerenciar os dados de confissões.
        cerveja_repository (CervejaRepository):\
              O repositório para gerenciar os dados de cervejas.
        feedback_repository (FeedBackRepository):\
              O repositório para gerenciar os dados de feedbacks.

    """

    podcast_repository: PodcastRepository = PodcastRepository()
    correio_repository: CorreioRepository = CorreioRepository()
    user_message_repository: UserMessageRepository = UserMessageRepository()
    confesso_repository: ConfessoRepository = ConfessoRepository()
    cerveja_repository: CervejaRepository = CervejaRepository()
    feedback_repository: FeedBackRepository = FeedBackRepository()
