from re import T
import time
from tkinter import E
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
url = "https://www.century21.com.au/your-local-c21"
officeList = []
df = []
list = []
objlist = []

# Functions


def obj(title, email, phone):
    objlist.append({"title": title, "email": email, "phone": phone})


def getEmail(t):
    email = t
    return email


def getPhone(t):
    i = "".join(e for e in t if e.isalnum())
    if i.isdigit() == True:
        phone = i
    return phone


def getTitle(e):
    title = e.find_element(By.TAG_NAME, "title").get_attribute("id")
    title = title.replace("svgTitle0", "")
    return title


def getData(elm):
    for e in elm:
        title = getTitle(e)
        print(title, "this is title")
        list = e.find_elements(By.TAG_NAME, "a")
        for i in list:
            t = i.get_attribute("innerText")
            if t is not None:
                if "@" in t:
                    email = getEmail(t)
                if "@" not in t:
                    phone = getPhone(t)
            print(email, "this is email")
            print(phone, "this is phone")
            # obj(title, email, phone)


def getVcards(officeList):
    for i in officeList:
        print(i)
        driver.get(i)
        elm = driver.find_elements(
            By.XPATH, "//main[@id='site-main']/section[2]/div/div/div/div[2]/ul/li"
        )
        getData(elm)


def getSitelist():
    elm = driver.find_elements(
        By.XPATH, "//footer[@id='site-footer']/section/div/div/div[3]/ul/li[3]/ul/li"
    )
    for i in elm:
        link = str(i.find_element(By.TAG_NAME, "a").get_attribute("href"))
        officeList.append(link)
    getVcards(officeList)


try:
    print("Starting automated test...")
    driver.get(url)
    getSitelist()
    print(objlist)
    print("Test run successful")
    driver.quit()

except Exception as e:
    print(e)
    print("test failed")
    driver.quit()
