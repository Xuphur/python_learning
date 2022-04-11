from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pymsteams
import pandas as pd

# for local PC (comment below code before git commit)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)

# for jenkins server (uncomment below code before git commit)
# chrome_driver = "/home/kafkaadmin/chromedriver"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=chrome_driver,
#                           chrome_options=chrome_options)

# initialize the driver
driver.implicitly_wait(10)

# Web hook for MsTeam Alerts
webHook = "https://tridentnc.webhook.office.com/webhookb2/3372124a-8362-4b31-b2d6-a87bd2a7acdc@ad77ac5c-0feb-494c-b00e-914b8b35ec53/IncomingWebhook/ebc8d91c34aa461299c58b405afdac36/ee9effc6-2f09-45ff-8020-aab9e6b3d8ad"


# Variables

url = "https://www.travelresorts.com/"
xpath = "//div[@data-id='580d0771']/div/h2"
h_text = "Discover A Vacation That's More Than Just A View"
title = "Travel Resorts Of America"
links = []
report = []
check_list = []

# send report to teams channel.

def send_report():
    if len(report) > 0:
        print(report)
        myTeamsMessage = pymsteams.connectorcard(webHook)
        myTeamsMessage.title("Travel Resorts of America has these errors / broken links")
        # myTeamsMessage.text(str(report))
        reportDF = pd.DataFrame(check_list)
        myTeamsMessage.text(reportDF.to_html())
        myTeamsMessage.send()
    else:
        myTeamsMessage = pymsteams.connectorcard(webHook)
        myTeamsMessage.title("Test Alert - Please Ignore")
        reportDF = pd.DataFrame(check_list)
        myTeamsMessage.text(reportDF.to_html())
        myTeamsMessage.send()
        # myTeamsMessage.send()
        print("No errors test compeleted successfully")


def removeDuplicates(links):
    for x in links:
        if x not in check_list:
            check_list.append(x)
    return check_list



def goTo( url ):
    if "errorPageContainer" in [ elem.get_attribute("id") for elem in driver.find_elements_by_css_selector("body > div") ]:
        report.append({"Btn-Text": "Error", "title": title,
                        "link": url, "status": "failed"})
        raise Exception( "this page is an error" )
    else:
        driver.get( url )

def test_subpages():
    for i in check_list:
        print('link test start for', i["link"])
        subPageUrl = i["link"]
        goTo(subPageUrl)
    # report all failed pages and buttons
    send_report()

def get_all_subpages():
    aTags = driver.find_elements_by_tag_name("a")
    print('total aTags =', len(aTags))
    for i in aTags:
      text = str(i.get_attribute('innerText')).lower().strip()
      link = i.get_attribute('href')
      if len(text) > 1 and text.isspace() == False and url in link and link != url and '#' not in link and '.jpeg' not in link:
        links.append({"Btn-Text": text, "link": link})
    removeDuplicates(links)
    # [test_links.append(x) for x in links if x not in test_links]
    print('total links =', len(links))
    print('total check list', len(check_list))
    # print('link for test', check_list)
    test_subpages()


try:
    print('Starting automated test...')
    goTo(url)
    t_title = driver.title
    x = t_title.find(title)
    print(x)
    if x != -1 :
        print ('title match found')
        heading = driver.find_element_by_xpath(xpath).text
        print(heading)
        y = heading.find(h_text)
        if y != -1 :
          print(y)
          print('home page test successful')
          get_all_subpages()
        else:
            report.append({"Btn-Text": heading, "title": t_title,
            "link": url, "status": "failed"})
    else:
        print('title match not found')
        report.append({"Btn-Text": title, "title": t_title,
                        "link": url, "status": "failed"})
    driver.close()
    driver.quit()
    print('Test completed')


except Exception as e:
    print(e)
    driver.close()
    driver.quit()
    send_report()
    print("test failed")
