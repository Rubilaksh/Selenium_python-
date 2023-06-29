from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/msedgedriver.exe")

opt=Options()
opt.add_experimental_option("detach", True)
driver=webdriver.Edge(service=service_obj, options=opt)
driver.get("https://www.youtube.com/")
driver.maximize_window()
dr=driver.find_element(By.XPATH,"//input[@id='search']")
dr.send_keys("Selenium tutorial for beginners")
dr.send_keys(Keys.ENTER)
select=driver.find_element(By.XPATH,"//h3[@id='text-image-title']")
select.click()