from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class CorreioModel(Base):
    __tablename__ = "correios"

    id: Mapped[int] = mapped_column(primary_key=True)
    remetente: Mapped[str | None]
    destinatario: Mapped[str] = mapped_column(default="Anonimo")
    mensagem: Mapped[str]
    user_id: Mapped[int]
    user_name: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )


class ConfissaoModel(Base):
    __tablename__ = "confissoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str | None]
    user_id: Mapped[int | None]
    mensagem: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )


class FeedBackModel(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    user_name: Mapped[str]
    feedback: Mapped[str]
    tipo_sugestao: Mapped[str]
    pode_contato: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )


class PodcastModel(Base):
    __tablename__ = "podcasts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    link: Mapped[str]
    published: Mapped[datetime]
    image: Mapped[str]
    summary: Mapped[str]
    audio: Mapped[str]
    episode: Mapped[int]
    season: Mapped[int]
    duration: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )

    __table_args__ = (UniqueConstraint("episode", "season"),)


class UserMessageModel(Base):
    __tablename__ = "user_messages"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"<UserMessageModel {self.user_id}: {self.updated_at}>"


class CervejaModel(Base):
    __tablename__ = "cervejas"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    user_name: Mapped[str]
    data: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now(),
    )
