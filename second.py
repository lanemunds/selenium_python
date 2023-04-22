from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service_obj = Service('/Users/lanemunds/Downloads/chromedriver')

driver = webdriver.Chrome(service=service_obj)
driver.get('https://espn.com')
driver.maximize_window()
driver.get('https://google.com')
driver.find_element(By.NAME, 'q').send_keys('Ivory Edmunds')
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
driver.find_element(By.CLASS_NAME , 'byrV5b' ).click()
time.sleep(5)
driver.back()
driver.back()
driver.find_element(By.NAME, 'q').send_keys('Finnley Edmunds')
driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
driver.find_element(By.CLASS_NAME , 'byrV5b' ).click()
time.sleep(5)
driver.get('https://lanemunds.github.io/')
driver.find_element(By.ID, '').click()
time.sleep(5)