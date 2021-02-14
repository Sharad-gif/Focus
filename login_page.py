from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")


driver.find_element_by_xpath('//*[@id="downloads"]/a').click()


time.sleep(4)
driver.refresh()
time.sleep(8)
driver.forward()
time.sleep(2)
driver.close()
