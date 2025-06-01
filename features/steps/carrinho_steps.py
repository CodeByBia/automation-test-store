from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


@given(u'que o usuário se encontra na home da loja')
def acessar_pagina_inicial(context):
    get_driver().get("https://automationteststore.com/")


@when(u'ele adiciona o primeiro produto ao carrinho')
def adicionar_ao_carrinho(context):
    base_page = BasePage(get_driver())
    base_page.click(By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")
    base_page.click(By.CSS_SELECTOR, "a.cart")


@then(u'o produto deve aparecer no carrinho')
def verificar_produto_no_carrinho(context):
    base_page = BasePage(get_driver())
    assert base_page.is_visible(By.ID, "cart_quantity50"), "Produto não foi adicionado ao carrinho."