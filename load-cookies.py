from selenium import webdriver
import time
import json

# Create an instance of the desired browser driver
driver = webdriver.Firefox()

# Load the URL
driver.get("https://outlook.com")

input("Press enter to load the cookies")

# Read the cookies from the file
with open("cookies.json", "r") as f:
    cookies = json.load(f)

# Add the cookies to the browser
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

# Wait for the user to press enter
input("Press enter to close the browser.")

# Close the browser
driver.quit()
