from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CarrinhoPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "a[title='Add to Cart']")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_contents")
    
    def adicionar_produto(self):
        self.click(*self.ADD_TO_CART_BTN)

    def item_no_carrinho(self):
        return self.is_visible(*self.CART_ITEMS)