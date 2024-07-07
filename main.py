from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv("./vars/.env")

# Constants
GOOGLE_EMAIL = os.getenv("G_EMAIL")
GOOGLE_PASSWORD = os.getenv("G_PASS")

class TinderAutoSwipe:
    driver: webdriver
    main_window = ""

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--lang=en")
        chrome_options.add_argument(f"--user-data-dir={os.getcwd()}/.data")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://tinder.com/")
        sleep(5)

        # Accept cookies if present
        try:
            cookies_button = self.driver.find_element(By.XPATH, '//*[text()="I accept"]')
            cookies_button.click()
            sleep(1)
        except NoSuchElementException:
            print("No cookies button found")

        # Click on "Log in" button
        try:
            login_button = self.driver.find_element(By.XPATH, '//*[text()="Log in"]')
            login_button.click()
            sleep(5)
        except NoSuchElementException:
            print("Login button not found")

        # Switch to Google login frame
        try:
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@title="Sign in with Google Button"]'))
            google_sign_in_button = self.driver.find_element(By.ID, 'identifierId')
            google_sign_in_button.click()
            sleep(2)
            google_sign_in_button.send_keys(GOOGLE_EMAIL)
            google_sign_in_button.send_keys(Keys.ENTER)
            sleep(5)
            google_password = self.driver.find_element(By.XPATH, '//*[@name="password"]')
            google_password.send_keys(GOOGLE_PASSWORD)
            google_password.send_keys(Keys.ENTER)
            sleep(5)
        except NoSuchElementException:
            print("Failed to find and login with Google")

    def swipe(self):
        # Handle location and notification permissions if they appear
        try:
            allow_location_button = self.driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            allow_location_button.click()
            sleep(1)
        except NoSuchElementException:
            print("Location button not found")

        try:
            notifications_button = self.driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
            notifications_button.click()
            sleep(1)
        except NoSuchElementException:
            print("Notifications button not found")

        # Start swiping right (liking) profiles
        for _ in range(100):  # Adjust this range as per your preference or Tinder's limits
            try:
                like_button = self.driver.find_element(By.XPATH,
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                like_button.click()
                print("Liked profile")
                sleep(1)  # Delay to avoid overwhelming Tinder's server
            except NoSuchElementException:
                print("Like button not found, continuing...")
                continue
            except Exception as e:
                print(f"Error: {str(e)}")
                continue

    def run(self):
        self.login()
        self.swipe()


if __name__ == "__main__":
    app = TinderAutoSwipe()
    app.run()
