from selenium.webdriver.common.by import By


class Login_Class:
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    Verify_Login_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")
    Login_Link_XPATH = (By.XPATH, "//a[normalize-space()='Login']")
    Menu_Button_XPATH = (By.XPATH, "//a[@role='button']")
    Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(*Login_Class.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*Login_Class.Text_Password_ID).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*Login_Class.Click_Login_Button_XPATH).click()

    def Verify_Login_Status(self):
        try:
            self.driver.find_element(*Login_Class.Verify_Login_XPATH)
            return "Pass"
        except:
            return "Fail"

    def Login_Link(self):
        self.driver.find_element(*Login_Class.Login_Link_XPATH).click()

    def Click_Menu_Button(self):
        self.driver.find_element(*Login_Class.Menu_Button_XPATH).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login_Class.Logout_Button_XPATH).click()
