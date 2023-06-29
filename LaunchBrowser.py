from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
service_obj=Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
chr_options=Options()
chr_options.add_experimental_option("detach",True)

#this line is used to launch the chrome browser
driver=webdriver.Chrome(service=service_obj, options= chr_options)

#driver= webdriver.Firefox(service=service_obj)

#get() is the method to navigate to the specific url
driver.get("https://www.google.com/")

driver.find_element(By.NAME,"q").send_keys("seleneium")

print("Title of the "
      ""
      "webpage is ",driver.title)

driver.maximize_window()

driver.get("https://www.yahoo.com/")

print(driver.current_url)

driver.refresh()

#driver.back()

#driver.forward()

#driver.minimize_window()



