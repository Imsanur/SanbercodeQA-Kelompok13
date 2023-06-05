import time
from selenium.webdriver.common.by import By
from locator import elem
from locator import url
from data import input

def positive_login(driver): #OHRM01
    driver.get(url.baseUrl) #buka website
    time.sleep(30)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys(input.username) #input valid username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys(input.password) #input valid password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)

def negative_login_invalid_username(driver): #OHRM02
    driver.get(url.baseUrl) #buka situs
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys(input.invalidUsername) #input invalid username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys(input.password) #input valid password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)

def negative_login_upcase_username(driver):#OHRM03
    driver.get(url.baseUrl) #buka website
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys(input.upcaseUsername) #input invalid username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys(input.password) #input valid password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)

def negative_login_invalid_password(driver):#OHRM04
    driver.get(url.baseUrl) #buka website
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys(input.username) #input valid username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys(input.invalidPassword) #input invalid password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)

def negative_login_empty_username(driver):#OHRM05
    driver.get(url.baseUrl) #buka website
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys("") #input empty username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys(input.password) #input valid password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)

def negative_login_empty_password(driver): #OHRM06
    driver.get(url.baseUrl) #buka website
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys(input.username) #input valid username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys("") #input empty password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click()  #click login
    time.sleep(3)

def negative_login_blank_all(driver):#OHRM07
    driver.get(url.baseUrl) #buka website
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.NAME, elem.name).send_keys("") #input empty username
    time.sleep(1)
    driver.find_element(By.NAME, elem.pwd).send_keys("") #input empty password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginBtn).click() #click login
    time.sleep(3)
