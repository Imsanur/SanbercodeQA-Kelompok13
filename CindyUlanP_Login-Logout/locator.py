class elem():
    #Login & Logout
    name = "username" #by_xpath
    pwd = "password" #by_name
    required = "oxd-input-group__message" #by_class
    loginBtn = "orangehrm-login-button" #by_class
    invalidCred = "oxd-alert-content-text" #by_class
    dashboardTxt = "oxd-topbar-header" #by_class
    userProfil = "oxd-userdropdown-tab" #by_class
    logoutMenu = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]/ul[1]/li[4]/a[1]"
    loginPage = "orangehrm-login-title" #by_class

    #User Management-Add User
    adminBtn = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]"
    addBtn = "//button[normalize-space()='Add']"
    selectUser = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]" 
    userRole = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/span"
    selectEnable = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]" 
    status = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span"
    employee = "oxd-autocomplete-wrapper" #by_class
    hintEmployee = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input"
    listbox = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span"
    userMana = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/input[1]" 
    passMana = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]" 
    confirmPass ="//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']"
    saveBtn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"
    
    #Invalid/blank Field User
    exsUser = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span"
    blankField = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/span"
    blankEmploye = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/span"
    blankUsername = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span"
    blankPassword = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span"
    invalidUser = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/span"
    invalidPass = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span"
    invalidConfpass = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/span"
    
    #Search User
    searchName = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
    searchEmploye = "oxd-autocomplete-wrapper" #by_class
    hintSerach = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/input"
    listboxSearch = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div/span"
    searchRole = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"
    dropdownRole = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span"
    serachStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]"
    dropdownStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span"
    searchBtn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    foundName = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span" 
    foundEmploye = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
    foundStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
    foundRole = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"
    noFound = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span" 
    reset = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"
    resetBtn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]"
    
    #Edit User
    penBtn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div/button[2]/i"
    editRole = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    dropdownEdit = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/span"
    editStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]"
    dropdownStatus = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[3]/span"
    editBtn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    valEdit = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]/text()"

    #Delete User
    trashBtn ="//i[@class='oxd-icon bi-trash']"
    deleteBtn = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"
    cancelBtn = "//*[@id='app']/div[3]/div/div/div/div[3]/button[1]"

    



class url():
    baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboardUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    logoutUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/logout"
    addUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

