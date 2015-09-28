from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

safari_driver = "/Users/abhijitpradhan/code/selenium-server-standalone-2.47.1.jar"
os.environ["SELENIUM_SERVER_JAR"] = safari_driver
driver = webdriver.Safari(safari_driver)

driver.get("http://dev.arc.ht/login")
driver.maximize_window()
sleep(5)
email_input = driver.find_element_by_css_selector("div[data-name='username'] input")
password_input = driver.find_element_by_css_selector("div[data-name='password'] input")
email_input.send_keys("mark@architizer.com")
password_input.send_keys("password")
sleep(1)
submit_button = driver.find_element_by_css_selector("a.submit")
submit_button.click()
sleep(10)

driver.get("http://dev.arc.ht/source/specifier/requests/")
sleep(5)
driver.get("http://dev.arc.ht/logout/")
sleep(5)

driver.quit()
