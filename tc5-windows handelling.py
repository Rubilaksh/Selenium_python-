from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
first_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()

win_hadles= driver.window_handles

for handle in win_hadles:
    if handle != first_window:
        driver.switch_to.window(handle)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT,"Skip it, take me to the tips").click()
        time.sleep(2)
        driver.switch_to.window(first_window)