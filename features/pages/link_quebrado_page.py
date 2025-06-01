from selenium.webdriver.common.by import By
import requests

class LinkQuebradoPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_all_links(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#footer a")
    
    def verificar_link(self, url):
        try:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        except:
            return False