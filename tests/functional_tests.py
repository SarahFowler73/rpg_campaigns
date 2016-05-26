# test selenium

from selenium import webdriver

BASE_URL = 'localhost:8888'

driver = webdriver.Chrome()
driver.get(BASE_URL + '/registration')
driver.quit()
