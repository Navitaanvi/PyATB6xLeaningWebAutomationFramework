"""
Dashboard Page Class
Page Locators
Page Actions
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from src.test.utils.common_utils import webdriver_wait


class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    user_logged_in = (By.XPATH, "//h6[normalize-space()='Tempumail']")
    user_logged_in_user_ID = (By.XPATH, "(//span[normalize-space()='#1188580'])[1]")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.user_logged_in,timeout = 15)
        return self.get_user_logged_in().text
