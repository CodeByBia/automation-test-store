from features.pages.base_page import get_driver
from selenium.webdriver.common.by import By
import requests

LINK_FOOTER = "#footer a"

def get_all_links():
    return get_driver().find_elements(By.CSS_SELECTOR, LINK_FOOTER)

def verificar_status_link(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code
    except Exception as e:
        print(f"Erro ao verificar {url}: {e}")
        return 404
