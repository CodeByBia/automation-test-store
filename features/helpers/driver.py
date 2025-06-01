# _driver = None

# def set_driver(instance):
#     global _driver
#     _driver = instance

# def get_driver():
#     if _driver is None:
#         raise RuntimeError("Driver não foi inicializado! Verifique o before_scenario.")
#     return _driver
    
# #seta o driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

_driver = None

def init_driver(headless=False):
    global _driver
    if _driver is not None:
        return _driver
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    if headless:
        options.add_argument("--headless=new")
    
    service = Service(ChromeDriverManager().install())
    _driver = webdriver.Chrome(service=service, options=options)
    _driver.implicitly_wait(10)
    return _driver

def get_driver():
    if _driver is None:
        raise RuntimeError("Driver não inicializado. Chame init_driver() primeiro.")
    return _driver

def quit_driver():
    global _driver
    if _driver is not None:
        _driver.quit()
        _driver = None