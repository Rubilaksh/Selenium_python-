from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opti = Options()
opti.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opti)

driver.get("https://www.google.com/")

driver.maximize_window()

#By Id-> tagname#idname
#driver.find_element(By.CSS_SELECTOR,"textarea#APjFqb").send_keys("learing css")

#By Class-> tagname.classname
#driver.find_element(By.CSS_SELECTOR,"textarea.gLFyf").send_keys("css class name")

#By attribute-> tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"textarea[title='Search']").send_keys("css attribute")




