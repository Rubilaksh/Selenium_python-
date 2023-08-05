from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver= webdriver.Chrome(service=service_obj, options=opt)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#To scroll down by 700 pixels
driver.execute_script("window.scrollBy(0,700);")

time.sleep(2)

#To scroll down to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(2)

#to scrollto the top of the page
#driver.execute_script("window.scrollTo(0,0);")

#to scroll up by 700
driver.execute_script("window.scrollBy(0,-700);")

#to to horizontl scroll
driver.execute_script("window.scrollBy(300,0);")

print(driver.execute_script("return document.title;"))

driver.execute_script("location.reload();")
time.sleep(2)

alert_button= driver.find_element(By.ID,"alertbtn")
driver.execute_script("arguments[0].scrollIntoView(true);",alert_button)

driver.execute_script("argument[0].click()",alert_button)
