from sqlalchemy.ext.asyncio import async_sessionmaker

from estacao_do_amor.src.domain.repositories.abstract_repository import AbstractReposity
from estacao_do_amor.src.domain.repositories.correio_repository import CorreioRepository
from estacao_do_amor.src.domain.repositories.podcast_repository import PodcastRepository


class Repositories:
    """
    Classe responsável por agrupar os repositórios utilizados pela aplicação.

    Atributos:
        async_session_maker (async_sessionmaker): O objeto `async_sessionmaker` utilizado para criar sessões assíncronas.

    Métodos:
        _reflection() -> None:
            Método interno que associa o objeto `async_session_maker` a todos os repositórios presentes na instância da classe.

    """

    def __init__(self, async_session_maker: async_sessionmaker) -> None:
        self.async_session_maker = async_session_maker
        self._reflection()

    def _reflection(self):
        """
        Método interno que associa o objeto `async_session_maker` a todos os repositórios presentes na instância da classe.

        Returns:
            None

        """
        for atributo in dir(self):
            if atributo.startswith("_"):
                continue
            atributo_real = getattr(self, atributo)
            if isinstance(atributo_real, AbstractReposity):
                atributo_real.async_session_maker = self.async_session_maker  # type: ignore


class Repository(Repositories):
    """
    Classe que define os repositórios utilizados pela aplicação.

    Atributos:
        empresa_repository (EmpresaRepository): O repositório para a entidade Empresa.
        filial_repository (FilialRepository): O repositório para a entidade Filial.
        usuario_repository (UsuarioRepository): O repositório para a entidade Usuário.
        xml_repository (RepositoryXML): O repositório para o XML.
        xml_dados_repository (RepositoryXMLDados): O repositório para os dados XML.

    """

    podcast_repository: PodcastRepository = PodcastRepository()
    correio_repository: CorreioRepository = CorreioRepository()
