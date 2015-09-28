from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

interval = 5
driver = webdriver.Firefox()
driver.get("http://dev.arc.ht/")
sleep(interval)
driver.maximize_window()
sleep(interval)
driver.quit()