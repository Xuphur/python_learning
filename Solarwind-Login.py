import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
from requests import get, post

# initialize the chrome browser

print('Starting Test ...')


def wait(seconds):
    time.sleep(seconds)

# for getting ChromeDriver from jenkins


chrome_driver = "/home/kafkaadmin/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=chrome_driver)
print('Chrome driver found')
driver.get(
    'http://solarwinds.travelresorts.com/Orion/Login.aspx?ReturnUrl=%2f')

wait(5)

elem = driver.find_element_by_xpath('//*[@id="ctl00_BodyContent_Username"]')
elem.send_keys("admin")

wait(3)

elem = driver.find_element_by_xpath('//*[@id="ctl00_BodyContent_Password"]')
elem.send_keys("p0;oil")

wait(3)

elem = driver.find_element_by_xpath('//*[@id="ctl00_BodyContent_LoginButton"]')
elem.click()

wait(15)

elam = driver.find_element_by_xpath(
    '//*[@id="aspnetForm"]/div[4]/h1')

wait(5)

assert elam.text == 'Orion Summary Home', 'Login failed.'
print('Solarwinds live login test ran successfully')

driver.close()
