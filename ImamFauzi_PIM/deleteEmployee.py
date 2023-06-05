import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from locator import elem
from dataPim import addData

class TestDeleteEmployee(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # variable data
        self.url = "https://opensource-demo.orangehrmlive.com"

    def tearDown(self):
        self.browser.quit()
        #Delete Employee 
    def test_delete(self):
        #step
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_locator(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_locator(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_locator(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_locatort(By.XPATH, elem.menuPIM).click()
        time.sleep(2)
        driver.find_locator(By.XPATH, elem.nameEmployee).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_locator(By.XPATH, elem.btnSearchk).click()
        time.sleep(5)
        # Button Delete
        driver.find_locator(By.XPATH,"//i[contains(@class,'oxd-icon bi-trash')]").click()
        time.sleep(3)
        # Konfirmasi Delete
        driver.find_locator(By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
        time.sleep(3)

        #validasi
        response_data = driver.find_locator(
            By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").text
        self.assertIn(response_data, 'Employee List')        


if __name__ == "__main__":
    unittest.main()