from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


@given(u'que o visitante está na página principal do site')
def acessar_pagina_inicial(context):
    get_driver().get("https://automationteststore.com/")


@when(u'ele clica na categoria "Hair Care"')
def clicar_categoria(context):
    base_page = BasePage(get_driver())
    base_page.click(By.CSS_SELECTOR, "a[href*='category&path=52']")


@then(u'os produtos da categoria devem ser exibidos')
def verificar_produtos_categoria(context):
    base_page = BasePage(get_driver())
    produtos = base_page.get_text(By.CSS_SELECTOR, ".contentpanel")
    assert "Shampoo" in produtos, "Produtos da categoria 'Hair Care' não estão visíveis."
    assert "Conditioner" in produtos, "Produtos da categoria 'Hair Care' não estão visíveis."