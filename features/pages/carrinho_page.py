from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TreinamentoPage(BasePage):

    FIRST_PRODUCT = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "a[title='Adicionado ao carrinho']")
    SUCCESS_ALERT = (By.ID, "cart_quantity50")




    def acessar_site(self):
        self.driver.get("https://automationteststore.com/")

    def esperar_pagina_login(self):
        WebDriverWait(self.driver, 10).until
        EC.visibility_of_element_located(self.USERNAME_INPUT)

    def adicionar_primeiro_produto(self):
        self.click(*self.FIRST_PRODUCT)
        self.click(*self.ADD_TO_CART_BUTTON)

    def produto_no_carrinho(self):
        return self.is_visible(*self.SUCCESS_ALERT)




