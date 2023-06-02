import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from locator import elem
from locator import url
from data import input
import baseLogin

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #OHRM01
    def test_a_login_success(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboardUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.dashboardTxt).text
        self.assertIn(input.dashboardTxt, response_data)

    #OHRM02
    def test_b_login_invalid_username(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_invalid_username(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.invalidCred).text
        self.assertIn(input.invalidCred, response_data)

    #OHRM03
    def test_c_login_upcase_username(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_upcase_username(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.dashboardUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.dashboardTxt).text
        self.assertIn(input.dashboardTxt, response_data)

    #OHRM04
    def test_d_login_invalid_password(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_invalid_password(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.invalidCred).text
        self.assertIn(input.invalidCred, response_data)

    #OHRM05
    def test_e_login_empty_username(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_empty_username(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(input.required, response_data)

    #OHRM06
    def test_f_login_empty_password(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_empty_password(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(input.required, response_data)
    
    #OHRM07
    def test_g_login_blank_all(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_all(driver)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url, url.baseUrl)
        response_data = driver.find_element(By.CLASS_NAME,elem.required).text
        self.assertIn(input.required, response_data)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()