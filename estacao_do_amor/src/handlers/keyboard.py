from pyrogram.types import InlineKeyboardMarkup
from pyromod.helpers import ikb


def create_option_keyboard(options: list[str, str]) -> InlineKeyboardMarkup:
    return ikb(
        [
            [(option[0], option[1]) for option in options],
        ]
    )
