from selenium import webdriver
#from selenium.webdriver.chrome import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


service_obj = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")


opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=service_obj, options=opt)
driver.get("https://www.google.com/")
driver.maximize_window()

