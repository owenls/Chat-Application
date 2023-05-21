from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
def test_private_room():
    driver = webdriver.Chrome('C:/Users/John Lumagbas/Desktop/GITHUB-UWA/CITS3403-Project-1/selenium-testing/chromedriver.exe')
    driver.get("http://127.0.0.1:5000/login")
    driver.maximize_window()
    # Login this assumes that a person with this email is already registered
    email = "testjohn@example.com"
    password = "j"

    email_input = driver.find_element("id", "email")
    email_input.send_keys(email)
    print("Email entered")

    password_input = driver.find_element("id", "password")
    password_input.send_keys(password)
    print("Password entered")

    submit_button = driver.find_element("xpath", "//button[@type='submit']")
    submit_button.click()
    print("Submit button clicked")
    # Wait for the login process to complete
    time.sleep(2)

    # Navigate to the home page
    driver.get("http://127.0.0.1:5000/home")

    # Click on the private message icon
    private_message_button = driver.find_element_by_css_selector("button[name='private_message']")
    private_message_button.click()

    # Wait for the private room page to load
    time.sleep(2)

    # Perform additional interactions or assertions as needed

    driver.close()

test_private_room()