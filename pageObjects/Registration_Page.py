from selenium.webdriver.common.by import By


class Registration_Class:
    Registration_Link_XPATH = (By.XPATH, "//a[normalize-space()='Register']")
    Text_Name_XPATH = (By.XPATH, "//input[@id='name']")
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_ID = (By.ID, "password-confirm")
    Click_Register_Button_XPATH = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def Click_Registration_Link(self):
        self.driver.find_element(*Registration_Class.Registration_Link_XPATH).click()

    def Enter_Name(self, name):
        self.driver.find_element(*Registration_Class.Text_Name_XPATH).send_keys(name)

    def Enter_Email(self, email):
        self.driver.find_element(*Registration_Class.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Registration_Class.Text_Password_ID).send_keys(password)

    def Enter_ConfirmPassword(self, confirm_password):
        self.driver.find_element(*Registration_Class.Text_ConfirmPassword_ID).send_keys(confirm_password)

    def Click_Register_Button(self):
        self.driver.find_element(*Registration_Class.Click_Register_Button_XPATH).click()
