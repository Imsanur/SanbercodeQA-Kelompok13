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

class TestEdituser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) # type: ignore
    def test_a_editrole_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button search
        time.sleep(1)
        driver.find_element(By.XPATH, elem.penBtn).click() #click icon button pen
        time.sleep(3)

        #dropdown user role
        driver.find_element(By.XPATH, elem.editRole).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.dropdownEdit).click() #click dropdown admin
        time.sleep(3)
        driver.find_element(By.XPATH, elem.editBtn).click() #click button edit
        time.sleep(30)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.valEdit).text
        self.assertIn(input.valEdit, response_data)


    def test_b_editstatus_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchName).send_keys(input.userManage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.searchBtn).click() #click button search
        time.sleep(1)
        driver.find_element(By.XPATH, elem.penBtn).click() #click icon button pen
        time.sleep(3)

        # dropdown user status
        driver.find_element(By.XPATH, elem.editStatus).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.dropdownStatus).click() #click dropdown Enable
        time.sleep(3)
        driver.find_element(By.XPATH, elem.editBtn).click() #click button edit
        time.sleep(1)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.valEdit).text
        self.assertIn(input.valEdit, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()