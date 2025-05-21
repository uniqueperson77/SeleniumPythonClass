from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.implicitly_wait(15)

driver.get("https://www.abhibus.com/")

driver.maximize_window()

time.sleep(3)

#source
driver.find_element(By.XPATH,"//input[@placeholder='From Station']").send_keys("Hyderabad")
time.sleep(1.5)
driver.find_element(By.XPATH,"//input[@placeholder='From Station']").send_keys(Keys.ENTER)


#destination
driver.find_element(By.XPATH,"//input[@placeholder='To Station']").send_keys("Bangalore")
time.sleep(1.5)
driver.find_element(By.XPATH,"//input[@placeholder='To Station']").send_keys(Keys.ENTER)

# date selection
date_input_xpath = "//input[contains(@placeholder,'Onward Journey Date')]"
driver.find_element(By.XPATH,date_input_xpath).click()

date_xpath = "//span[text()='25']"
driver.find_element(By.XPATH,date_xpath).click()

time.sleep(1.5)

#Search click
driver.find_element(By.XPATH,"//button[contains(text(),'Search')]").click()

time.sleep(10)

Status = driver.find_element(By.XPATH,"//span[contains(text(),'Showing')]").is_displayed()

if Status == True:
    print("successfully navigated to list of buses page.")
else:
    print("Test case Failed. Since, it's not navigated to other page.")

driver.quit()
exit()






















list = driver.find_elements(By.XPATH,"//span[contains(text(),'Showing')]")
if len(list)>0:
    print("successfully navigated.")
else:
    print("unsucessfull")



# slot selection
driver.find_element(By.XPATH,"//a//span[text()='After 11 PM']").click()

time.sleep(3)

# depature time in ascending Order
driver.find_element(By.XPATH,"//a//span[text()='Departure Time']").click()

time.sleep(5)

## give me a count of buses which departs exactly at 11pm

list_dtimes = driver.find_elements(By.XPATH,"//span[@class='departure-time']")

count = 0
for dtime in list_dtimes:
    timee = dtime.text
    if timee == "23:00":
        count = count +1

print(count)

## seat selection button
driver.find_element(By.XPATH,"//button[text()='Select Seats']").click()
time.sleep(2)

# selecting available seat

upper_xpath = "//table[@id='seat-layout-details']"
driver.find_element(By.XPATH,"//button//span[text()='U8']").click()
time.sleep(2)




