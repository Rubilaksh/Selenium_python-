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
#//span[@data-csa-c-content-id='p_89/Samsung']
phones = driver.find_elements(By.XPATH,"//ul[@data-csa-c-content-id='3837712031']")
for phone in phones:
    sam = driver.find_element(By.XPATH,"//ul//span[@data-csa-c-content-id='p_89/Samsung']").text
    print(sam)
    print(phone.text)
    if sam == phone.text:
        phone.find_element(By.XPATH,"//i[@class='a-icon a-icon-checkbox']").click()
#sam = driver.find_element(By.XPATH,"//ul//span[@data-csa-c-content-id='p_89/Samsung']")
#print(sam)
