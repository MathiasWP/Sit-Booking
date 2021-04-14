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

username = os.environ.get("username")
password = os.environ.get("password")

sit_user_url = "https://www.sit.no/user"
driver.get(sit_user_url)

def querySelector(query):
    return driver.find_element_by_css_selector(query)

login_btn = querySelector('.button--login')
login_btn.click()

org_chooser = querySelector('#org-chooser-selectized')
org_chooser.click()
org_chooser.send_keys("NTNU", Keys.RETURN)

org_submit_btn = querySelector('#discoform_feide button[type=submit]')
org_submit_btn.click()

username_input = querySelector("#username")
username_input.send_keys(username)

password_input = querySelector("#password")
password_input.send_keys(password, Keys.RETURN)

# Step 2: Choosing training
sit_website_url = "https://www.sit.no/trening/treneselv"
driver.get(sit_website_url)

# Because sits website is fucking amazing we have to wait until the booking-iframe is ready
wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(querySelector('#ibooking-iframe')))
wait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".days")))

# Taking over with JS from here to make things easier (mostly because i am too lazy to learn xpath and i just want to use querySelectorAll with CSS)
JS_script = """
const allBookableWithLatestFirst = [...document.querySelectorAll('.instance:not(.not-bookable)')].reverse();
const wantedBooking = allBookableWithLatestFirst.find(d => d.innerHTML.includes('Gløshaugen'));
wantedBooking.click();

const bookBtn = document.querySelector('.instanceModalButtons .btn-primary');
bookBtn.click();
"""
driver.execute_script(JS_script)

