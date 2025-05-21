import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()


url = "D:/Isha/SeleniumPythonClass/StaticWebPage/site-1/index.html"
browser.get(url)

time.sleep(5)


# browser.find_element(By.LINK_TEXT,"Go to Google").click()
browser.find_element(By.PARTIAL_LINK_TEXT,"to").click()

time.sleep(5)

browser.quit()      #close all the windows

time.sleep(5)