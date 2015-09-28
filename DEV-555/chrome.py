from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import os

chromedriver = "/Users/abhijitpradhan/code/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://dev.arc.ht/login")
sleep(5)
email_input = driver.find_element_by_css_selector("div[data-name='username'] input")
password_input = driver.find_element_by_css_selector("div[data-name='password'] input")
email_input.send_keys("mark@architizer.com")
password_input.send_keys("password")
password_input.send_keys(Keys.RETURN)
sleep(15)
driver.get("http://dev.arc.ht/source/supplier/signup/")
sleep(10)
brand_input = driver.find_element_by_css_selector("div[name='brand'] input")
brand_input.send_keys("Eames")
sleep(5)
select_option = driver.find_element_by_css_selector("div.option.brand")
select_option.click()
position_input = driver.find_element_by_css_selector("div[name='position'] input")
position_input.send_keys("Test")
sleep(1)
join_button = driver.find_element_by_css_selector("button[type='submit']")
join_button.click()
sleep(5)
driver.get("http://dev.arc.ht/admin/users/rolerequest/")
sleep(5)
checkbox = driver.find_element_by_name("_selected_action")
checkbox.click()
select = Select(driver.find_element_by_name("action"))
select.select_by_value("delete_selected")
submit_button = driver.find_element_by_css_selector("button[type='submit']")
submit_button.click()
sleep(5)
submit_button = driver.find_element_by_css_selector("input[type='submit']")
submit_button.click()
driver.quit()
