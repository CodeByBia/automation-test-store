from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


@given(u'que o usuário está na página inicial da loja')
def acessar_pagina_inicial(context):
    get_driver().get("https://automationteststore.com/")


@when(u'ele pesquisa por "shampoo"')
def pesquisar_produto(context):
    base_page = BasePage(get_driver())
    base_page.send_keys("shampoo", By.NAME, "filter_keyword")
    base_page.click(By.CSS_SELECTOR, "div.button-in-search")


@then(u'os resultados da pesquisa devem conter o termo "shampoo"')
def verificar_resultados_pesquisa(context):
    base_page = BasePage(get_driver())
    resultados = base_page.get_text(By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")
    assert "shampoo" in resultados.lower(), f"Esperado: 'shampoo' nos resultados. Recebido: {resultados}"