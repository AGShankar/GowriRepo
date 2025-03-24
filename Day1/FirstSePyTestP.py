import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from webdriver_manager.chrome import ChromeDriverManager  # To auto-download Chromedriver

# Create a Service object (Only needed if you specify the driver path)
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.orangehrm.com/")

time.sleep(10)

title=driver.title
print(title)

if title == "Human Resources Management Software | OrangeHRM":
    print("Title matched!")
else:
    print("Title did not match!")

# Print title


# Close the browser
driver.quit()
