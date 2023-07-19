from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver= webdriver.Chrome(service=service_obj, options=opt)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
time.sleep(2)
print(driver.find_element(By.PARTIAL_LINK_TEXT,"Classes").is_displayed())

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"AbstractAnnotations").click()
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

