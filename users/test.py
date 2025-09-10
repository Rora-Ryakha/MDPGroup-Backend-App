import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By


browser = wd.Firefox()
browser.get("https://egrul.nalog.ru/index.html")
search = browser.find_element(by=By.ID, value="query")
search.send_keys("3461059265")
time.sleep(3)
button = browser.find_element(by=By.ID, value="btnSearch")
button.click()
time.sleep(3)
result = browser.find_element(by=By.CLASS_NAME, value="res-caption")
print(result.text)