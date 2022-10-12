from selenium.webdriver.common.by import By


class RegisterPage:
    link_myAccount_xpath = '//*[@id="top-links"]/ul/li[2]/a'
    link_register_xpath = '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'
    textbox_firstname_id = 'input-firstname'
    textbox_lastname_id = 'input-lastname'
    textbox_email_id = 'input-email'
    textbox_telephone_id = 'input-telephone'
    textbox_password_id = 'input-password'
    textbox_passwordConfirm_id = 'input-confirm'
    checkbox_privacyPolicy_name = 'agree'

    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.link_myAccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.link_register_xpath).click()

    def setFirstName(self, username):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(username)

    def setLastName(self, username):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(username)

    def setEmail(self, username):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(username)

    def setTelephone(self, username):
        self.driver.find_element(By.ID, self.textbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def setPasswordConfirm(self, password):
        self.driver.find_element(By.ID, self.textbox_passwordConfirm_id).clear()
        self.driver.find_element(By.ID, self.textbox_passwordConfirm_id).send_keys(password)

    def clickPrivacyPolicy(self):
        self.driver.find_element(By.NAME, self.checkbox_privacyPolicy_name).click()
