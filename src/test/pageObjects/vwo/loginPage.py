from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

        #PageLocators
    username = (By.ID,"login-username")
    password = (By.NAME,"password")
    submit_button = (By.XPATH,"//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR,"#js-notification-box-msg")

    def get_usename(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trial)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()

        except Exception as e:
            print(e)
