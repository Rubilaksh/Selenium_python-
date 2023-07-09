import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.implicitly_wait(3)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("to")
time.sleep(5)
veggies=driver.find_elements(By.XPATH,"//button[contains(text(),'CART')]")

count= len(veggies)
print(count)
if count > 0:
    for veg in veggies:
        veg.click()
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED')]").click()
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
code = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
#coupon_code=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
#print(code)
assert code == "Code applied ..!"
driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()