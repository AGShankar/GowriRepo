from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("D:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()

#self
# Text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/self::a").text
# print(Text_msg)

#parent
# Text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/parent::td").text
# print(Text_msg)

#child
# Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/child::td")
# print(len(Text_msgs))

#ancestor

# Text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr").text
# print(Text_msg)  # Max Healthcare Inst. A 437.90 456.50 + 4.25
#
# #decendant
# Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/descendant::*")
# print("Number of descendant Nodes",len(Text_msgs))
#

#following
Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/following::*")
print("Number of following Nodes",len(Text_msgs))

# following-siblings

Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/following-sibling::tr")
print("Number of following Sibling Nodes",len(Text_msgs))

# preceding

Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/preceding::*")
print("Number of preceding Nodes",len(Text_msgs))

# preceding-siblings

Text_msgs=driver.find_elements(By.XPATH,"//a[contains(text(),'Max Healthcare Inst.')]/ancestor::tr/preceding-sibling::*")
print("Number of preceding Sibling Nodes",len(Text_msgs))

driver.close()
