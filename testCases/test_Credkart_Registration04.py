import pytest

from pageObjects.Login_Page import Login_Class
from pageObjects.Registration_Page import Registration_Class
from utilities.Logger import Logging_Class


class Test_CredKart_Registration:
    log = Logging_Class.log_generator()

    @pytest.mark.sanity
    def test_CredKart_Registration04(self, setup):
        self.log.info("Testcase test_CredKart_Registration04 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.reg = Registration_Class(self.driver)
        self.log.info("Click On Register Link")
        self.reg.Click_Registration_Link()
        self.log.info("Enter Name")
        self.reg.Enter_Name("Credence")
        self.log.info("Enter Email")
        self.reg.Enter_Email("12may2024@gmail.com")
        self.log.info("Enter Password")
        self.reg.Enter_Password("Test@123")
        self.log.info("Enter Confirm Password")
        self.reg.Enter_ConfirmPassword("Test@123")
        self.log.info("Click register button")
        self.reg.Click_Register_Button()
        self.lg = Login_Class(self.driver)
        self.log.info("Verifying the registration stauts")
        if self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_Registration04_pass.PNG")
            self.log.info("Testcase test_CredKart_Registration04 is Pass")
            assert True
        else:
            self.log.info("Testcase test_CredKart_Registration04 is Fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_Registration04_fail.PNG")
            assert False
        self.log.info("Testcase test_CredKart_Registration04 is comepleted")
