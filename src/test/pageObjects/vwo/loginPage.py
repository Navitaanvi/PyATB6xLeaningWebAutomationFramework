from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait

class LoginPage:
    def __init__(self, driver):
        self.driver = driver  # it will get the driver and set the driver

    # PageLocators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    free_trial = (By.XPATH, "//a[contains(text(),'Start a free trial')]")

    # Page Actions

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_free_trial_button(self):
        return self.driver.find_element(*LoginPage.free_trial)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self, usr, pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_submit_button().click()

        except Exception as e:
            print(e)

    def get_error_msg_as_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_message, timeout=5)
        return self.get_error_message().text


    def free_trial_button_click(self):
        try:
            self.get_free_trial_button().click()
        except Exception as e:
            print(e)
