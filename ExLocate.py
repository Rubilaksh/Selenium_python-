from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj=Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
chr_options=Options()
chr_options.add_experimental_option("detach",True)

#this line is used to launch the chrome browser
driver=webdriver.Chrome(service=service_obj, options=chr_options)


driver.get("https://www.google.com")

#driver.find_element(By.NAME,"q").send_keys("selenium learning")

driver.find_element(By.ID,"APjFqb").send_keys("Trying id locator")



