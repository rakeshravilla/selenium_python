from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    link_login_linkText = 'Login'
    textbox_email_name = 'email'
    textbox_password_name = 'password'
    button_login_xpath = '//*[@id="content"]/div/div[2]/div/form/input'
    link_logout_linkText = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linkText).click()

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linkText).click()
