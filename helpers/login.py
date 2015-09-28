from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep


def login(driver):
    driver.get("http://dev.arc.ht/login")
    driver.maximize_window()
    sleep(5)
    email_input = driver.find_element_by_css_selector("div[data-name='username'] input")
    password_input = driver.find_element_by_css_selector("div[data-name='password'] input")
    email_input.send_keys("mark@architizer.com")
    password_input.send_keys("password")
    password_input.send_keys(Keys.RETURN)
    sleep(15)
