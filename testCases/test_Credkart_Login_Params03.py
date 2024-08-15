import pytest

from pageObjects.Login_Page import Login_Class
from utilities.Logger import Logging_Class
from utilities import XLUTILIES


class Test_CredKart_Login_Params:

    log = Logging_Class.log_generator()
    path = ".\\Test_Data\\UserLogin.xlsx"

    @pytest.mark.regression
    def test_CredKart_url_Params_003(self, setup, getDataForLogin):
        self.log.info("Testcase test_CredKart_url_Params_003 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Click On login Link")
        self.lg.Login_Link()
        self.log.info("Enter Email" + getDataForLogin[0])
        self.lg.Enter_Email(getDataForLogin[0])
        self.log.info("Enter Password" + getDataForLogin[1])
        self.lg.Enter_Password(getDataForLogin[1])
        self.log.info("Click Login Button")
        self.lg.Click_Login_Button()
        self.log.info("Verify Login Stauts")
        if  getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
            self.lg.Click_Menu_Button()
            self.lg.Click_Logout_Button()
            assert True
        elif getDataForLogin[2] == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
            assert False
        elif getDataForLogin[2] == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
            self.lg.Click_Menu_Button()
            self.lg.Click_Logout_Button()
            assert False
        elif getDataForLogin[2] == "Login_Fail" and self.lg.Verify_Login_Status() == "Fail":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
            assert True
            self.log.info("Testcase test_user_login_002 is Completed\n")


