import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.campoQuantidade_page import *

@given('que o user está na home page')
def ir_para_home_step(context):
    get_driver().get("https://automationteststore.com/")

@when('o user clicar no item')
def clicar_item_step(context):
    clicar_item()
    sleep(2)  

@when('clicar no botão de adicionar ao carrinho')
def clicar_botao_carrinho_step(context):
    clicar_carrinho()
    sleep(2)  

@when('digitar um número decimal no campo de quantidade')
def digitar_quantidade_decimal_step(context):
    digitar_quantidade_decimal()
    sleep(2)  

@when('clicar em update')
def clicar_update_step(context):
    clicar_update()
    sleep(3) 

@then('o sistema deve corrigir o número para um inteiro')
def checar_valor_inteiro_step(context):
    checar_valor_inteiro()
    