from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TermoInvalidoPage(BasePage):
    SEARCH_INPUT = (By.NAME, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div.button-in-search")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, ".contentpanel")

    def pesquisar_termo_invalido(self, termo):
        self.send_keys(termo, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)

    def mensagem_sem_resultados(self):
        return "No results" in self.get_text(*self.NO_RESULTS_MSG)