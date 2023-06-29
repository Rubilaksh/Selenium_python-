from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/msedgedriver.exe")

edge_options= Options()
edge_options.add_experimental_option("detach", True)
driver=webdriver.Edge(service=service_obj, options=edge_options)

driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("Capital of India")

driver.get("https://www.facebook.com/")
print(driver.title)

driver.maximize_window()
print(driver.current_url)
