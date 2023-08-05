import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=service_obj, options=opt)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Shop").click()
shop_name=driver.find_element(By.TAG_NAME,"h1").text
assert "Shop" in shop_name

phones= driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for phone in phones:

    phone_name= phone.find_element(By.XPATH,"div/h4/a").text
    print(phone_name)

    if phone_name == "Nokia Edge":
        phone.find_element(By.XPATH,"div/button").click()

checkout= driver.find_element(By.XPATH,"//a[contains(@class,'btn-primary')]")
driver.execute_script("arguments[0].scrollIntoView(true);",checkout)

checkout.click()

remove_button= driver.find_element(By.XPATH,"//span[contains(@class,'remove')]")

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[contains(@class,'remove')]")))

status = driver.find_element(By.XPATH,"//strong[contains(text(),'In Stock')]").text
print(status)
if status == "In Stock":
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-success')]").click()

country = driver.find_element(By.ID,"country").send_keys("India")
explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
country_select= driver.find_element(By.LINK_TEXT,"India")
country_select.click()
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()

purchased= driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(purchased)

assert "Success!" in purchased

