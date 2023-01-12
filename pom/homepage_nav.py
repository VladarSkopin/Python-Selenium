from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()  # list[WebElement]
        nav_links_text = [link.text for link in nav_links]  # list[str]
        return ','.join(nav_links_text)  # to return a joined string
