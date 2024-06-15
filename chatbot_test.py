from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#my user and pw
username = "pengi.__"
password = "Hagu_775047"

#list of influencer ig ac (for now only 1 for testing purposes)
influencer_accounts = ["sandeep__maheshwari"]

#message to dm
message = "Hi, I hope you are fine. We have started a good work from home job for everyone from where you an earn upto 30-50 thousand per month. Whatsapp me +91 9433811943 if you wanna know the criteria."

#create a new instance of the chrome driver
driver = webdriver.Chrome()

#navigate to instagram
driver.get("https://www.instagram.com/")

#wait for the login page to load and locate the username field
login_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

#wait for the username input field to be interactable
time.sleep(5)
username_input_field = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))
)

#enter the username
username_input_field.send_keys(username)
#find the pw input field
password_element = driver.find_element(By.NAME, "password")
#enter the pw
password_element.send_keys(password)

#find the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#click the logn button
login_button.click()
time.sleep(10)
#lets try this one out
not_now = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save info')]"))
)
not_now.click()
time.sleep(5)
#ik why now
not_now2 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
)
not_now2.click()
time.sleep(9999999)
driver.quit()