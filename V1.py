import time

from selenium import webdriver
def test_log_vwo():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com ")
    driver.maximize_window()
    print(driver.title)
    assert driver.title=="Login - V"