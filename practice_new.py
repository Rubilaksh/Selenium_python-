from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service_obj=Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt=Options()
opt.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.maximize_window()
dr=driver.find_element(By.XPATH,"//input[@id = 'userId']")
dr.send_keys("rubilakshmanan@gmail.com")
##using And
driver.find_element(By.XPATH,"//input[@title='Password' and @name='Password']").send_keys("Jaisai")
##by using contains
driver.find_element(By.XPATH,"//input[contains(@name,'com')]").send_keys("HCL Tech")
##using text()
#driver.find_element(By.XPATH,"a
