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

current_window=driver.current_window_handle

driver.find_element(By.LINK_TEXT,"Click Here").click()
all_windows=driver.window_handles

for each_window in all_windows:
    if each_window != current_window:
        driver.switch_to.window(each_window)
        print(driver.find_element(By.TAG_NAME,"h3").text)
        time.sleep(2)
        driver.switch_to.window(current_window)
        print(driver.find_element(By.TAG_NAME,"h3").text)

driver.get("https://www.google.com/")

#driver.close()

driver.quit()