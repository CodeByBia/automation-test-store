from behave import *
from features.pages.termo_invalido import *

@when('pesquiso pelo termo "{termo}"')
def step_impl(context, termo):
    pesquisar_termo(termo)

@then('devo ver a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    assert mensagem in verificar_mensagem()