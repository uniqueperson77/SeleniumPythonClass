from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.maximize_window()

url = "D:/Isha/SeleniumPythonClass/StaticWebPage/site-1/index.html"
driver.get(url)

time.sleep(2.5)

# driver.find_element(By.NAME,"agree").click()

agree_checkbox_xpath = "//input[@id='agree']"
obj = driver.find_element(By.XPATH,agree_checkbox_xpath)        #element is agree checkbox
obj.click()     #clicking an element

time.sleep(3)

disagree_checkbox_xpath = "//input[@id='disagree']"
disagree_obj = driver.find_element(By.XPATH,disagree_checkbox_xpath)        #element is disagree checkbox
disagree_obj.click()     #clicking an element


time.sleep(5)

driver.close()


