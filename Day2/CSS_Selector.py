from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # To auto-download Chromedriver

# Create a Service object (Only needed if you specify the driver path)
service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.facebook.com/")

driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("sadyags@gmail.com")

driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("sady@1201")
