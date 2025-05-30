from features.pages.base_page import *

CAMPO_LOGIN = "#loginFrm_loginname"
CAMPO_SENHA = "#loginFrm_password"
BOTAO_LOGIN = "button[title='Login']"
MENSAGEM_ERRO = ".alert-danger"

def preencher_credenciais_invalidas(usuario, senha):
    find_element(CAMPO_LOGIN).send_keys(usuario)
    find_element(CAMPO_SENHA).send_keys(senha)

def clicar_botao_login():
    find_element(BOTAO_LOGIN).click()

def verificar_mensagem_erro():
    return get_element_text(MENSAGEM_ERRO)
