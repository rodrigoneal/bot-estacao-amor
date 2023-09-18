from selenium_tools.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By

def open_browser() -> str:
    file_name = "match.png"
    driver = SeleniumDriver().get_driver()

    driver.get(r"file:///Users/rodrigoneal/Documents/projetos/bot-estacao-do-amor/estacao_do_amor/src/match/static/index.html")
    breakpoint()
    driver.find_element(by=By.CLASS_NAME, value="match").screenshot(file_name)
    return file_name