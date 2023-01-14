import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        cookies = homepage_nav.driver.get_cookies()
        cookie_names = [cookie['name'] for cookie in cookies]
        print(f'COOKIES: {cookies}')
        print('---------------')
        print(cookie_names)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, 'Validating nav links text'
        elements = homepage_nav.get_nav_links()

        for idx in range(len(elements)):
            homepage_nav.get_nav_links()[idx].click()
            for cookie_name in cookie_names:
                homepage_nav.driver.delete_cookie(cookie_name)
                homepage_nav.driver.refresh()
                homepage_nav.is_visible('tag_name', 'h1', cookie_name)

        '''        
        for element in elements:
            element.click()
            time.sleep(3)
        '''
        '''        
        for idx in range(len(elements)):
            print(f'INDEX: {str(idx)} {homepage_nav.get_nav_links()[idx].text}')
            homepage_nav.get_nav_links()[idx].click()
            homepage_nav.driver.delete_all_cookies()  # NOT a good practice -> must find which cookies to delete!
            time.sleep(3)
        '''
        time.sleep(15)  # implicitly wait
