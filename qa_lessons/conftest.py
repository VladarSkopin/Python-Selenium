import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# create our own fixtures
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1200,600')
    return options


# "--headless" -> without a UI
# "--start-maximized" -> regardless of any previous settings
# "--window-size" -> sets the initial window size

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(executable_path='C:/user/123/...', options=options)  # custom driver path
    return driver


@pytest.fixture(scope='function')  # scope='session' -> for the whole browser, scope='funcion' -> to run in parallel
def setup(request, get_webdriver):  # request = built-in fixture
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)  # if request is not a class
    driver.delete_all_cookies()
    yield driver
    driver.quit()  # close the whole browser
