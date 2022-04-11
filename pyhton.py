from os import times
from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

print("hello world")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com/")

time.sleep(5)

driver.find_element_by_name("q").send_keys(
    "Zafar Naqeeb", Keys.ENTER)

time.sleep(5)

driver.quit()
