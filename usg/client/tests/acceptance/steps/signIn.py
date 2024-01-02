from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given("I am on SignIn Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

@when("i fill in email field with usertesting461@gmail.com")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/signin') 

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'email')
    username_input.send_keys('usertesting461@gmail.com')


@when("i fill in password field with UserTesting123")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('UserTesting123')
    
@when("i fill in password field with UserTesting12")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/signin')  # Update with your Django development server URL

    # Example: Use Selenium to fill in form fields
    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('UserTesting12')

@when("I press SignIn button")
def step_impl(context):
    # Example: Use Selenium to click the SignIn button
    SignIn_button = context.browser.find_element(By.CLASS_NAME, 'login-button')
    SignIn_button.click()

@then("i should be on dashboard")
def step_impl(context):
    # Implement code to check if the current page is the Search
    context.browser.get('http://127.0.0.1:8000/dashboard/')
    assert context.browser.current_url == 'http://127.0.0.1:8000/dashboard/'

@then("i should stay on SignIn")
def step_impl(context):
    # Implement code to check if the current page is the SignIn page
    assert context.browser.current_url == 'http://127.0.0.1:8000/signin'



    
    