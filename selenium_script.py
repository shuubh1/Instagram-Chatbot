from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Replace with your Instagram username and password
username = "pengi.__"
password = "Hagu_775047"

# List of influencer Instagram accounts
influencer_accounts = ["sandeep__maheshwari"]

# Pre-written message to send to scraped usernames
message = "Hi, I hope you are fine. We have started a good work from home job for everyone from where you an earn upto 30-50 thousand per month. Whatsapp me +91 9433811943 if you wanna know the criteria."

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to Instagram
driver.get("https://www.instagram.com/")

# Wait for the login page to load
login_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

# Wait for the username input field to be interactable
time.sleep(5)
username_input_field = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))
)

# Enter the username
username_input_field.send_keys(username)
password_element = driver.find_element_by_name("password")
password_element.send_keys(password)

# Click the login button
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the feed page to load
feed_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='imeline__feed']"))
)

# List to store scraped usernames
scraped_usernames = []

# Loop until we reach 500 users
while len(scraped_usernames) < 500:
    for influencer_account in influencer_accounts:
        # Navigate to the influencer's account page
        driver.get(f"https://www.instagram.com/{influencer_account}/")

        # Wait for the account page to load
        account_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='account__header']"))
        )

        # Find the first post on the account page
        post_element = driver.find_element_by_xpath("//div[@class='post']")

        # Click on the post to open it
        post_element.click()

        # Wait for the post page to load
        post_page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='post__content']"))
        )

        # Find all comments on the post
        comments_element = driver.find_elements_by_xpath("//div[@class='comment']")

        # Loop through each comment and extract the username
        for comment in comments_element:
            username_element = comment.find_element_by_xpath(".//a[@class='comment__username']")
            scraped_username = username_element.text
            if scraped_username not in scraped_usernames:
                scraped_usernames.append(scraped_username)
                if len(scraped_usernames) >= 500:
                    break

        # Close the post page
        driver.back()

    # If we've reached 500 users, break the loop
    if len(scraped_usernames) >= 500:
        break

# Loop through each scraped username and send a DM
for scraped_username in scraped_usernames:
    # Navigate to the direct message page
    driver.get("https://www.instagram.com/direct/new/")

    # Wait for the direct message page to load
    direct_message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='direct__header']"))
    )

    # Enter the scraped username in the recipient field
    recipient_element = driver.find_element_by_xpath("//input[@name='query']")
    recipient_element.send_keys(scraped_username)
    time.sleep(1)  # wait for the username to be suggested
    recipient_element.send_keys(Keys.RETURN)

    # Enter the pre-written message in the message field
    message_element = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
    message_element.send_keys(message.replace("[influencer_account]", influencer_account))

    # Click the send button
    send_button = driver.find_element_by_xpath("//button[@type='submit']")
    send_button.click()

    # Wait for the message to be sent
    time.sleep(2)

# Close the browser
driver.quit()