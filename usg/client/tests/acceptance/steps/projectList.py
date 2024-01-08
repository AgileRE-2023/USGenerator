from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given("I am on Sign In Page")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

@when("I fill in email field with usertesting461@gmail.com for the field")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/signin') 

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'email')
    username_input.send_keys('usertesting461@gmail.com')

@when("I fill in password field with UserTesting123 for the field")
def step_impl(context):
    # Example: Use Selenium to fill in form fields
    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('UserTesting12')

@when("I press Sign In button")
def step_impl(context):
    # Example: Use Selenium to click the SignIn button
    SignIn_button = context.browser.find_element(By.CLASS_NAME, 'login-button')
    SignIn_button.click()

@then("I should be on dashboard page")
def step_impl(context):
    # Implement code to check if the current page is the Search
    context.browser.get('http://127.0.0.1:8000/dashboard/')
    assert context.browser.current_url == 'http://127.0.0.1:8000/dashboard/'

@when("I press add project button on dashboard page")
def step_impl(context):
    add_project = context.browser.find_element(By.CLASS_NAME, 'add')
    add_project.click()

@then("The User should be on input user story page")
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/inputUserStory'

@when("I press User Story button")
def step_impl(context):
    user_story_button = context.browser.find_element(By.ID, "user_story_button")
    user_story_button.click()

@then("I should be on dashboard again")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/dashboard/')
    assert context.browser.current_url == 'http://127.0.0.1:8000/dashboard/'