import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)  # seconds
        search_box = driver.find_element(By.NAME, 'q')

        # (driver, timeout: sec, frequency -> by default = every 0.5 sec will check for condition)
        wait = WebDriverWait(driver, 15, 0.2)
        wait.until(ExCon.visibility_of_element_located(search_box))
        element = wait.until(ExCon.visibility_of_element_located((By.NAME, 'q')))
        search_box.send_keys('apple')
        search_box.submit()
