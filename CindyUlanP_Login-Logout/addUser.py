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
    #OHRM
    def test_a_adduser_success(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(5)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click field employee name
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(5)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.userManage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(10)

        # validasi
        response_url = driver.current_url
        self.assertEqual(response_url,url.addUrl)
    
    def test_b_failed_usnexist(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click filed employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.userManage)#input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.exsUser).text
        self.assertIn(input.existUser, response_data)
    
    def test_c_failed_blankall(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.blankField).text
        self.assertIn(input.reqMana, response_data)

    def test_d_failed_blankselect(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click field employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.usnmanage) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.blankField).text
        self.assertIn(input.reqMana, response_data)

    def test_e_failed_blankemploye(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.usnmanage_1) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.blankEmploye).text
        self.assertIn(input.reqMana, response_data)

    def test_f_failed_blankusername(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click field employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)
        
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.blankUsername).text
        self.assertIn(input.reqMana, response_data)   
    
    def test_g_failed_blankpassword(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click field employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)
        
        driver.find_element(By.XPATH, elem.userMana).send_keys(input.usnmanage_2) #input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        #validasi
        response_data = driver.find_element(By.XPATH,elem.blankPassword).text
        self.assertIn(input.reqMana, response_data)  

    def test_h_failed_invusername(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click filed employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.invUser)#input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.confirmPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.invalidUser).text
        self.assertIn(input.userInv, response_data)

    def test_i_failed_invpassword(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click filed employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.usnmanage_1)#input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.invPass) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.invPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.invalidPass).text
        self.assertIn(input.passInv, response_data)

    def test_j_failed_invconfpass(self):
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)#login
        time.sleep(5)
        driver.maximize_window()
        driver.find_element(By.XPATH, elem.adminBtn).click() #click button admin
        time.sleep(1)
        driver.find_element(By.XPATH, elem.addBtn).click() #click button +add
        time.sleep(1)

        #dropdown user role
        driver.find_element(By.XPATH, elem.selectUser).click() #click field user role
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRole).click() #click dropdown admin
        time.sleep(1)

        #employee name
        driver.find_element(By.CLASS_NAME, elem.employee).click() #click filed employee
        time.sleep(1)
        driver.find_element(By.XPATH, elem.hintEmployee).send_keys(input.employee) #input employee name
        time.sleep(5)
        driver.find_element(By.XPATH, elem.listbox).click() #click listbox
        time.sleep(1)

        #dropdown status
        driver.find_element(By.XPATH, elem.selectEnable).click() #click field status
        time.sleep(1)
        driver.find_element(By.XPATH, elem.status).click() #click dropdown enable
        time.sleep(1)

        driver.find_element(By.XPATH, elem.userMana).send_keys(input.usnmanage_1)#input username
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passMana).send_keys(input.passMana) #input password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPass).send_keys(input.invPass) #input confirm password
        time.sleep(1)
        driver.find_element(By.XPATH, elem.saveBtn).click() #click button save
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.XPATH,elem.invalidConfpass).text
        self.assertIn(input.confirmInv, response_data)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()