from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select

def clicar_logo():
    find_element(".logo").click()

def clicar_item():
    find_element(".thumbnail").click()

def clicar_carrinho():
    find_element(".cart").click()

def digitar_quantidade_decimal():
    quantity_field = find_element("#cart_quantity50") 
    quantity_field.send_keys("2.5")
    sleep(2)

def clicar_update():
    find_element("#cart_update").click()

def checar_valor_inteiro():
    quantity_field = find_element("#cart_quantity50")
    value = quantity_field.get_attribute("value")
    
    print(f"Valor atual do campo: {value}")

    if value is None:
        raise Exception("Campo de quantidade não retornou valor!")

    assert '.' not in value, f"O valor {value} não foi corrigido para inteiro"

    return value

def verificar_opcoes_desabilitadas():

    options = find_elements("#option353 option")
    
    for option in options:
        if option.text != "------":
            assert option.get_attribute("disabled") == "true", f"Option '{option.text}' is not disabled"

def botao_add_to_cart_desabilitado():
    return not is_enabled(".cart")

def ir_para_home(context):
    get_driver().get("https://automationteststore.com/index.php?rt=product/category&path=68")

def clicar_botao_carrinho():
    find_element(".productcart").click()