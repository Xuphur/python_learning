from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymsteams

import smtplib
from email import encoders
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart

# for local PC comment below code before git commit
# driver = webdriver.Chrome()

# for jenkins server uncomment below code before git commit

chrome_driver = "/home/kafkaadmin/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=chrome_driver,
                          chrome_options=chrome_options)

# initialize the driver
driver.implicitly_wait(10)


url = 'https://travelresorts.com/'
links = []
report = []


def get_all_subpages():
    aTags = driver.find_elements_by_tag_name("a")
    print('total aTags =', len(aTags))
    for i in aTags:
        text = i.text.lower().strip()
        if len(text) > 1 and text.isspace() == False and text != "click here":
            link = i.get_attribute('href')
            if url in link and link != url:
                links.append({"text": text, "link": link})
    test_subpages()


def test_subpages():
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
    if len(report) > 0:
        print(report)

        myTeamsMessage = pymsteams.connectorcard(
            "https://outlook.office.com/webhook/3372124a-8362-4b31-b2d6-a87bd2a7acdc@ad77ac5c-0feb-494c-b00e-914b8b35ec53/JenkinsCI/eb9ff08ec7fa4b089bdb564aa3e04849/6a9d9c54-af28-4e82-806c-8179e665e665")
        myTeamsMessage.text(
            "Travelresorts.com has these error / broken links")
        myTeamsMessage.send()

        toaddr = [
            'msayyam@travelresorts.com'
        ]
        cc = [
            'znaqeeb@travelresorts.com',
            # 'adeelahmed@travelresorts.com'
        ]
        # Sending an email via script.
        fromaddr = "trareporting@travelresorts.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ','.join(toaddr)
        msg['Cc'] = ','.join(cc)
        msg['Subject'] = 'Web Site Test Alert'
    else:
        myTeamsMessage = pymsteams.connectorcard(
            "https://outlook.office.com/webhook/3372124a-8362-4b31-b2d6-a87bd2a7acdc@ad77ac5c-0feb-494c-b00e-914b8b35ec53/JenkinsCI/eb9ff08ec7fa4b089bdb564aa3e04849/6a9d9c54-af28-4e82-806c-8179e665e665")
        myTeamsMessage.text(
            "Report: travelresorts.com has No errors test compeleted successfully")
        myTeamsMessage.send()
        print("No errors test compeleted successfully")


try:
    print('Starting automated test...')
    driver.get(url)
    heading = driver.find_element_by_xpath(
        "//div[@id='et-boc']/div/div/div/div/div/main/div/div/div[2]/div/div/div[2]/div/h1").text
    print(heading)
    result = heading == "Discover A Vacation That'S More Than Just A View"
    if result == False:
        report.append({"text": heading, "title": driver.title,
                       "link": url, "status": "failed"})
    assert heading == "Discover A Vacation That'S More Than Just A View"
    print('home page test successful')
    print('link test start')
    get_all_subpages()


except Exception as e:
    print(e)
    print("test failed")


# close and quite browser once done
driver.close()
driver.quit()
print('Test completed')
