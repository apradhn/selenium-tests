from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()

driver.get("http://dev.arc.ht/login")
driver.maximize_window()
sleep(5)
email_input = driver.find_element_by_css_selector("div[data-name='username'] input")
password_input = driver.find_element_by_css_selector("div[data-name='password'] input")
email_input.send_keys("mark@architizer.com")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)
sleep(15)

driver.get("http://dev.arc.ht/source/specifier/requests/")
sleep(5)
driver.get("http://dev.arc.ht/logout/")
sleep(5)

driver.quit()