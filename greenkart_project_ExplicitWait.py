import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

#Implicit wait is called as the Global wait. It will wait for a maxmium time of 10 seconds.
#If the webelement is identified in the 5th second, then the execution would be proceeded from 6th second and wont wait for 10 secs
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

time.sleep(3)
veggies= driver.find_elements(By.XPATH,"//button[contains(text(),'CART')]")
count=len(veggies)

if count >0:
    for veg in veggies:
        veg.click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

explicit_wait=WebDriverWait(driver,8)
explicit_wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

coupon_code=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert coupon_code == "Code applied ..!"
