import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opti = Options()
opti.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opti)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        #checkbox.click()
        assert checkbox.is_selected()
        break
