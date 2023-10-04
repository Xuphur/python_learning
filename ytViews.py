from random import randint
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import string

# Chorme Driver settings
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)


url = "https://www.youtube.com/watch?v=0EaD1D-ZUV8"


def wait(seconds):
    time.sleep(seconds)


try:
    print("Starting automated test...")
    driver.get(url)
    wait(10)
    y = random.randint(1, 7)
    driver.find_element(By.XPATH, "//div[@id='movie_player']").send_keys(y)
    x = random.randint(40, 60)
    print("watchtime =", x)
    wait(x)
    print("Test run successful")
    driver.quit()

except Exception as e:
    print(e)
    print("test failed")
    driver.quit()
