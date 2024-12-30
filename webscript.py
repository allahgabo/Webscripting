import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Constants
LOGIN_URL = 'http://purchasingprogramsaudi.com/'
USERNAME = 'MOH1@C1461'
PASSWORD = 'AP@@123123'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Function to add random delay to mimic human behavior
def random_delay(min_delay=1.5, max_delay=3.0):
    time.sleep(random.uniform(min_delay, max_delay))

# Function to set up the Chrome driver with additional options like User-Agent and headless mode
def setup_driver(headless=True):
    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--no-sandbox")  # To run in some environments (e.g., Docker)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Add a User-Agent to make it look like a real browser
    chrome_options.add_argument(f"user-agent={USER_AGENT}")

    # Disable WebDriver detection
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # Automatically get the latest version of ChromeDriver
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

# Function to log in to the website
def login(driver, username, password):
    try:
        # Open the login page
        driver.get(LOGIN_URL)

        # Wait for the username field to be present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "j_username")))

        # Enter username and password
        username_field = driver.find_element(By.ID, "j_username")
        password_field = driver.find_element(By.ID, "j_password")

        username_field.send_keys(username)
        random_delay()  # Introduce a delay to mimic human interaction
        password_field.send_keys(password)
        random_delay()

        # Click on the login button
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        random_delay()

        # Wait for successful login by checking an element on the next page (adjust as needed)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "logged-in-element")))  # Change this to an actual element that appears after login

        print("Login successful!")
    except Exception as e:
        print(f"Error during login: {e}")

# Function to check the value and interact with the div element with class 'div_assist_dashboard_Title'
def check_and_interact(driver):
    try:
        # Wait until the span with the id 'spfnc_waiting_confirmation_referral' is present
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "spfnc_waiting_confirmation_referral")))
        
        # Get the value of the span element
        value_span = driver.find_element(By.ID, "spfnc_waiting_confirmation_referral")
        value = int(value_span.text)
        
        # Check if the value is greater than 0
        if value > 0:
            print(f"New cases found: {value}")
            # Wait until the div with the class 'div_assist_dashboard_Title' is present
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "div_assist_dashboard_Title")))
        
            # Find the div element
            dashboard_title = driver.find_element(By.CLASS_NAME, "div_assist_dashboard_Title")
     
            # Find the anchor tag within the div
            anchor_tag = dashboard_title.find_element(By.TAG_NAME, "a")

            # Click the anchor tag
            anchor_tag.click()
            print("Clicked on the 'Waiting Confirmation Referral Requests' link.")
            random_delay()

            # Wait for the "View" button within the table row to be present and click it
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "input_btn")))
            view_buttons = driver.find_elements(By.CLASS_NAME, "input_btn")
            for button in view_buttons:
                if "View" in button.text:
                    button.click()
                    print("Clicked on the 'View' button.")
                    random_delay()
                    break

            # Wait for the "Close" button to be present and click it
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ui-dialog-buttonset")))
            close_button = driver.find_element(By.XPATH, "//div[@class='ui-dialog-buttonset']/button[contains(text(), 'Close')]")
            close_button.click()
            print("Clicked on the 'Close' button.")
            random_delay()

            # Wait for the "View documents" link to be present and click it
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@style='width:100%;float:left;font-size:8px !important;']//a[contains(text(), 'View documents')]")))
            view_documents_link = driver.find_element(By.XPATH, "//div[@style='width:100%;float:left;font-size:8px !important;']//a[contains(text(), 'View documents')]")
            view_documents_link.click()
            print("Clicked on the 'View documents' link.")
            random_delay()
        else:
            print("No new cases.")
        
    except Exception as e:
        print(f"Error interacting with 'div_assist_dashboard_Title': {e}")

# Main function to run the script
def main():
    # Set up the Chrome driver
    driver = setup_driver(headless=False)  # Set headless=True if you don't need the browser UI

    # Attempt to login
    login(driver, USERNAME, PASSWORD)

    # Check the value and interact with the div element with class 'div_assist_dashboard_Title' if needed
    check_and_interact(driver)
    # Close the driver after completing the tasks
    time.sleep(120)
    driver.quit()

if __name__ == "__main__":
    main()



