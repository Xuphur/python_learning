from ast import Not
from multiprocessing.connection import wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
from tkinter import *
from tkinter import filedialog
from datetime import date

# Chorme Driver settings

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


# Variables

url = "https://hamariweb.com/finance/prizebonds/"
table = []


# Functions


def wait(seconds):
    time.sleep(seconds)


def exportResult(l, s):
    data = pd.DataFrame(l)
    with pd.ExcelWriter("result.xlsx", mode="a", if_sheet_exists="replace") as writer:
        data.to_excel(writer, sheet_name=s)


def newPrize(s):
    mylist = list(dict.fromkeys(table))
    exportResult(mylist, s)


def clear():
    wait(5)
    driver.find_element(By.CLASS_NAME, "btn_clear").click()


def getResult():
    result = driver.find_element(By.XPATH, "//div[@id='result']/table")
    bondNo = result.find_elements(By.XPATH, "//tbody/tr/td[1]")
    PrizeValue = result.find_elements(By.XPATH, "//tbody/tr/td[2]")
    drawDate = result.find_elements(By.XPATH, "//tbody/tr/td[3]")
    drawNo = result.find_elements(By.XPATH, "//tbody/tr/td[4]")
    prize = result.find_elements(By.XPATH, "//tbody/tr/td[4]")
    # for i in range(len(drawNo)):
    for i in range(len(drawNo)):
        tempData = {
            "Bond No": bondNo[i + 1].text,
            "Draw Date": drawDate[i].text,
            "Draw No": drawNo[i].text,
            "Prize": prize[i].text,
            "Prize Value": PrizeValue[i].text,
        }
        print(tempData)
        table.append(tempData)
    clear()


def findResult():
    driver.find_element(By.CLASS_NAME, "btn_check").click()
    wait(5)
    getResult()


def addNum(n):
    driver.find_element(By.XPATH, "//input[@id='txtNumber']").send_keys(n)
    wait(1)
    driver.find_element(By.CLASS_NAME, "btn_add").click()


def addBondNum(list):
    for i in list:
        # print(i)
        x = str(i).replace(".0", "")
        if len(x) < 6:
            n = "0" + x
            addNum(n)
        else:
            addNum(x)
    findResult()


def sliceIt(bondNum, s):
    bondNum2 = bondNum.dropna()
    start = 0
    end = len(bondNum2)
    step = 20
    for i in range(start, end, step):
        x = i
        b = bondNum2[x : x + step]
        addBondNum(b)
    newPrize(s)


def selectOpt(price):
    el = driver.find_element(By.XPATH, "//select[@id='PageContent_ddPB']")
    for option in el.find_elements(By.TAG_NAME, "option"):
        if option.text == price:
            option.click()
    wait(2)
    el = driver.find_element(By.XPATH, "//select[@id='PageContent_ddDraws']")
    for option in el.find_elements(By.TAG_NAME, "option"):
        if option.text == "All Draws":
            option.click()


def get100(df):
    s = "Walda 100"
    price = "Rs. 100/-"
    selectOpt(price)
    bondNum = df.walda_100
    sliceIt(bondNum, s)


def getWalda200(df):
    s = "Walda 200"
    price = "Rs. 200/-"
    selectOpt(price)
    bondNum = df.walda_200
    sliceIt(bondNum, s)


def get200(df):
    s = "bond 200"
    price = "Rs. 200/-"
    selectOpt(price)
    bondNum = df.bond_200
    sliceIt(bondNum, s)
    # addBondNum(bondNum, s)


def get750(df):
    s = "Walda 750"
    price = "Rs. 750/-"
    selectOpt(price)
    bondNum = df.walda_750
    sliceIt(bondNum, s)


def getCsv():
    filePath = ""
    filePath = filedialog.askopenfilename()
    file = open(filePath, "r")
    df = pd.read_csv(filePath)
    file.close()
    # get100(df)
    # getWalda200(df)
    # get750(df)
    get200(df)


try:
    print("Starting automated test...")
    driver.get(url)
    wait(5)
    getCsv()
    print("Test run successful")
    driver.quit()

except Exception as e:
    print(e)
    print("test failed")
    # driver.quit()
