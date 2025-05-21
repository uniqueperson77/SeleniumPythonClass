import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()


url = "D:/Isha/SeleniumPythonClass/StaticWebPage/site-1/index.html"
browser.get(url)

time.sleep(2)

male_radio_button_xpath = "//input[@value='male']"
browser.find_element(By.XPATH,male_radio_button_xpath).click()

time.sleep(6000)


#findlements - click all the radio button in sequence with time gap of 3 seconds