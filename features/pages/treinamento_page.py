from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TreinamentoPage(BasePage):

    LOGIN_LINK = (By.LINK_TEXT, "Login or register")
    USERNAME_INPUT = (By.ID, "loginFrm_loginname")
    PASSWORD_INPUT = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    WELCOME_MESSAGE = (By.XPATH, "//*[contains(text(), 'Welcome back')]")


    def acessar_site(self):
        self.driver.get("https://automationteststore.com/")

    def esperar_pagina_login(self):
        WebDriverWait(self.driver, 10).until
        EC.visibility_of_element_located(self.USERNAME_INPUT)

    def preencher_username(self, nome):
        self.send_keys(nome, *self.USERNAME_INPUT)

    def preencher_password(self, senha):
        self.send_keys(senha, *self.PASSWORD_INPUT)

    def clicar_botao_login(self):
        self.click(*self.LOGIN_BUTTON)

    def mensagem_bem_vindo_exibida(self):
        return self.is_visible(*self.WELCOME_MESSAGE)

