from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


sel = Service("C:/Users/yuvar/PycharmProjects/pythonSelenium/drivers/chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)

web_chr = webdriver.Chrome(service=sel, options=opt)
web_chr.get("https://www.google.com/")

web_chr.get("https://www.yahoo.com/")
print(web_chr.title)
web_chr.maximize_window()
print(web_chr.current_url)