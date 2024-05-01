import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_HRM():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    time.sleep(5)