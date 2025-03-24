from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv = Service("D:\Drivers\chromedriver-win64\chromedriver.exe")
driver= webdriver.Chrome(service= serv)

#driver.get("https://demo.nopcommerce.com/")
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()



# driver.find_element(By.ID, "small-searchterms").send_keys("laptops")
#
# driver.find_element(By.TAG_NAME, "button").click()


#driver.find_element(By.PARTIAL_LINK_TEXT, "Log").click()

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))


