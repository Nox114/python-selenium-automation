from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#Amazon logo, search by Class-Name, "a-icon a-icon-logo"
#Email, search by Name, "name=email"
#Continue, search by id, "Continue"
#Conditions of Use, search by Linktext, "Conditions of Use"
#Privacy Notice, search by tag and attribute, "a" "href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088'
#Need Help, search by attribute, "class=a-expander-prompt'
#Forgot your password link, search by id, "auth-fpp-link-bottom"
#Other issues with Sign-In link, search by id, "ap-other-signin-issues-link"
#Create your Amazon account button, search by id, "createAccountSubmit"

driver.get('https://www.target.com/')
driver.find_element(By.ID, 'account-sign-in').click()
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()

print('Test case passed')
driver.quit()