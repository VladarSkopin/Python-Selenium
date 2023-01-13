from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()  # list[WebElement]
        nav_links_text_list = self.get_text_from_web_elements(nav_links)  # list[str]
        return Utils.join_strings(nav_links_text_list)  # str

    def get_nav_link_by_name(self, element_name) -> WebElement:
        elements = self.get_nav_links()  # List[WebElement]
        return self.get_element_by_text(elements, element_name)  # WebElement
