import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from locator import elem
from data import input
import baseLogin

class TestSearchuser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) # type: ignore

    def test_a_searchuser_byname(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input searchname
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button search
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.foundName).text
        self.assertIn(input.foundName, response_data)
    
    def test_b_searchuser_byrole(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        #dropdown user role
        driver.find_element(By.XPATH, elem.searchRole).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.dropdownRole).click() #click dropdown admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button save
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.foundRole).text
        self.assertIn(input.foundRole, response_data)
    
    def test_c_searchuser_invalidname(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.invName) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button save
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.noFound).text
        self.assertIn(input.noRecord, response_data)
    
    def test_d_searchuser_btnreset(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input username
        time.sleep(1)
        #dropdown user role
        driver.find_element(By.XPATH, elem.searchRole).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.dropdownRole).click() #click dropdown admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.resetBtn).click() #click button save
        time.sleep(3)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.reset).text
        self.assertIn(input.reset, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()