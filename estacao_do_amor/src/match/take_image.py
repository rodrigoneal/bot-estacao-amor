from selenium.webdriver.common.by import By
from selenium_tools.selenium_driver import SeleniumDriver


def open_browser() -> str:
    file_name = "match.png"
    driver = SeleniumDriver(headless=True).get_driver()

    driver.get(r"file:///Users/rodrigoneal/Documents/projetos/bot-estacao-do-amor/estacao_do_amor/src/match/static/index.html")
    driver.find_element(by=By.CLASS_NAME, value="match").screenshot(file_name)
    return file_name