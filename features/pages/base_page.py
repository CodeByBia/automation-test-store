from selenium.webdriver.common.by import By
from features.helpers.driver import get_driver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

def find_elements(self, locator):
        return self.driver.find_elements(By.CSS_SELECTOR, locator)

def get_element_text(self, locator):
        return self.find_element(locator).text

    
def get_element_text_get_attribute(self, locator):
        return self.find_element(locator).get_attribute("value")

def is_enabled(self, locator):
        return self.find_element(locator).is_enabled()
