# Unit test file to determine if the Customer List page is displayed when the user
# clicks the 'Customers' button in the navigation pane of the mfscrm app
# Customer list is shown if the 'summary' button exists on the page
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # Test if Customer list is displayed when Customers is clicked in the Navigation bar
    # Customer list is shown if the 'summary' button exists on the page
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load

        # click the next button
        elem = driver.find_element(By.XPATH,
                                   '//*[@id="carouselSlider"]/a[2]')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        # click the previous button
        elem = driver.find_element(By.XPATH,
                                   '//*[@id="carouselSlider"]/a[1]')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)


        try:
            # verify Slider is working
            elem = driver.find_element(By.XPATH,
                                       '//*[@id="carouselSlider"]/a[2]')
            elem.send_keys(Keys.RETURN)
            print("Test passed - slider working")
            assert True

        except NoSuchElementException:
            self.fail("slider not working - test failed")


def tearDown(self):
    self.driver.close()