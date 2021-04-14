import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By

# Setting desired driver
cwd = os.getcwd()
driver = webdriver.Chrome(cwd + '/drivers/chrome/v89/mac/chromedriver')

# Step 1: Logging in
from dotenv import load_dotenv, find_dotenv # It is not required, but recommended to store your credentials in an .env file and load them with this library
load_dotenv(find_dotenv())

telephone = os.environ.get("telephone")
password = os.environ.get("password")

ibooking_login_url = "https://ibooking.sit.no/index.php?page=login"
driver.get(ibooking_login_url)

def querySelector(query):
    return driver.find_element_by_css_selector(query)

username_input = querySelector("#username")
username_input.send_keys(telephone)

password_input = querySelector("#password")
password_input.send_keys(password, Keys.RETURN)

# Taking over with JS from here to make things easier
JS_script = """
const allInstancesWithLatestFirst = [...document.querySelectorAll('.visualInstance')].reverse();
const wantedBooking = allInstancesWithLatestFirst.find(el => el.getAttribute('onclick').includes('Reserver timen'))
const aid = wantedBooking.id.replace('visual', '');
location.href='/index.php?page=reservation&aid=' + aid;
"""
driver.execute_script(JS_script)

reserve_button = querySelector('input[type="submit"]')
reserve_button.click()
