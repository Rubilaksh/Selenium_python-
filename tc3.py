from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.maximize_window()

ber_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(3)
ber_veg = driver.find_elements(By.XPATH,"//h4[contains(text(),'ber')]")
print(len(ber_veg))
#veg_list= []
#for veg in ber_veg:
    #veg_list.append(veg.text)
#print(veg_list)
#assert veg_list == ber_list

for veg in ber_veg:
    print(veg.text,"----",ber_list)
    assert veg.text in ber_list





