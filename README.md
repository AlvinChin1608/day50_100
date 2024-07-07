# day50_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

----
# Tinder Automation Project
This project automates the Tinder swiping process using Selenium WebDriver in Python. It logs into Tinder, handles permissions, and swipes right on profiles.

## Overview
This automation script uses Selenium to interact with the Tinder website. It performs the following actions:

- __Login:__ Automates the login process using credentials stored securely in environment variables.
- __Permissions:__ Handles location and notification permissions if prompted.
- __Swiping:__ Automatically swipes right on profiles, emulating user interaction.

## Issues
- __Google Login Window:__ There is currently an issue with reliably logging in via Google. The script attempts to interact with the Google login window, but it may encounter issues depending on the timing and layout of the sign-in process.

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (ChromeDriver)

## Setup
- Clone the repository.
- Set up environment variables for Tinder and Google credentials in a .env file.

## Notes
- This project is for educational purposes and should be used responsibly.
- Adjust the script's behaviour and timings based on Tinder's usage guidelines to avoid account limitations.
