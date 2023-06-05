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

class TestAdduser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install()) # type: ignore
    def test_a_addpim_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.menuAdmin).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addPim).click() #click button +add
        time.sleep(20)
        driver.find_element(By.NAME, elem.fName).send_keys(input.fName) #input username
        time.sleep(5)
        driver.find_element(By.NAME, elem.mName).send_keys(input.nName) #input password
        time.sleep(5)
        driver.find_element(By.NAME, elem.lName).send_keys(input.lName) #input confirm password
        time.sleep(5)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(input.id) #input confirm password
        time.sleep(3)
        driver.find_element(By.XPATH, elem.svBtn).click() #click button save
        time.sleep(20)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.valPim).text
        self.assertIn(input.valAdd, response_data)

    def test_b_addpim_blank1(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.menuAdmin).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addPim).click() #click button +add
        time.sleep(20)
        driver.find_element(By.NAME, elem.fName).send_keys(input.fName) #input username
        time.sleep(5)
        driver.find_element(By.XPATH, elem.svBtn).click() #click button save
        time.sleep(10)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.reqPim1).text
        self.assertIn(input.reqPim, response_data)

    def test_c_addpim_blank2(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.menuAdmin).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addPim).click() #click button +add
        time.sleep(5)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(Keys.BACK_SPACE)
        time.sleep(5)
        driver.find_element(By.XPATH, elem.idEmp).send_keys(input.id) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.svBtn).click() #click button save
        time.sleep(10)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.reqPim2).text
        self.assertIn(input.reqPim, response_data)

    def test_d_addpim_blankall(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.menuAdmin).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addPim).click() #click button +add
        time.sleep(10)
        driver.find_element(By.XPATH, elem.svBtn).click() #click button save
        time.sleep(10)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.reqPim2).text
        self.assertIn(input.reqPim, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()