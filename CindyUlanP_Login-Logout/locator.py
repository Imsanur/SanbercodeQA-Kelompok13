class elem():
    username = "username" #by_name
    password = "password" #by_name
    required = "oxd-input-group__message" #by_class
    loginBtn = "orangehrm-login-button" #by_class
    invalidCred = "oxd-alert-content-text" #by_class
    dashboardTxt = "oxd-topbar-header-breadcrumb-module" #by_class
    userProfil = "oxd-userdropdown-tab" #by_class
    logoutMenu = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]/ul[1]/li[4]/a[1]" #by_xpath

    loginPage = "orangehrm-login-title" #by_class

class url():
    baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboardUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    logoutUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/logout"
