from typing import NamedTuple

import yaml
from pyrogram.types import InlineKeyboardMarkup


class DataMessage(NamedTuple):
    text: str
    keyboard: InlineKeyboardMarkup

    def __repr__(self) -> str:
        return self.text

    def to_dict(self) -> dict[str, str | InlineKeyboardMarkup | None]:
        return {"text": self.text, "reply_markup": self.keyboard}


class UtterMessage:
    def __init__(self):
        with open("domain.yml", "r", encoding="utf-8") as stream:
            try:
                self.yaml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                raise exc

    def __getitem__(self, name) -> DataMessage:
        from estacao_do_amor.src.handlers.keyboard import (
            create_option_keyboard,
        )

        data = self.yaml_data["responses"][name]
        text = data[0]["text"]
        keyboard = None
        try:
            keyboard_data = data[1].get("buttons")
            values = [
                (data["title"], data["payload"]) for data in keyboard_data
            ]
            keyboard = create_option_keyboard(values)
        except (IndexError, KeyError):
            pass

        return DataMessage(text, keyboard)
