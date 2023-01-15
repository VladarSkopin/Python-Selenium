import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait


browser = webdriver.Firefox()
wait = WebDriverWait(browser, 15, 0.2)
browser.get('https://www.amazon.com/')
# see_more_link = wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, "a[href='https://www.amazon.com/b?node=23508887011&pf_rd_r=S4EF16JAAP6PZFAQ6P6G&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=5d9f1111-7868-48f6-9ce7-7a2513d9d304&pd_rd_w=OA1tE&pd_rd_wg=hJy5U&ref_=pd_gw_unk']")), '"see more" link')
# see_more_link.click()
time.sleep(3)
browser.get('https://www.amazon.com/b?node=23508887011&pf_rd_r=G5SC0JMFD59WHBTN7FQ6&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=77ec5ced-4b40-44bc-97ef-3a7b846d6b30&pd_rd_w=Wagnk&pd_rd_wg=snkBx&ref_=pd_gw_unk')
figures_tile = wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Action Figures"]')), 'figures tile')

time.sleep(3)

figures_tile.click()
'''div_list = wait.until(ExCon.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.bxc-grid-overlay")), 'div list')
print(len(div_list))  # 15
for item in div_list:
    print(item.text)'''
time.sleep(3)
browser.save_screenshot('figures_page_1.png')

element_list = wait.until(ExCon.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='a-section a-spacing-base']")))
print(len(element_list))
for element in element_list:
    print(f'TEXT = {element.text}')

time.sleep(3)
print('---------------')
print('GOING TO PAGE 3')
print('---------------')

page_3 = wait.until(ExCon.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Go to page 3']")))
page_3.click()
time.sleep(3)
element_list_2 = wait.until(ExCon.visibility_of_all_elements_located((By.TAG_NAME, "h2")))
print(len(element_list_2))
for element in element_list_2:
    print(f'TITLE = {element.text}')

time.sleep(3)
browser.save_screenshot('figures_page_3.png')
browser.back()

print('---------------')
print('GOING BACK TO PAGE 1')
print('---------------')

# refresh stale elements on page 1
element_list = wait.until(ExCon.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='a-section a-spacing-base']")))

for element in element_list:
    title = element.find_element(By.TAG_NAME, 'h2').text
    img = 'No image'
    try:
        "div[class='a-section a-spacing-base'] img.s-image"
        # img = wait.until(ExCon.visibility_of_element_located(element.find_element(By.CSS_SELECTOR, '.s-image')), 'img src').get_attribute("src")
        img = element.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
    except:
        print(f'NO IMAGE FOUND FOR "{title}" !')
    print(f'TITLE = {title}, \nIMAGE SRC = {img}')

time.sleep(10)
browser.quit()
