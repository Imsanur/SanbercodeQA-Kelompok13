import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from locator import elem
from locator import url
from data import input
import baseLogin

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_logout_success(self):
        # steps
        #login
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)
        #login.test_a_login_success(self)

        #logout
        driver.find_element(By.CLASS_NAME, elem.userProfil).click() #isi email
        time.sleep(1)
        driver.find_element(By.XPATH, elem.logoutMenu).click() # menu Logout
        time.sleep(2)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.loginPage).text
        self.assertIn(input.loginTxt, response_data)


    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()