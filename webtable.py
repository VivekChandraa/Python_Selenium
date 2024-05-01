import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

def test_table():
    driver.get("https://awesomeqa.com/webtable.html")
    table_row = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    print(len(table_row))
    table_column=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr/td")
    print(len(table_column))

