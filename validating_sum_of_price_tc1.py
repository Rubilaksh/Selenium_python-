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
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")

time.sleep(3)
veggies = driver.find_elements(By.XPATH,"//button[contains(text(),'CART')]")
count = len(veggies)

if count > 0:
    for veg in veggies:
        veg.click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED')]").click()
summ = 0
time.sleep(3)

#we should not add text to findElements instead we should be adding to the individual webelement
prices = driver.find_elements(By.XPATH,"//tbody/tr/td[4]/p[@class='amount']")
print(len(prices))

for p in prices:
    summ= summ + int(p.text)
print(summ)

cart_sum = driver.find_element(By.CLASS_NAME,"discountAmt").text
print(cart_sum)
assert int(cart_sum) == summ

