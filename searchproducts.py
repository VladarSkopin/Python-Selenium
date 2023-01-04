from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://demo.magentocommerce.com/")

search_field = driver.find_element(By.NAME, 'q')
