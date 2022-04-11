import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys





driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


# Variables

url = 'http://www.pgshf.gop.pk/'
serverIp = '116.58.23.82'



# Functions







driver.quit()
driver.close()

