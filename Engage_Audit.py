import datetime as dt
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# for local PC (comment below code before git commit)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# initialize the driver
driver.implicitly_wait(10)

# Variables

url = "https://prospect-booking.apps.travelresorts.com/admin"
username = "znaqeeb@travelresorts.com"
password = "N@q33b"
h2text = "Discover A Vacation That's More Than Just A View"
LitmusTitle = "Travel Resorts Of America"
# LitmusTitle = "Text to fail this test"
links = []
report = []
check_list = []
status = False



def goTo( url ):
    if "error" in [ elem.get_attribute("id") for elem in driver.find_elements_by_css_selector("body > div") ]:
        report.append({"Litmus_text": "Error", "Title": LitmusTitle,
                        "URL": url, "Status": "failed"})
        print ('goTo url failed')
        # send_report()
        raise Exception( "this page is an error" )
    else:
        driver.get( url )

def getIds():
    idList = driver.find_elements_by_class_name("table-responsive")
    print(idList)




try:
    print('Starting automated test...')
    goTo(url)
    btns = driver.find_elements_by_tag_name("button")
    for i in btns:
        text = i.text
        if text == "Login":
            i.click()
        else:
            print("bla bla bla do it again")
    driver.find_element_by_id("i0116").send_keys(username)
    time.sleep(3)
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(3)
    
    driver.find_element_by_id("i0118").send_keys(password)
    time.sleep(3)
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(3)
    driver.find_element_by_id("idSIButton9").click()
    time.sleep(5)
    driver.get( url )
    time.sleep(5)
    el = driver.find_element_by_id("itemsPerPage")
    for option in el.find_elements_by_tag_name('option'):
        if option.text == "50":
            option.click()
    getIds()

except Exception as e:
    print(e)
    # driver.close()
    # driver.quit()
    # send_report()
    print("test failed")