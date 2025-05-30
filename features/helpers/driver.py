from selenium import webdriver

_driver = None

def get_driver():
    global _driver
    if _driver is None:
        raise RuntimeError("Driver não foi inicializado. Use set_driver() primeiro.")
    return _driver

def set_driver(driver):
    global _driver
    _driver = driver

def finalizar_driver():
    global _driver
    if _driver is not None:
        _driver.quit()
        _driver = None
