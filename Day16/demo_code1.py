from selenium import webdriver
from selenium.webdriver.common.by import By

import time
## ChromeDriver installation automated
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

##initializing Chrome app
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome()

driver.maximize_window()

############################

driver.get("D:/Isha/SeleniumPythonClass/StaticWebPage/site-1/index.html")

time.sleep(2)

#Username field
# username_obj = driver.find_element(By.ID,"username")
# username_obj.send_keys("Isha")
# print("{} field was entered.".format("Username"))
# #Email filed
# driver.find_element(By.ID,"email").send_keys("i@gmail.com")
# print("{} field was entered.".format("Email"))
# #Pswd filed
# driver.find_element(By.ID,"password").send_keys("12345678")
# print("{} field was entered.".format("Password"))

list_of_ele = driver.find_elements(By.TAG_NAME,"button")        #list of locators
print("No:of buttons:")
print(len(list_of_ele))  #0,1,2

time.sleep(2)
list_of_ele[1].click()

time.sleep(2)

# driver.switch_to.alert.accept()

time.sleep(10)

driver.close()



