import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opti = Options()
opti.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opti)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(5)

countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:

     if country.text == "India":
         country.click()
         break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "Ind"

#will close the current active window
driver.close()



