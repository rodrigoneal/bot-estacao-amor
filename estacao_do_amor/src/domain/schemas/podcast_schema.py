from datetime import datetime

from bs4 import BeautifulSoup
from dateutil.parser import parse
from pydantic import BaseModel, field_validator


class Episode(BaseModel):
    title: str
    link: str
    published: datetime
    image: str
    summary: str
    audio: str
    episode: int
    season: int
    duration: int

    @field_validator('published', mode='before')
    @classmethod
    def published_parse_to_datetime(cls, v):
        return parse(v)

    @field_validator('duration', mode='before')
    @classmethod
    def duration_parse_to_int(cls, v):
        horas, minutos, segundos = map(int, v.split(":"))
        total_segundos = (horas * 3600) + (minutos * 60) + segundos
        return total_segundos

    @field_validator('summary', mode='before')
    @classmethod    
    def summary_remove_html_syntax(cls, v):
        return BeautifulSoup(v, "html.parser").text

class Podcast(BaseModel):
    episodes: list[Episode] = []