from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()        #this will initialize chrome browser
# browser = webdriver.Edge()        #this will initialize Edge browser

browser.maximize_window()

website_url = "https://www.amazon.in/"

browser.get(website_url)

time.sleep(50)

mobile_xpath = '//*[@id="nav-xshop"]/ul/li[6]/div/a'

browser.find_element(By.XPATH,mobile_xpath).click()

time.sleep(10)
