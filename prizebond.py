from ast import Not
from multiprocessing.connection import wait
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
url = "https://hamariweb.com/finance/prizebonds/"
table = []
bond750 = [
    228566,
    676869,
    676870,
    676871,
    676872,
    676873,
    676874,
    676875,
    668159,
    586246,
    "041729",
    925973,
    333753,
    333745,
    755797,
    798799,
    829935,
    912600,
    535860,
    491617,
    677474,
    677473,
    958471,
    757143,
    352000,
    851383,
    851384,
    575063,
    413910,
    123308,
    930228,
    926401,
    881099,
    875542,
    875522,
    815432,
    799049,
    680194,
    682309,
    682308,
    603581,
    601052,
    851973,
    757062,
    757064,
    757065,
    758523,
    200079,
    609990,
    758522,
    758521,
    758545,
    758543,
    758542,
    758540,
    758539,
    206924,
    328380,
    152043,
    536113,
    757061,
    757062,
    757060,
    "022904",
    "087438",
    "098425",
    "005685",
    "071298",
]
bond200 = [
    788883,
    940213,
    562713,
    "033095",
    916993,
    439714,
    920724,
    121809,
    940272,
    995054,
    279976,
    691703,
    694050,
    695615,
    520950,
    126336,
    413872,
    212244,
    693912,
    128945,
    419932,
    498420,
    866617,
    498422,
    100709,
    609654,
    894951,
    941848,
    961983,
    454251,
    948352,
    767130,
    767133,
    230972,
    211701,
    767131,
    256338,
    256337,
    207982,
    207345,
    944189,
    562713,
    "033095",
    916993,
    940213,
    439714,
    920724,
    121809,
    940272,
    995054,
    379976,
    691703,
    694050,
    695615,
    520950,
    126336,
    143872,
    212244,
    693912,
    128945,
    419932,
    498420,
    866617,
    498422,
    100709,
    788883,
    609654,
    894951,
    941848,
    961983,
    454251,
    948352,
    767130,
    767133,
    230972,
    211701,
    767131,
]
bond100 = [
    146045,
    536040,
    536041,
    536046,
    542011,
    542049,
    542050,
    872255,
    872256,
    872257,
]

# Functions
def selectOpt(price):
    el = driver.find_element(By.XPATH, "//select[@id='PageContent_ddPB']")
    for option in el.find_elements(By.TAG_NAME, "option"):
        if option.text == price:
            option.click()


def clear():
    wait(30)
    driver.find_element(By.CLASS_NAME, "btn_clear").click()


def findResult():
    driver.find_element(By.CLASS_NAME, "btn_check").click()
    clear()


def addBondNum(list):
    for i in list:
        print(i)
        driver.find_element(By.XPATH, "//input[@id='txtNumber']").send_keys(i)
        wait(2)
        driver.find_element(By.CLASS_NAME, "btn_add").click()
        wait(2)
        # driver.find_element(
        #     By.XPATH, "//form[@id='form1']/div[3]/div[6]/div[2]/div/a"
        # ).click()
    findResult()


def dynamicTalbe():
    result = driver.find_element(By.XPATH, "//div[@id='result']/table")
    headings = result.find_elements(By.XPATH, "//tbody/tr[2]/td")
    rows = result.find_elements(By.XPATH, "//tbody/tr")
    hlist = []
    for i in headings:
        text = i.text
        hlist.append(text)
    # print(hlist)
    for i in rows:
        strs = str(rows.index(i))
        strJoin = "//tbody/tr[" + strs + "]/td"
        tds = result.find_elements(By.XPATH, strJoin)
        tdList = []
        for i in tds:
            text = i.text
            tdList.append(text)
            # print(tdList)
        tempObj = {}
        if len(tdList) > 2:
            for i in hlist:
                n = hlist.index(i)
                t = {hlist[n]: tdList[n]}
                tempObj.update(t)
                for i in table:
                    if tempObj != i and tempObj != {}:
                        table.append(tempObj)
                        print(tempObj)
        # table.append(tempObj)
    print(*table, sep="\n")
    # td = i.find_elements(By.XPATH, "//td")
    # print(td)


def getResult():
    result = driver.find_element(By.XPATH, "//div[@id='result']/table")
    bondNo = result.find_elements(By.XPATH, "//tbody/tr/td[1]")
    drawDate = result.find_elements(By.XPATH, "//tbody/tr/td[3]")
    drawNo = result.find_elements(By.XPATH, "//tbody/tr/td[4]")
    prize = result.find_elements(By.XPATH, "//tbody/tr/td[4]")

    for i in range(len(drawNo)):
        tempData = {
            "Bond No": bondNo[i + 1].text,
            "Draw Date": drawDate[i].text,
            "Draw No": drawNo[i].text,
            "Prize": prize[i].text,
        }
        table.append(tempData)


def exportResult():
    data = pd.DataFrame(table)
    data.to_excel("result.xlsx", sheet_name="sheet1", index=False)


def get100():
    price = "Rs. 100/-"
    selectOpt(price)
    addBondNum(bond100)
    # getResult()
    dynamicTalbe()


def get200():
    price = "Rs. 200/-"
    selectOpt(price)
    addBondNum(bond200)
    # getResult()
    dynamicTalbe()


def get750():
    price = "Rs. 750/-"
    selectOpt(price)
    addBondNum(bond750)
    # getResult()
    dynamicTalbe()


try:
    print("Starting automated test...")
    driver.get(url)
    wait(10)
    get100()
    get200()
    get750()
    exportResult()
    print("Test run successful")
    driver.quit()

except Exception as e:
    print(e)
    print("test failed")
    driver.quit()
