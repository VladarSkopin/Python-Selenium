from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.2)

    def get_selenium_by(self, find_by: str) -> dict:  # returns dict
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'name': By.NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME,
                    'class_name': By.CLASS_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ExCon.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ExCon.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ExCon.invisibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ExCon.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ExCon.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

