import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Chorme Driver settings
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


def wait(seconds):
    time.sleep(seconds)


# Variables
url = "https://beoe.gov.pk/foreign-jobs?job_title=driver&min_salary=1500&currency=SAR&page="
table = []


try:
    print("Starting automated test...")
    i = "1"
    driver.get(url + i)
    wait(30)
    print("Test run successful")
    driver.quit()

except Exception as e:
    print(e)
    print("test failed")
    driver.quit()
