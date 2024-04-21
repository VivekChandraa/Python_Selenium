# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password
# Verify that Trial is fnished and current URL also
# Add a logic to add Allure Screen for the Trail end.

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_idrive():
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@id ='frm-btn']").click()
    driver.maximize_window()
    time.sleep(15)
    message_member = driver.find_element(By.TAG_NAME,"h5").text
    assert message_member =="Your free trial has expired"
    assert driver.current_url=="https://www.idrive360.com/enterprise/account?upgradenow=true"

