import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tkinter import *
from tkinter import filedialog
import webbrowser


# Windows
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


# Variables

url = "http://www.pgshf.gop.pk/"
serverIp = "http://116.58.23.82/search/login.asp"
filePath = ""
username = "Javed"
password = "zaroon456789"


# Functions


def getCsvPath():
    filePath = filedialog.askopenfilename()
    file = open(filePath, "r")
    df = pd.read_csv(filePath)
    r = df.loc[0, :]
    print(r)
    # playDataFrame()
    file.close()


def selectCSV():
    window = Tk()
    button = Button(text="Open CSV", command=getCsvPath)
    button.pack()
    window.mainloop()
    getCsvPath()


def login():
    driver.find_element(By.NAME, "login").send_keys(username)
    driver.find_element(By.NAME, "psw").send_keys(username)


try:
    print("Starting automated test...")
    # selectCSV()
    webbrowser.get(chrome_path).open(url)
    # driver.get(serverIp)
    # login()
    # print("Test run successful")
    # driver.quit()

except Exception as e:
    print(e)
    # print("test failed")
    # driver.quit()


driver.quit()
driver.close()
