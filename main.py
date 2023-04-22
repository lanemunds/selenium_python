from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://espn.com')
driver.get('https://facebook.com')
driver.maximize_window()
driver.get('https://google.com')
driver.find_element(By.NAME, 'Q').send_keys('Ivory Edmunds')
driver.back()
driver.close()