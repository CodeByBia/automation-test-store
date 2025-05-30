from features.helpers.driver import get_driver
from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PesquisaPage(BasePage):
    SEARCH_INPUT = (By.NAME, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div.button-in-search")



    def acessar_site(self):
        self.driver.get("https://automationteststore.com/")

    def pesquisar_produto(self, termo):
        self.send_keys(termo, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def resultado_contem_termo(self, termo):
        return termo.lower() in self.driver.page_source.lower()
