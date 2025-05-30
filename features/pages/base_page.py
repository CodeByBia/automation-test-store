from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_element(locator):
    return get_driver().find_element(By.CSS_SELECTOR, locator)

def get_element_text(locator):
    return find_element(locator).text

def wait_for_element(locator, timeout=10):
    return WebDriverWait(get_driver(), timeout).until
    EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    
def acessar_site():
    get_driver().get("https://automationteststore.com/")
    time.sleep(3)