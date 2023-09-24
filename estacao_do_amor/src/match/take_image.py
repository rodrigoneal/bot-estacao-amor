from pathlib import Path

from selenium.webdriver.common.by import By
from selenium_tools.selenium_driver import SeleniumDriver

from estacao_do_amor.src import CONSTANTS


def download_image_match(file_name: str) -> str:
    driver = SeleniumDriver(headless=True).get_driver()
    index_html = Path(CONSTANTS.URI_INDEX).absolute().as_uri()
    driver.get(index_html)
    driver.find_element(by=By.CLASS_NAME, value="match").screenshot(file_name)
    driver.quit()
