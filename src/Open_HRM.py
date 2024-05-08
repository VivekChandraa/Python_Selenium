import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_open_HRM():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="login_screenshot", attachment_type=AttachmentType.PNG)
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='oxd-form-row']//div//div//div//div//div//div").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//div[@class='oxd-form-row']//div//div//div//div//div//div[text()='Admin']")

    # user role
    time.sleep(10)

    # search user

    actions = ActionChains(driver)
    search_user = driver.find_elements(By.XPATH, "(//input[@data-v-1f99f73c=''])")

    actions.move_to_element(search_user[1]).click(search_user[1]).send_keys("Automation").perform()

    search_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_btn.click()

    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="search_screenshot", attachment_type=AttachmentType.PNG)

    search_result = driver.find_element(By.XPATH, "(//div[@data-v-6c07a142=''])[1]")
    assert search_result.text == "Automation"

    time.sleep(10)