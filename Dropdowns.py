import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

service_obj= Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opti = Options()
opti.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=service_obj, options=opti)
driver.get("https://demo.guru99.com/test/newtours/register.php")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input[name='firstName']").send_keys("Rubini")
#driver.find_element(By.NAME,"firstName").send_keys("Yuvi")
driver.find_element(By.NAME,"lastName").send_keys("Lakshmanan")
driver.find_element(By.NAME,"phone").send_keys("9944901900")
driver.find_element(By.CSS_SELECTOR,"input#userName").send_keys("rubilakshmana@gmail.com")
driver.find_element(By.NAME,"address1").send_keys("No-1, 2nd street")
driver.find_element(By.XPATH,"//input[@name='city']").send_keys("Chennai")
driver.find_element(By.XPATH,"//input[contains(@name,'sta')]").send_keys("Tamilnadu")
driver.find_element(By.XPATH,"//input[contains(@name,'postal')]").send_keys("600124")



dropdown= Select(driver.find_element(By.XPATH,"//select[@name='country']"))
time.sleep(3)
dropdown.select_by_visible_text("BERMUDA")
time.sleep(3)
dropdown.select_by_value("BRAZIL")

time.sleep(3)
dropdown.select_by_index(5)
time.sleep(3)