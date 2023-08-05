import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

'''
Actions: Mouse and keyboard events
Methods inside ActionChains class,
1. move_to_element(ele)
2. double_click(ele)
3. context_click(ele) --> (right click)
4. click_and_hold(ele)
5.drag_and_drop(source, destination)
'''
act=ActionChains(driver)
act.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(2)
act.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)


