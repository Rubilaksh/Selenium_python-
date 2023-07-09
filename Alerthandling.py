import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt, service= service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name="Rubini"
driver.find_element(By.NAME,"enter-name").send_keys(name)

driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)

#to switch the control from browser to alert
alert = driver.switch_to.alert

#to get the alert text
alerText= alert.text
print("ALert Text-->",alerText)

#validating whether the name is present in alert text
assert name in alerText

#to accept the alert
#alert.accept()

#to dismiss the alert
alert.dismiss()



