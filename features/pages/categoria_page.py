from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CategoriaPage(BasePage):
    CATEGORY_LINK = (By.CSS_SELECTOR, "a[href*='path=52']")
    CATEGORY_TITLE = (By.CSS_SELECTOR, ".maintext")

    def acessar_categoria(self):
        self.click(*self.CATEGORY_LINK)

    def categoria_carregada(self):
        return "Hair Care" in self.get_text(*self.CATEGORY_TITLE)