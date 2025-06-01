from behave import given, when, then
from features.pages.pesquisa_page import PesquisaPage

@given('que estou na página inicial')
def step_acessar_pagina(context):
    context.page = PesquisaPage(context.driver)
    context.page.acessar_site()

@when('pesquiso pelo termo "{termo}"')
def step_pesquisar_produto(context, termo):
    context.page.pesquisar_produto(termo)

@then('devo ver a mensagem "Products meeting the search criteria"')
def step_verificar_mensagem(context):
    assert "Products meeting the search criteria" in context.driver.page_source
