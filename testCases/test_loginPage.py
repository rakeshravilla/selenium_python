from selenium import webdriver

from pageObjects.loginPage import LoginPage
from pageObjects.registerPage import RegisterPage


class Test_LoginPage:
    baseURL = 'http://tutorialsninja.com/demo/'
    email = 'khsdhsufh@mail.com'
    password = 'jkhdckhsk'

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = RegisterPage(self.driver)
        self.lp.clickMyAccount()
        self.lp = LoginPage(self.driver)
        self.lp.clickLogin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLoginButton()

        act_title = self.driver.title
        print(f'********title txt {act_title}')
        if act_title == "My Account":
            print("**** Home page title test passed ****")
            # self.driver.close()
            assert True
        else:
            print("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            # self.driver.close()
            assert False
        self.lp.clickLogout()
        self.driver.quit()
