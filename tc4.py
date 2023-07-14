import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()
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
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshetty")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

promo_code = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert promo_code == "Invalid code ..!"
perc = driver.find_element(By.CSS_SELECTOR,".discountPerc").text
print(perc)
disc_per = list(map(int,re.findall(r'[0-9]+',perc)))
print(disc_per)
assert disc_per[0] == 0
tot_amt = driver.find_element(By.CSS_SELECTOR,".totAmt").text
after_disc = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print(tot_amt)
print(after_disc)
assert tot_amt == after_disc