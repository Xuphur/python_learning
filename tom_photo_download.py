from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen, HTTPError

driver = webdriver.Chrome()

driver.implicitly_wait(10)

print("Photo download test run start")

try:
    driver.get("https://www.instagram.com/tomcruise/")
    # url = driver.find_element(
    #     By.XPATH,
    #     '//div[@id="mount_0_0_ZM"]/div/div/div/div/div/div/div/div/section/main/div/header/div/div/span/img',
    # ).get_attribute("src")
    url = driver.find_element(By.CLASS_NAME, "_aa8j").get_attribute("src")
    img = urlopen(url).read()
    open("tom.jpg", "wb").write(img)

except HTTPError:
    print("HTTP Error, image not found")


driver.close()
driver.quit()

print("test run successful")
