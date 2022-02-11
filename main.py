from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

import time

start_time = time.time()

username = "LinkedIn User"  # Enter Email
password = "LinkedIn Password"  # Enter Password
phone_number = "Phone Number"  # Enter Phone number

s = Service('Chrome Driver Path/chromedriver')  # Enter chromedriver path/folder
driver = wd.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/")  # Exact Url of linkedIn w/ job preferences

sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()
time.sleep(2)

Email_field = driver.find_element(By.ID, "username")
Email_field.send_keys(username)

Password_field = driver.find_element(By.ID, "password")
Password_field.send_keys(password)
Password_field.send_keys(Keys.ENTER)

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(3)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".job-s-apply button")
        apply_button.click()
        time.sleep(3)

        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        phone.send_keys(phone_number)
        next_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if next_button.get_attribute("data-control-name") == "continue unify":
            next_button.click()
        else:
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-model__dismiss")
            close_button.click()
            time.sleep(3)
            discard_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button')]//*[contains("
                                                           "., 'Discard')]/..")
            discard_button.click()
            print("Complete application, skipped..")
            continue

        time.sleep(3)
        review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
        if review_button.get_attribute("data-control-name") == "continue unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-model__dismiss")
            close_button.click()
            time.sleep(3)
            discard_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button')]//*[contains("
                                                           "., 'Discard')]/..")
            discard_button.click()
            print("Complete application, skipped..")
            continue
        else:
            review_button.click()
            time.sleep(3)
            submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            if submit_button.get_attribute("data-control-name") == "submit_unify":
                submit_button.click()
                time.sleep(3)
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-model__dismiss")
                close_button.click()
            else:
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-model__dismiss")
                close_button.click()
                time.sleep(3)
                discard_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button')]//*["
                                                               "contains(., 'Discard')]/..")
                discard_button.click()
                print("Complete application, skipped..")
                continue
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
