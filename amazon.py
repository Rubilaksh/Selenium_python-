import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt =Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)
search = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
search.send_keys("mobile phones")
search.send_keys(Keys.ENTER)
time.sleep(5)
phones = driver.find_elements(By.CSS_SELECTOR,".s-image")
print(len(phones))
phones[0].click()
