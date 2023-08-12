from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")
driver.maximize_window()
print(driver.title)
sleep(60)
