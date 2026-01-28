from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait

class FreeTrialPage:
    def __init__(self,driver):
        self.driver = driver

    free_trial_link = (By.XPATH,"//a[normalize-space()='Start a free trial']")
    username_email_ft = (By.XPATH,"//input[@id = 'page-v1-step1-email']")
    checkbox_terms = (By.XPATH,"//input[@id = 'page-free-trial-step1-cu-gdpr-consent-checkbox']")
    button_click_ft = (By.XPATH,"//button[normalize-space() = 'Create a Free Trial Account']")
    error_msg_invalid_email = (By.XPATH,"//div[normalize-space()= 'The email address you entered is incorrect.']")
    ALLOW_C0OKIES = (By.XPATH,"//button[contains(text(),'Allow Cookies')]")
    def get_free_trial_link(self):
        return self.driver.find_element(*FreeTrialPage.free_trial_link)

    def get_username_ft(self):
        webdriver_wait(driver = self.driver,element_tuple=self.username_email_ft,)
        return self.driver.find_element(*FreeTrialPage.username_email_ft)

    def get_button_click_ft(self):
        return self.driver.find_element(*FreeTrialPage.button_click_ft)

    def get_button_checkbox_terms(self):
        return self.driver.find_element(*FreeTrialPage.checkbox_terms)

    def get_error_msg_invalid_email(self):
        return self.driver.find_element(*FreeTrialPage.error_msg_invalid_email)

    def get_error_message_text(self):
        webdriver_wait(driver = self.driver,element_tuple = self.error_msg_invalid_email,timeout = 15)
        return self.get_error_msg_invalid_email().text

    def accept_cookies(self):
        try:
            webdriver_wait(self.driver,self.ALLOW_C0OKIES,10).click()
        except Exception as e:
            print(e)

    def enter_free_trial_details_invalid(self,invalid_email):
        try:
            self.accept_cookies()
            self.get_username_ft().send_keys(invalid_email)
            self.get_button_checkbox_terms().click()
            webdriver_wait(driver=self.driver,element_tuple = self.button_click_ft,timeout=5)
            self.get_button_click_ft().click()

        except Exception as e:
            print(e)