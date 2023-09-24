from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class CorreioModel(Base):
    __tablename__ = "correios"

    id: Mapped[int] = mapped_column(primary_key=True)
    remetente: Mapped[str | None] = mapped_column()
    destinatario: Mapped[str] = mapped_column()
    mensagem: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )


class ConfissaoModel(Base):
    __tablename__ = "confissoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    remetente: Mapped[str | None] = mapped_column()
    mensagem: Mapped[str] = mapped_column()
    data: Mapped[datetime] = mapped_column(
        default=func.now(),
    )


class SugestaoModel(Base):
    __tablename__ = "sugestoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    remetente: Mapped[str | None] = mapped_column()
    mensagem: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
    )


class PodcastModel(Base):
    __tablename__ = "podcasts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column()
    published: Mapped[datetime] = mapped_column()
    image: Mapped[str] = mapped_column()
    summary: Mapped[str] = mapped_column()
    audio: Mapped[str] = mapped_column()
    episode: Mapped[int] = mapped_column()
    season: Mapped[int] = mapped_column()
    duration: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        default=func.now(),
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
