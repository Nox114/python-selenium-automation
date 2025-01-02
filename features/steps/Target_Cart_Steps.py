from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then('Verify "Your cart is empty" message shown')
def verify_cart_is_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")
    assert expected_text in actual_text.text, f'Expected text {expected_text} but got {actual_text.text}'
    print ('Test case passed')