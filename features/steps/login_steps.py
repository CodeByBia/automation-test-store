from behave import when, then
from features.pages.treinamento_page import TreinamentoPage

@when('preencho com usuário "{usuario}" e senha "{senha}"')
def step_impl(context, usuario, senha):
    context.login_page = TreinamentoPage(context.driver)
    context.login_page.preencher_credenciais(usuario, senha)

@when('clico no botão de login')
def step_impl(context):
    context.login_page.clicar_login()

@then('vejo a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    if "Error" in mensagem:
        assert context.login_page.mensagem_erro_visivel()
    else:
        assert context.login_page.mensagem_bem_vindo_visivel()