import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # print(homepage_nav.get_nav_links_text())
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, 'Validating nav links text'
        # homepage_nav.get_nav_link_by_name('Jewelry').click()
        elements = homepage_nav.get_nav_links()
        '''        
        for element in elements:
            element.click()
            time.sleep(3)
        '''
        for idx in range(len(elements)):
        # for idx in range(12):  # we have 12 tabs in total
            homepage_nav.get_nav_links()[idx].click()
            # print('INDEX: ' + str(idx) + ' ' + homepage_nav.get_nav_links()[idx].text)
            print(f'INDEX: {str(idx) } {homepage_nav.get_nav_links()[idx].text}')
            homepage_nav.driver.delete_all_cookies()
            time.sleep(3)
        time.sleep(15)  # implicitly wait
