from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


@given(u'que o usuário esteja na página inicial do site')
def acessar_pagina_inicial(context):
    get_driver().get("https://automationteststore.com/")


@given(u'clique em "Login or register"')
def clicar_login_register(context):
    base_page = BasePage(get_driver())
    base_page.click(By.LINK_TEXT, "Login or register")


@given(u'esteja na página de login')
def verificar_pagina_login(context):
    base_page = BasePage(get_driver())
    assert base_page.is_visible(By.ID, "loginFrm_loginname"), "Campo Username não encontrado."


@when(u'o usuário preencher o campo "Username" com "usuario_valido"')
def preencher_username(context):
    base_page = BasePage(get_driver())
    base_page.send_keys("Testeautomaçao", By.ID, "loginFrm_loginname")


@when(u'preencher o campo "Password" com "senha_valida"')
def preencher_password(context):
    base_page = BasePage(get_driver())
    base_page.send_keys("123456teste", By.ID, "loginFrm_password")


@when(u'clicar no botão "Login"')
def clicar_login(context):
    base_page = BasePage(get_driver())
    base_page.click(By.CSS_SELECTOR, "button[title='Login']")


@then(u'o usuário deve ver a mensagem "Welcome back"')
def verificar_mensagem_welcome_back(context):
    base_page = BasePage(get_driver())
    message = base_page.get_text(By.XPATH, "//*[contains(text(), 'Welcome back')]")
    assert "Welcome back" in message, f"Mensagem esperada: 'Welcome back', mas recebeu: {message}"



