import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave.model_core import Status
from features.helpers.driver import set_driver, get_driver, finalizar_driver


def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    set_driver(driver)


def after_scenario(context, scenario):
    driver = get_driver()
    if scenario.status == Status.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        driver.save_screenshot(screenshot_path)
    finalizar_driver()