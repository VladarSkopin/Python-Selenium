import time
# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait


email = 'washastdupirozhok@gmail.com'
password = 'h7D*12lB'

# browser = webdriver.Chrome()
browser = uc.Chrome()
wait = WebDriverWait(browser, 15, 0.2)
browser.get('https://accounts.google.com/v3/signin/identifier?dsh=S403206861%3A1673803940165995&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AeAAQh6uKfGSBqe5uHGqgwmHpapUNA2Jr3iPbWDGWs3Z2KrgcK1Yn4rNwHI0waozntO_M4NOqUXG')

browser.find_element(By.ID, 'identifierId').send_keys(email)
time.sleep(3)
wait.until(ExCon.element_to_be_clickable((By.CSS_SELECTOR, '#identifierNext > div > button > span')), 'Next button').click()
".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)"

password_field = browser.find_element(By.CSS_SELECTOR, "#password > div > div > input")
password_field.send_keys(password)
time.sleep(3)
password_field.submit()  # ENTER

time.sleep(100)
browser.quit()
