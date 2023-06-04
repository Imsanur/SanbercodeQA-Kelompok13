import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from locator import elem
from data import input
import baseLogin

class TestDeleteuser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) # type: ignore
    def test_a_canceldelete_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button search
        time.sleep(10)
        driver.find_element(By.XPATH, elem.trashBtn).click() #click icon button trash
        time.sleep(1)
        driver.find_element(By.XPATH, elem.cancelBtn).click() #click button cancel
        time.sleep(10)  

        #validasi
        response_data = driver.find_element(By.XPATH,elem.valEdit).text
        self.assertIn(input.valEdit, response_data)

    def test_b_delete_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button search
        time.sleep(10)
        driver.find_element(By.XPATH, elem.trashBtn).click() #click icon button trash
        time.sleep(1)
        driver.find_element(By.XPATH, elem.deleteBtn).click() #click button delete
        time.sleep(10)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.valEdit).text
        self.assertIn(input.valEdit, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()  