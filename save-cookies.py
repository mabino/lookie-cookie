from selenium import webdriver
import time
import json

# Create an instance of the desired browser driver
driver = webdriver.Firefox()

# Load the URL
driver.get("https://outlook.com")

# Wait for the user to complete authentication
input("Press enter when you have completed authentication.")

# Store the cookies
cookies = driver.get_cookies()

# Write the cookies to a file in JSON format
with open("cookies.json", "w") as f:
    json.dump(cookies, f)

# Keep the browser open until the user closes it
input("Press enter to close the browser.")

# Close the browser
driver.quit()
