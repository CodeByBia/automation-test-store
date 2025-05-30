from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, by, locator):
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def send_keys(self, text, by, locator):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def is_visible(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except:
            return False

    def get_text(self, by, locator):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.text

    def get_attribute(self, by, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.get_attribute(attribute)
