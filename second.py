from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service('/Users/lanemunds/Downloads/chromedriver')

driver = webdriver.Chrome(service=service_obj)

driver.get('https://espn.com')
driver.get('https://cougarboard.com')
driver.maximize_window()
driver.back()
print(driver.title)
print(driver.current_url)
driver.get('https://google.com')
driver.find_element(By.NAME, 'Q').send_keys('Ivory Edmunds')

driver.close()