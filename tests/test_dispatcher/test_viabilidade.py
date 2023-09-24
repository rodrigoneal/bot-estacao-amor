# Testando se é viavel usar um arquivo yaml para gerenciar as conversas.

import yaml

from estacao_do_amor.src.dispatch.request_components import RequestHandler

def test_se_e_viavel_usar_um_arquivo_yaml_para_gerenciar_as_conversas():
    request_handler = RequestHandler(func_name='command_confesso_private_handler')
    request_handler.can_handle()
    breakpoint()

    