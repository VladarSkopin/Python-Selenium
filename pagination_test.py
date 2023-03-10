import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.ui import WebDriverWait
import json

with open("data.json", "w") as f:
    json.dump([], f)


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)  # file_data = list, new_data = dict
        file_data.append(new_data)
        # sets file's current position at offset
        file.seek(0)
        # convert back to json
        json.dump(file_data, file, indent=4)


browser = webdriver.Firefox()
wait = WebDriverWait(browser, 15, 0.2)
browser.get('https://www.amazon.com/')
browser.get(
    'https://www.amazon.com/b?node=23508887011&pf_rd_r=G5SC0JMFD59WHBTN7FQ6&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=77ec5ced-4b40-44bc-97ef-3a7b846d6b30&pd_rd_w=Wagnk&pd_rd_wg=snkBx&ref_=pd_gw_unk')
figures_tile = wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Action Figures"]')),
                          'figures tile')

time.sleep(3)
figures_tile.click()

print('---------------')
print('GOING TO PAGE 1')
print('---------------')

isNextDisabled = False  # PAGINATION - if Next is disabled then it's the END of pagination
page_number = 1
product_id = 0
while not isNextDisabled:
    try:
        time.sleep(3)
        print(f'\n---------------\nPAGE = {page_number} \n---------------\n')
        element_list = wait.until(
            ExCon.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[class='a-section a-spacing-base']")))
        print(f'ELEMENTS ON PAGE {page_number} = {len(element_list)}')

        for element in element_list:
            title = element.find_element(By.TAG_NAME, 'h2').text
            img = 'No image'
            link = element.find_element(By.CSS_SELECTOR, "a[class='a-link-normal s-no-outline']").get_attribute('href')
            try:
                "div[class='a-section a-spacing-base'] img.s-image"
                img = element.find_element(By.CSS_SELECTOR, '.s-image').get_attribute("src")
            except Exception as e:
                print(f'NO IMAGE FOUND FOR "{title}" !')
                print(e)
            print(f'TITLE = {title}, \nIMAGE SRC = {img}, \nLINK = {link} \n-----')
            write_json({
                "page": page_number,
                "product_id": product_id,
                "title": title,
                "image": img,
                "link": link
            })
            product_id += 1

        # click on Next button (pagination)
        browser.find_element(By.CSS_SELECTOR,
                             "a[class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']").click()
        page_number += 1
    except Exception as e:
        print(e, 'Error. POSSIBLY THE END OF PAGINATION')
        isNextDisabled = True

time.sleep(10)
browser.quit()
