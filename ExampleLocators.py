from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
service_obj=Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
chr_options=Options()
key_obj = Keys()
chr_options.add_experimental_option("detach",True)

#this line is used to launch the chrome browser
driver=webdriver.Chrome(service=service_obj, options= chr_options)

driver.get("https://www.google.com")

driver.maximize_window()

#driver.find_element(By.ID,"APjFqb").send_keys("Trying id locator")

#driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("Trying class name locator")

#driver.find_element(By.LINK_TEXT,"Gmail").click()

#driver.find_element(By.PARTIAL_LINK_TEXT,"Image").click()

#syntax for xpath
#//tagname[@attribute='value']

#driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("Learning xpath")

dr=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
dr.send_keys("Xpath with id")
dr.send_keys(Keys.ENTER)


