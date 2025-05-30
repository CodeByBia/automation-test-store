from features.pages.base_page import *
from time import sleep

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
