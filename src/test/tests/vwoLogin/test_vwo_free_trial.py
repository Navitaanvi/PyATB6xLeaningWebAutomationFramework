'''
Assertions and ose the page object model
webdriver start
user interaction+assertions
close webdriver
'''
import allure
import pytest
import time

from dotenv import load_dotenv
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjects.vwo.loginPage import LoginPage
from src.test.pageObjects.vwo.freetrialPage import FreeTrialPage
import os
from src.test.utils.Utils import *

@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_url())
    yield driver
    driver.quit()

@allure.title("VWO Free Trial")
@allure.description("tc#0 - VWO Free Trail")
@allure.feature("Feature | VWO  Free Trial ")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver = setup

    login_page = LoginPage(driver=driver)
    login_page.get_free_trial_button().click()

    free_trial_page = FreeTrialPage(driver=driver)
    free_trial_page.enter_free_trial_details_invalid("admin")

    take_screenshot(driver=driver,name="test_vwo_ft_negative")

    error_msg_text = free_trial_page.get_error_message_text()
    assert error_msg_text == "The email address you entered is incorrect."

























