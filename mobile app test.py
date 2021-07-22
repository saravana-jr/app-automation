from appium import webdriver
import time
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps["platformName"]= "android"
        desired_caps["appActivity"]= "com.atg.world.activity.SplashActivity"
        desired_caps["appWaitDuration"]= "50000"
        desired_caps["appExecTimeout"]= "500000"
        desired_caps["uiautomator2ServerLaunchTimeout"]= "50000"
        desired_caps["uiautomator2ServerInstallTimeout"]= "50000"
        desired_caps["appPackage"]= "com.ATG.World"
        desired_caps["deviceName"]= "emulator-5554"
        desired_caps["driver"]= "http://localhost:4723/wd/hub"
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)



    def test_login(self):
        driver = self.driver
        time.sleep(5)
        st=driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
        time.sleep(2)
        sign=driver.find_element_by_id("com.ATG.World:id/login_email").click()
        time.sleep(2)
        email = driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()
        time.sleep(50)
        print("test_LoginWithRightCredential passed")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    #Construction test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)