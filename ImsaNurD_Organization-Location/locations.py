import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from element import elem
from data import addData

# Test Case Menu Admin - Organization - Locations


class TestAOL(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # variable data
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def tearDown(self):
        self.browser.quit()

    # OHMR28 - Add location successfully
    def add_location_successully(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR29 - Add location failed (Blank all field)
    def add_location_failed_blank_all_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')


    # OHMR30 - Add location failed (Blank name field)
    def add_location_failed_blank_name_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')


    # OHMR31 - Add location failed (Blank city field)
    def add_location_failed_blank_city_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba1")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR32 - Add location failed (Blank state field)
    def add_location_failed_blank_state_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba2")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR33 - Add location failed (Blank post code field)
    def add_location_failed_blank_pcode_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba3")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR34 - Add location failed (Blank country field)
    def add_location_failed_blank_country_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')


    # OHMR35 - Add location failed (Blank phone field)
    def add_location_failed_blank_phone_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba4")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR36 - Add location failed (Invalid phone (input letter))
    def add_location_failed_due_to_invalid_phone(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        # Input string
        driver.find_element(By.XPATH, elem.phone).send_keys("098765ab@#$")
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')


    # OHMR37 - Add location failed (Blank fax field)
    def add_location_failed_blank_fax_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba5")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR38 - Add location failed (Invalid fax (input letter))
    def add_location_failed_due_to_invalid_fax(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        # Input string
        driver.find_element(By.XPATH, elem.fax).send_keys("1234abcd@#$")
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/h6[1]").text
        self.assertIn(response_data, 'Add Location')


    # OHMR39 - Add location failed (Blank address field)
    def add_location_failed_blank_address_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba6")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR40 - Add location failed (Blank notes field)
    def add_location_failed_blank_notes_fields(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys("coba7")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR41 - Cancel add location
    def cancel_add_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.nameAdd).send_keys(addData.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(addData.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(addData.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(addData.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(addData.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(addData.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(addData.fax)
        time.sleep(1)
        
        # dropdown country
        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)
        
        driver.find_element(By.XPATH, elem.notes).send_keys(addData.notes)
        # Button Cancel
        driver.find_element(
            By.XPATH, elem.btnCancel).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR42 - Search location by valid name
    def search_location_successfully_by_name(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, '(1) Record Found')


    # OHMR43 - Search location by valid city
    def search_location_successfully_by_city(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.cityLoc).send_keys(addData.city)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, '(1) Record Found')


    # OHMR44 - Search location by invalid name
    def search_location_failed_due_to_invalid_name(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys("new zeland")
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, 'No Records Found')


    # OHMR45 - Search location by invalid city
    def search_location_failed_due_to_invalid_city(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.cityLoc).send_keys("Ngawi")
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, 'No Records Found')


    # OHMR46 - Edit location successully
    def edit_location_successfully(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Edit
        driver.find_element(By.XPATH, elem.btnEdit).click()
        time.sleep(3)
        # Edit Data
        cityEdit = driver.find_element(By.XPATH, elem.cityEdit)
        cityEdit.send_keys(Keys.CONTROL + "a")
        cityEdit.send_keys(Keys.BACKSPACE)
        cityEdit.send_keys("Surabaya")
        time.sleep(2)
        addressEdit = driver.find_element(By.XPATH, elem.addressEdit)
        addressEdit.send_keys(Keys.CONTROL + "a")
        addressEdit.send_keys(Keys.BACKSPACE)
        addressEdit.send_keys("Surabaya, Jawa Timur")
        time.sleep(2)
        stateEdit = driver.find_element(By.XPATH, elem.stateEdit)
        stateEdit.send_keys(Keys.CONTROL + "a")
        stateEdit.send_keys(Keys.BACKSPACE)
        stateEdit.send_keys("Jawa Timur")
        time.sleep(2)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSaveEdit).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR47 - Cancel edit location
    def cancel_edit_location(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)

        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Edit
        driver.find_element(By.XPATH, elem.btnEdit).click()
        time.sleep(5)
        # Button Cancel
        driver.find_element(By.XPATH, elem.btnCancel).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')


    # OHMR48 - Delete location successully
    def delete_location_successfully(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(addData.name)
        time.sleep(1)
        # Button Search
        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)
        # Button Delete
        driver.find_element(By.XPATH, elem.btnDelete).click()
        time.sleep(5)
        # konfirmasi delete
        driver.find_element(By.XPATH, elem.confirmDelete).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')



if __name__ == "__main__":
    unittest.main()
