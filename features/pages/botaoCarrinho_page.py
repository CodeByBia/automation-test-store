from features.pages.base_page import *
import time
from time import sleep

def verificar_opcoes_desabilitadas():
    options = find_elements("#option353 option")
    
    for option in options:
        if option.text != "------":
            assert option.get_attribute("disabled") == "true", f"Option '{option.text}' is not disabled"
            time.sleep(1)

def botao_add_to_cart_desabilitado():
    return not is_enabled(".cart")
    



