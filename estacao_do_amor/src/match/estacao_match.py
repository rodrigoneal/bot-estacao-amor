from bs4 import BeautifulSoup
from pyrogram.types.user_and_chats.user import User
from pathlib import Path

match_text_template = "{username_1} and {username_2} have liked each other."


def create_match(user_1: User, user_2: User) -> str:
    html_url = r"estacao_do_amor/src/match/static/index.html"
    html_content = open(html_url, "r").read()
    soup = BeautifulSoup(html_content, "html.parser")
    match_text = soup.find(class_="NTMText")
    match_text.string = match_text_template.format(
        username_1=user_1.first_name, username_2=user_2.first_name
    )
    first_image = soup.find(class_="m1")
    second_image = soup.find(class_="m2")
    first_image.find("img").attrs["src"] = user_1.foto
    second_image.find("img").attrs["src"] = user_2.foto
    with open(html_url, 'w') as file:
        file.write(soup.prettify())
    
