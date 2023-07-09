import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(3)

veggies= driver.find_elements(By.XPATH,"//button[contains(text(),'CART')]")
count=len(veggies)
time.sleep(2)

if count >0:
    for veg in veggies:
        veg.click()

time.sleep(2)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(5)

coupon_code=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert coupon_code == "Code applied ..!"
