from behave import *
from features.pages.teste_login_invalido import *
from features.pages.base_page import acessar_site


@given('que estou na página de login')
def step_impl(context):
    acessar_site()
    find_element("a[href*='account/login']").click()


@when('preencho com usuário "{usuario}" e senha "{senha}"')
def step_impl(context, usuario, senha):
    preencher_credenciais_invalidas(usuario, senha)


@when('clico no botão de login')
def step_impl(context):
    clicar_botao_login()


@then('devo ver a mensagem de erro "{mensagem}"')
def step_impl(context, mensagem):
    assert mensagem in verificar_mensagem_erro()
