from estacao_do_amor.src.dispatch.parser_yaml import UtterMessage
from estacao_do_amor.src.handlers.keyboard import create_option_keyboard

utter_message = UtterMessage()

def test_se_pega_os_valores_do_yaml():
    response_message = utter_message["utter_identicar_correio"]
    assert response_message.text == "Deseja se identificar? 🤔"
    assert response_message.keyboard == create_option_keyboard(["Sim", "Não"])