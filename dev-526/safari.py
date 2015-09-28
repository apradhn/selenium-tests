from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

safari_driver = "/Users/abhijitpradhan/code/selenium-server-standalone-2.47.1.jar"
os.environ["SELENIUM_SERVER_JAR"] = safari_driver
driver = webdriver.Safari(safari_driver)

driver.get("http://dev.arc.ht/products/")
driver.maximize_window()
sleep(1)
main_search_input = driver.find_element_by_css_selector(".content input[type='text']")
main_search_input.send_keys("balustrade")
sleep(5)
submit_button = driver.find_element_by_css_selector("form.heroForm button[type='submit']")
submit_button.click()
sleep(5)
global_search_holder = driver.find_element_by_css_selector("span#globalSearchPlaceholder ")
global_search_holder.click()
sleep(5)
global_search_input = driver.find_element_by_css_selector("input#globalSearchInput")
global_search_input.send_keys("chandelier")
sleep(1)
global_search_input.send_keys(Keys.RETURN)
sleep(10)
driver.quit()
