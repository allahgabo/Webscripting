
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# Function to add random delay to mimic human behavior
def random_delay(min_delay=1.5, max_delay=3.0):
    time.sleep(random.uniform(min_delay, max_delay))


# Function to set up the Chrome driver with additional options like User-Agent and headless mode
def setup_driver(headless=True):
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--no-sandbox")  # To run in some environments (e.g., Docker)

    # Add a User-Agent to make it look like a real browser
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Disable WebDriver detection
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Automatically get the latest version of ChromeDriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


# Function to log in to the website
def login(driver, username, password):
    try:
       
        driver.get('http://purchasingprogramsaudi.com/') 

        # Wait for the username field to be present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "j_username")))

        # Enter username and password
        username_field = driver.find_element(By.ID, "j_username")
        password_field = driver.find_element(By.ID, "j_password")

        username_field.send_keys(username)
        random_delay()  # Introduce a delay to mimic human interaction
        password_field.send_keys(password)
        random_delay()

        # Click on the login button (anchor tag with id="btnLogin")
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        random_delay()

        # Wait for successful login by checking an element on the next page (adjust as needed)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "logged-in-element")))  # Change this to an actual element that appears after login

        print("Login successful!")
    except Exception as e:
        print(f"Error during login: {e}")


# Function to interact with the div element with class 'div_assist_dashboard_Title'
def interact_with_dashboard_title(driver):
    try:
        # Wait until the div with the class 'div_assist_dashboard_Title' is present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "div_assist_dashboard_Title")))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "input_btn")))
        # Find the element by its class name
        dashboard_title = driver.find_element(By.CLASS_NAME, "div_assist_dashboard_Title")
        views = driver.find_element(By.CLASS_NAME, "input_btn")

        # Extract and print the text of the element
        print(f"Dashboard Title: {dashboard_title.text}")

        # Click on the anchor tag within the div if it exists
        anchor_tag = dashboard_title.find_element(By.TAG_NAME, "a")
        view_class = views.find_element(By.TAG_NAME, "a")
        anchor_tag.click()
        print("Clicked on the 'Waiting Confirmation Referral Requests' link.")
        random_delay()
        view_class.click()
        print("Clicked on the 'View Class")

    except Exception as e:
        print(f"Error interacting with 'div_assist_dashboard_Title': {e}")


# Main function to run the script
def main():
    # Set up the Chrome driver
    driver = setup_driver(headless=False)  # Set headless=True if you don't need the browser UI

    # Login credentials
    username = 'MOH1@C1461'
    password = 'AP@@123123'

    # Attempt to login
    login(driver, username, password)

    # Interact with the div element with class 'div_assist_dashboard_Title'
    interact_with_dashboard_title(driver)

    # Add more automation tasks here if necessary

    # Close the driver after completing the tasks
    time.sleep(120)
    driver.quit()


if __name__ == "__main__":
    main()



