from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# for local PC comment below code before git commit 
# driver = webdriver.Chrome()

# for jenkins server uncomment below code before git commit

chrome_driver = "/home/kafkaadmin/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=chrome_driver,
                          chrome_options=chrome_options)


driver.implicitly_wait(10)

# initialize the driver


try:
    print('Starting automated test...')
    driver.get('https://travelresorts.com/')
    heading = driver.find_element_by_xpath(
        "//div[@id='et-boc']/div/div/div/div/div/main/div/div/div[2]/div/div/div[2]/div/h1").text
    print(heading)
    assert heading == "Discover A Vacation That'S More Than Just A View"
    aTags = driver.find_elements_by_tag_name("a")
    links = []
    for i in aTags:
        link = i.get_attribute('href')
        if "https" in link and link.endswith("/"):
            links.append(link)
    links = list(dict.fromkeys(links))
    print('list of links created total links =',  len(links))
    print('home page test successful')
except Exception as e:
    print(e.message)
    print("test failed")

# test linked pages 1 by 1


def test_link(listToStr):
    try:
        driver.get(listToStr)
        print(next_value, driver.title)
        text = listToStr.replace(
            'https://travelresorts.com/', '').replace('/', ' ').replace('-', ' ')
        title = driver.title
        result = text.lower() in title.lower()
        print(text.lower(), title.lower(), result)
        assert result == True
    except Exception as e:
        print(e.message)


for i in range(0, len(links)):
    try:
        next_value = i+1
        if next_value > len(links):
            next_value = len(links) + 1
        link_chunk = links[i:next_value]
        listToStr = ' '.join([str(elem) for elem in link_chunk])
        test_link(listToStr)
    except Exception as e:
        print(e.message)


# close and quite browser once done
driver.close()
driver.quit()
print('Test completed successfully')
