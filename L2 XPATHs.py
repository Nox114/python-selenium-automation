from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.target.com/')
driver.find_element(By.ID, 'account-sign-in').click()
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()

print('Test case passed')
driver.quit()