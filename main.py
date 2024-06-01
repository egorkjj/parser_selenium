from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

inp = input()
name = inp.replace(" ", "+") if inp.find(" ") != -1 else inp

options = webdriver.ChromeOptions()
options.add_argument('--headless')

with webdriver.Chrome(options=options) as browser:
    while True:
        try:
            browser.get(f'https://yandex.ru/images/search?text={name}')
            WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located)
            el = browser.find_element(By.CLASS_NAME, "ContentImage-Image")
            # browser.close()
            url = el.get_attribute("src")
            img_data = requests.get(url).content
            with open('image.jpg', 'wb') as handler:
                handler.write(img_data)
            break
        except Exception as e:
            print(e)
            continue
