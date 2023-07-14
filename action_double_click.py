import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver= webdriver.Chrome(service=service_obj, options=opt)

driver.get("https://demoqa.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(5)

act = ActionChains(driver)
drag = driver.find_element(By.ID,"draggable")
drop = driver.find_element(By.ID,"droppable")
time.sleep(3)
act.drag_and_drop(drag, drop).perform()
time.sleep(5)
assert driver.find_element(By.XPATH,"//p[contains(text(),'Dropped!')]")