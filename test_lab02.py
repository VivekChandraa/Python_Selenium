# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appoinment button
# verify that url changes - assert
# time.sleep(3)
# enter the username, password
# next page verify the current url
# make appoinment text on the web page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    elementbutton = driver.find_element(By.ID,"btn-make-appointment").click()
    assert driver.current_url!="https://katalon-demo-cura.herokuapp.com/"
    time.sleep(3)
    driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    assert driver.current_url == driver.current_url
    driver.find_element(By.ID,"btn-login").click()
