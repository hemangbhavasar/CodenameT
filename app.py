import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Define the URL of the Tableau page
url = 'https://public.tableau.com/app/profile/hemang.bhavasar/viz/Recessioniscoming/RecessionisComing'

def generate_random_profile_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=profile')  # Use a custom profile directory

while True:
    # Generate a random delay in seconds
    random_delay = random.randint(1, 60)
    delay_seconds = random_delay
    print(delay_seconds)

    # Generate a random user name
    random_username = generate_random_profile_name()
    print(random_username)

    # Wait for the random delay
    time.sleep(delay_seconds)

    # Set up Chrome driver service
    chrome_service = Service(ChromeDriverManager().install())

    # Launch Chrome with the desired profile
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Open the Tableau page
    driver.get(url)

    # Wait for the page to load
    time.sleep(10)

    # Click on the "Nominate viz of the day" button
    nominate_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div[1]/div/div[2]/button[5]/i')
    nominate_button.click()

    # Wait for the nomination to complete
    time.sleep(10)

    # Close the browser
    driver.quit()
