from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opt, service= service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.XPATH,"//input[@class='radioButton']")

for radio in radio_buttons:
    if radio.get_attribute("value")== "radio1":
        radio.click()
        assert radio.is_selected()
        break