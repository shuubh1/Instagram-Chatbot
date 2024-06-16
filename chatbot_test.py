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
#click the login button
login_button.click()
time.sleep(10)

#locate the 'Save info' button
save_info = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save info')]"))
)
#click the 'Save info' button
save_info.click()

time.sleep(5)
#locate the 'Not now' button
not_now = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
)
#click the 'Not now' button
not_now.click()
time.sleep(10)
#wait for the feed page to load
#feed_element = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.XPATH, "//*[@id='mount_0_0_sA']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div[1]"))
#)
#feed_element.send_keys(Keys.ESCAPE)
#find the login button
login_button2 = driver.find_element(By.XPATH, "//button[@type='submit']")
#click the login button
login_button2.click()
time.sleep(10)
#list to store scraped usernames
scraped_usernames = []

#loop until we reach 500 users
while len(scraped_usernames) < 500:
    for influencer_account in influencer_accounts:
        #navigate to the influencer's account page
        driver.get(f"https://www.instagram.com/{influencer_account}/")

        #wait for the account page to laod
        account_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='account__header']"))
        )

        #find the first post on the account page
        post_element = driver.find_element(By.XPATH, "//div[@class='_aagu']")

        #click on the post to open it
        post_element.click()
time.sleep(9999999)
driver.quit()