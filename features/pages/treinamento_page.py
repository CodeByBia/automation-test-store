from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage  # Importe apenas a BasePage

class TreinamentoPage(BasePage):
    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Login or register")
    USERNAME_INPUT = (By.ID, "loginFrm_loginname")
    PASSWORD_INPUT = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    WELCOME_MESSAGE = (By.XPATH, "//*[contains(text(), 'Welcome back')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    def acessar_pagina_login(self):
        self.click(*self.LOGIN_LINK)

    def preencher_credenciais(self, usuario, senha):
        self.send_keys(usuario, *self.USERNAME_INPUT)
        self.send_keys(senha, *self.PASSWORD_INPUT)

    def clicar_login(self):
        self.click(*self.LOGIN_BUTTON)

    def mensagem_bem_vindo_visivel(self):
        return self.is_visible(*self.WELCOME_MESSAGE)

    def mensagem_erro_visivel(self):
        return self.is_visible(*self.ERROR_MESSAGE)