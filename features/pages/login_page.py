from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "loginFrm_loginname")
    PASSWORD_INPUT = (By.ID, "loginFrm_password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[title='Login']")
    ERROR_MSG = (By.CSS_SELECTOR, ".alert-danger")
    WELCOME_MSG = (By.XPATH, "//*[contains(text(), 'Welcome back')]")

    def fazer_login(self, usuario, senha):
        self.send_keys(usuario, *self.USERNAME_INPUT)
        self.send_keys(senha, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)

    def mensagem_erro_visivel(self):
        return self.is_visible(*self.ERROR_MSG)

    def mensagem_sucesso_visivel(self):
        return self.is_visible(*self.WELCOME_MSG)