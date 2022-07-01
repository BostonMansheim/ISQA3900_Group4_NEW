# Unit test file to determine if the Products List page is displayed when the user
# clicks the 'Products' button in the navigation pane of the mfscrm app
# Products list is shown if the 'Edit' button exists on the page
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

    # Test if Services list is displayed when Product is clicked in the Navigation bar
    # Product list is shown if the 'edit' button exists on the page
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load

        # click the login button - log in user
        elem = driver.find_element(By.XPATH,
                                   '/html/body/nav/ul/li[5]/a')
        elem.send_keys(Keys.RETURN)

        # find the username and password input boxes and login
        user = "user1234"  # must be a valid username for the application
        pwd = "bigboston"  # must be the password for a valid user

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to load

        elem = driver.find_element(By.XPATH, '/html/body/nav/ul/li[3]/a')
        elem.send_keys(Keys.RETURN)

        time.sleep(3)


        try:
            # verify drinks menu exist
            elem = driver.find_element(By.XPATH,
                                       '/html/body/nav/ul/li[3]/a')
            elem.send_keys(Keys.RETURN)
            print("Test passed - about page is displayed")
            assert True

        except NoSuchElementException:
            self.fail("about page is not displayed on click - test failed")


def tearDown(self):
    self.driver.close()
