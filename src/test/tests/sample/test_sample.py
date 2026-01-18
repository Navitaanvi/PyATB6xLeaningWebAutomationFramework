import allure
import pytest
import time

@allure.title("Dry run of the Passed TestCase")
@allure.description("TC#1 Dry run of the Passed Testcase")
def test_sample_pass():
    print("Hi")
    assert True == True

@allure.title("Dry run of the Failed TestCase")
@allure.description("TC#2 Dry run of the Passed Testcase")
def test_sample_fail():
    print("Hi")
    assert True == False
