from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PesquisaPage(BasePage):

    CATEGORY_HAIR_CARE = (By.CSS_SELECTOR, "a[href*='category&path=52']")


    def acessar_site(self):
        self.driver.get("https://automationteststore.com/")

    def abrir_categoria_hair_care(self):
        self.click(*self.CATEGORY_HAIR_CARE)

    def produtos_categoria_visiveis(self):
        return "Hair Care" in self.driver.page_source