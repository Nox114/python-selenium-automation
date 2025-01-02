from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on sign in')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "#account-sign-in").click()

@then('Click on nav menu sign in')
def nav_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then('Verify sign in form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1//span")
    assert expected_text in actual_text.text, f'Expected text {expected_text} but got {actual_text.text}'
    print('Test case passed')