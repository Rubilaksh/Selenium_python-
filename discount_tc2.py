from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import re

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
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[contains(text(),'Apply')]").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
total_amt = driver.find_element(By.CSS_SELECTOR,".totAmt").text
print(total_amt)
disc_percentage =driver.find_element(By.CSS_SELECTOR,".discountPerc").text
print(disc_percentage)
disc_number_list = re.findall(r'[0-9]+',disc_percentage)
print(disc_number_list)
disc_int = list(map(int, disc_number_list))
print(disc_int)
disc_logic = int(total_amt) * disc_int[0]
print(disc_logic)
dl = disc_logic / 100
print(dl)
after_disc = int(total_amt) - dl
print(after_disc)
final_price = driver.find_element(By.CLASS_NAME,"discountAmt").text
print(final_price)

assert after_disc == (float(final_price) or int(final_price))