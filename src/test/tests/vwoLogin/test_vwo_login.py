"""
Assertions and use the page object class
Webdriver start
user interaction + Assertions
close webdriver
"""
import allure
from selenium import webdriver
from src.test.constants.Constants import Constants
from src.test.pageObjects.vwo.loginPage import LoginPage
from src.test.pageObjects.vwo.dashboardPage import DashboardPage
from dotenv import load_dotenv
import os
import pytest
from src.test.utils.Utils import *

@pytest.fixture
def setup():
    load_dotenv(override=True)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants().app_url())
    return driver

@allure.title("VWO Login Test")
@allure.id("JIRA_ID_1234")
@allure.description("TC#0 - VWO App Negative Test")
@allure.feature("Feature | VWO App Negative Test")
@pytest.mark.negative

def test_vwo_login_negative(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_vwo(usr = os.getenv("INVALID_USERNAME"),
                            pwd= os.getenv("INVALID_PASSWORD")
    )
    error_msg_element_text = login_page.get_error_msg_as_text()
    take_screenshot(driver = driver,name = "test_vwo_login_negative")
    assert error_msg_element_text == os.getenv("error_message_expected")

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_Positive(setup):
    driver = setup
    login_page = LoginPage(driver = driver)
    login_page.login_to_vwo(usr=os.getenv("USERNAME"),
                            pwd= os.getenv("PASSWORD"))
    print("Current_URL",driver.current_url)
    # print("Page_Source",driver.page_source)
    print("ENV USERNAME =", os.getenv("USERNAME"))
    print("ENV PASSWORD =",os.getenv("PASSWORD"))
    dashboard_page = DashboardPage(driver=driver)
    user_name = dashboard_page.user_logged_in_text()
    take_screenshot(driver = driver, name = 'test_vwo_login_positive')
    print("EXPECTED USER =", os.getenv("USERNAME_LOGGED_IN"))
    print("ACTUAL USER =", user_name)
    print("RAW ACTUAL USER repr =", repr(user_name))

    assert os.getenv("USERNAME_LOGGED_IN") == user_name



















