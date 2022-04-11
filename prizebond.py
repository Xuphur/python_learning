import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

url = "https://hamariweb.com/finance/prizebonds/"
bond750 = [
333753,333745,755797,798799,829935,912600,535860,491617,677474,677473,958471,757143,352000,851383,851384,575063,
413910,123308,930228,926401,881099,875542,875522,815432,799049,680194,682309,682308,603581,601052,851973,757062,
757064,757065,758523,200079,609990,758522,758521,758545,758543,758542,758540,758539,206924,328380,152043,536113,
757061,757062,757060,"022904","087438","098425","005685","071298",
]
bond200 = [
562713,"033095",916993,940213,439714,920724,121809,940272,995054,379976,691703,694050,695615,520950,126336,143872,212244,693912,128945,419932,498420,866617,498422,100709,788883,609654,894951,941848,961983,454251,948352,767130,767133,230972,211701,767131,
           ]
bond100 = [
    146045,536040,536041,536046,542011,542049,542050,872255,872256,872257,
           ]

today = dt.date.today()
yesterday = today - dt.timedelta(1)
timenow  = dt.time()
print("date =" , today , "time = ", timenow , "yesterday = ", yesterday)


def get100():
    price= "Rs. 100/-"
    el = driver.find_element_by_xpath("//select[@id='PageContent_ddPB']")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == price:
            option.click()
    for i in bond100:
        print(i)
        driver.find_element_by_xpath("//input[@id='txtNumber']").send_keys(i)
        driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div/a").click()
    driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div[3]/div/div/a[3]").click()
    result = driver.find_element_by_xpath("//div[@id='result']")
    print(result, 'home page test successful')

def get200():
    price= "Rs. 200/-"
    el = driver.find_element_by_xpath("//select[@id='PageContent_ddPB']")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == price:
            option.click()
    for i in bond200:
        print(i)
        driver.find_element_by_xpath("//input[@id='txtNumber']").send_keys(i)
        driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div/a").click()
    driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div[3]/div/div/a[3]").click()
    result = driver.find_element_by_xpath("//div[@id='result']")
    print(result, 'home page test successful')

def get750():
    price= "Rs. 750/-"
    el = driver.find_element_by_xpath("//select[@id='PageContent_ddPB']")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == price:
            option.click()
    for i in bond200:
        print(i)
        driver.find_element_by_xpath("//input[@id='txtNumber']").send_keys(i)
        driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div/a").click()
    driver.find_element_by_xpath("//main[@id='main']/div/div[6]/div[2]/div[3]/div/div/a[3]").click()
    result = driver.find_element_by_xpath("//div[@id='result']")
    print(result, 'home page test successful')


try:
    print('Starting automated test...')
    driver.get(url)
    get100()
    time.sleep(30)
    get200()
    time.sleep(30)
    get750()
    time.sleep(30)
    driver.quit()
    driver.close()
    
except Exception as e:
    print(e.message)
    print("test failed")


e_date = dt.datetime.now().strftime("%Y-%m-%d")
s_date = dt.date.today() - dt.timedelta(1)
str_date = s_date.strftime("%Y-%m-%d")
s_time  = dt.time().strftime("T%H:%M:%S")
print("date =" , s_date , "time = ", s_time)


e_time = "T23:59:00.000Z"
start_date = str_date + s_time
end_date = e_date + e_time

print (start_date)
print (end_date)
