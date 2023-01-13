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
        homepage_nav.get_nav_link_by_name('Jewelry').click()
        time.sleep(5)  # implicitly wait for 5 seconds

        'https://www.macys.com/shop/jewelry-watches?id=544&cm_sp=us_hdr-_-jewelry-_-544_jewelry'
