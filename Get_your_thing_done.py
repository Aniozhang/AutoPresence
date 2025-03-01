from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# CONFIGURATIONS - Update these
CANVAS_URL = "https://yourcanvas.instructure.com"  # Replace with your Canvas URL
USERNAME = "your_username"
PASSWORD = "your_password"
ATTENDANCE_URL = "https://yourcanvas.instructure.com/courses/xxxxxx/attendance"  # Replace with actual attendance page URL

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background (remove for debugging)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# Path to ChromeDriver
CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Update with your actual path

# Set up WebDriver
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open Canvas login page
    driver.get(CANVAS_URL)
    time.sleep(2)  # Allow page to load

    # Enter username
    user_input = driver.find_element(By.ID, "pseudonym_session_unique_id")  # Adjust selector if needed
    user_input.send_keys(USERNAME)

    # Enter password
    pass_input = driver.find_element(By.ID, "pseudonym_session_password")  # Adjust selector if needed
    pass_input.send_keys(PASSWORD)
    pass_input.send_keys(Keys.RETURN)  # Press Enter

    time.sleep(5)  # Wait for login

    # Navigate to attendance page
    driver.get(ATTENDANCE_URL)
    time.sleep(5)

    # Locate and mark attendance
    try:
        present_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Present')]")
        present_button.click()
        print("Attendance marked successfully!")
    except:
        print("Attendance button not found or already marked.")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
