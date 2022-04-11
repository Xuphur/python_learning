from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymsteams
from datetime import datetime

# for local PC comment below code before git commit
driver = webdriver.Chrome()
 
# for jenkins server uncomment below code before git commit
# chrome_driver = "/home/kafkaadmin/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=chrome_driver,
#                           chrome_options=chrome_options)

# initialize the driver
driver.implicitly_wait(10)
url = 'https://travelresorts.com/'
webHook = "https://outlook.office.com/webhook/3372124a-8362-4b31-b2d6-a87bd2a7acdc@ad77ac5c-0feb-494c-b00e-914b8b35ec53/JenkinsCI/632a7fa701bc45d9992fd126b0212484/6a9d9c54-af28-4e82-806c-8179e665e665"
links = []
sublinks = []
report = []

# send report to teams channel.


def send_report():
    if len(report) > 0:
        print(report)
        myTeamsMessage = pymsteams.connectorcard(webHook)
        myTeamsMessage.text(
            "Travelresorts.com has these error / broken links", report)
        myTeamsMessage.send()

    else:
        print("No errors test compeleted successfully")


def test_linkpages():
    print("Total links on subPage", len(sublinks))
    for index, i in enumerate(sublinks):
        print("test subLink # = ", index)
        l = i["link"]
        t = i["text"].split(" ")
        driver.get(l)
        title = driver.title.lower()
        result = []
        for i in t:
            r = i in title
            result.append(r)
        if "True" in result != True:
            print("partial match not found")
            report.append({"btn_text": t, "page_title": title,
                           "page_url": l, "status": "failed"})
    # report all failed pages and buttons
    # send_report() # un-comment this before git commit
    # delete or comment below code before git commit
    if len(report) > 0:
        print(report)


def get_linkpages():
    sublinks.clear()
    aTags = driver.find_elements_by_tag_name("a")
    print('total aTags on subpage =', len(aTags))
    for i in aTags:
        text = i.text.lower().strip()
        if len(text) > 1 and text.isspace() == False and text != "click here":
            link = i.get_attribute('href')
            if url in link and link != url:
                sublinks.append({"text": text, "link": link})
    test_linkpages()


def test_subpages():
    print("Total main links", len(links))
    for index, i in enumerate(links):
        print("test mainLink # = ", index)
        l = i["link"]
        t = i["text"].split(" ")
        driver.get(l)
        title = driver.title.lower()
        result = []
        for i in t:
            r = i in title
            result.append(r)
        if "True" in result != True:
            print("partial match not found")
            report.append({"btn_text": t, "page_title": title,
                           "page_url": l, "status": "failed"})
        # report all failed pages and buttons
        get_linkpages()


def get_subpages():
    aTags = driver.find_elements_by_tag_name("a")
    print('total aTags =', len(aTags))
    for i in aTags:
        text = i.text.lower().strip()
        if len(text) > 1 and text.isspace() == False and text != "click here":
            link = i.get_attribute('href')
            if url in link and link != url:
                links.append({"text": text, "link": link})
    test_subpages()


try:
    start_time = datetime.now().replace(microsecond=0)
    print('Starting automated test at =', start_time)
    driver.get(url)
    heading = driver.find_element_by_xpath(
        "//div[@id='et-boc']/div/div/div/div/div/main/div/div/div[2]/div/div/div[2]/div/h1").text
    print(heading)
    t = "Discover A Vacation That'S More Than Just A View"
    if heading.lower() != t.lower():
        report.append({"btn_text": heading, "page_title": driver.title,
                       "page_url": url, "status": "failed"})
    assert heading.lower() == t.lower(), "Home Page Heading test failed."
    print('home page test successful')
    print('link test start')
    get_subpages()
    end_time = datetime.now().replace(microsecond=0)
    print('test successfully completed at = ', end_time)
    ETA = end_time - start_time
    print("total test time = ", ETA)


except Exception as e:
    print(e)
    print("test failed")


# close and quite browser once done
driver.close()
driver.quit()
print('Test completed')
