from selenium import webdriver
from urllib.request import urlopen, HTTPError

driver = webdriver.Chrome()

driver.implicitly_wait(10)

print('Photo download test run start')

try:
    driver.get('https://www.instagram.com/tomcruise/')
    url = driver.find_element_by_xpath(
        '//div[@id="react-root"]/section/main/div/header/div/div/span/img').get_attribute('src')
    img = urlopen(url).read()
    open("tom.jpg", "wb").write(img)

except HTTPError:
    print('HTTP Error, image not found')


driver.close()
driver.quit()

print('test run successful')
