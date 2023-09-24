from pyrogram.types import (
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from pyromod.helpers import ikb


def create_keyboard(
    options: list[str], placeholder: str
) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(option)] for option in options],
        resize_keyboard=True,
        is_persistent=True,
        one_time_keyboard=True,
        placeholder=placeholder,
    )


def create_option_keyboard(options: list[str, str]) -> InlineKeyboardMarkup:
    return ikb(
        [
            [(option[0], option[1]) for option in options],
        ]
    )
