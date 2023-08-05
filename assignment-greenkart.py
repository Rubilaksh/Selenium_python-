from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver= webdriver.Chrome(service=service_obj, options=opt)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.ID,"search-field").send_keys("to")
#veggies = []
time.sleep(3)
veggies = driver.find_elements(By.XPATH,"//td[contains(text(),'to')]")
#veggy = driver.find_element(By.XPATH,"//td[contains(text(),'Potato')]").text
#veggies = driver.find_element(By.TAG_NAME,"tr").text
print(len(veggies))
for veg in veggies:



#veggies[0],veggies[1] = veggies[1],veggies[0]

