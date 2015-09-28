from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
driver.get("http://dev.arc.ht/products/")
driver.maximize_window()
sleep(1)
main_search_input = driver.find_element_by_css_selector(".content input[type='text']")
main_search_input.send_keys("balustrade")
main_search_input.send_keys(Keys.RETURN)
sleep(5)
global_search_holder = driver.find_element_by_css_selector("span#globalSearchPlaceholder ")
global_search_holder.click()
sleep(1)
global_search_input = driver.find_element_by_css_selector("input#globalSearchInput")
global_search_input.send_keys("chandelier")
sleep(5)
global_search_input.send_keys(Keys.RETURN)
sleep(5)
driver.quit()
