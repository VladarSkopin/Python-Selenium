from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.2)

    def __get_selenium_by(self, find_by: str) -> dict:  # returns dict
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
        return self.__wait.until(ExCon.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ExCon.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ExCon.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ExCon.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ExCon.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    #  ExCon.element_to_be_clickable()  # to click a button
