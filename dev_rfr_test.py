from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymsteams

# for local PC (comment below code before git commit)
driver = webdriver.Chrome()

# for jenkins server (uncomment below code before git commit)
# chrome_driver = "/home/kafkaadmin/chromedriver"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=chrome_driver,
#                           chrome_options=chrome_options)

# initialize the driver
driver.implicitly_wait(10)

# webhook for Teams Channel Alerts
webHook = "https://tridentnc.webhook.office.com/webhookb2/3372124a-8362-4b31-b2d6-a87bd2a7acdc@ad77ac5c-0feb-494c-b00e-914b8b35ec53/IncomingWebhook/ebc8d91c34aa461299c58b405afdac36/ee9effc6-2f09-45ff-8020-aab9e6b3d8ad"

# Variables for Site Test

url = 'https://dev.rockyforkranchresort.com/'
# title = "Rocky Fork Ranch Resort – A Private RV Campground and Resort in Kimbolton, OH"
title = "title to fail test"
xpath = "/html/body/div[1]/div/section[1]/div[2]/div[1]/div/div[1]/div/h1"
# h_text = "Welcome to Rocky Fork Ranch Resort"
h_text = "Heading to fail test"
links = []
report = []


# send report to teams channel.

def send_report():
    if len(report) != 0:
        myTeamsMessage = pymsteams.connectorcard(webHook)
        myTeamsMessage.title("Please ignore this test alert , dev test has these errors / broken links")
        myTeamsMessage.text(str(report))
        myTeamsMessage.send()

    else:
        # myTeamsMessage = pymsteams.connectorcard(webHook)
        # myTeamsMessage.title("dev test has No errors test compeleted successfully")
        # myTeamsMessage.send()
        print("No errors test compeleted successfully")


def test_subpages():
    print("Subpage test start")
    for i in links:
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
            report.append({"text": t, "title": title,
                           "link": l, "status": "failed"})
    # report all failed pages and buttons
    send_report()


def get_all_subpages():
    print('getting list of all subpages')
    aTags = driver.find_elements_by_tag_name("a")
    print('total aTags =', len(aTags))
    for i in aTags:
        text = i.text.lower().strip()
        if len(text) > 1 and text.isspace() == False and text != "click here":
            link = i.get_attribute('href')
            if url in link and link != url:
                links.append({"text": text, "link": link})
    print('total links =', len(links))
    test_subpages()


try:
    print('Starting automated test...')
    driver.get(url)
    t_title = driver.title
    if t_title.lower() != title.lower():
        report.append({"text": title, "title": t_title,
                        "link": url, "status": "failed"})
    assert t_title.lower() == title.lower(), "Home Page title test failed."
    heading = driver.find_element_by_xpath(xpath).text
    print(heading)
    if heading.lower() != h_text.lower():
        report.append({"text": heading, "title": driver.title,
                       "link": url, "status": "failed"})
    assert heading.lower() == h_text.lower(), "Home Page Heading test failed."
    print('home page test successful')
    get_all_subpages()
    # close and quit browser once done
    driver.close()
    driver.quit()
    print('Test completed')


except Exception as e:
    print(e)
    driver.close()
    driver.quit()
    send_report()
    print("test failed")
