from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_zafar(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name(
            "q").send_keys("Zafar Naqeeb", Keys.ENTER)
        self.driver.close

    def test_search_tra(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name(
            "q").send_keys("Travel Resorts", Keys.ENTER)
        self.driver.close

    @classmethod
    def tearDownClass(cls):
        cls.driver.close
        cls.driver.quit


print("test run successful")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='E:/Python Learning/reports'))
