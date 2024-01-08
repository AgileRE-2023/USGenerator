from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given("As a logged user")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

    context.browser.get('http://127.0.0.1:8000/signin') 

    # Example: Use Selenium to fill in form fields
    username_input = context.browser.find_element(By.ID, 'email')
    username_input.send_keys('usertesting461@gmail.com')
    password_input = context.browser.find_element(By.ID, 'password')
    password_input.send_keys('UserTesting123')
    SignIn_button = context.browser.find_element(By.CLASS_NAME, 'login-button')
    SignIn_button.click()
@when("I press profile icon")
def step_impl(context):
    profile_button = context.browser.find_element(By.CLASS_NAME, 'profile-page')
    profile_button.click()
@then("I should see user profile page")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/user-profile')
    assert context.browser.current_url == 'http://127.0.0.1:8000/user-profile'
@when("I press edit profile button")
def step_impl(context):
    edit_button = context.browser.find_element(By.CLASS_NAME, 'edit-button')
    edit_button.click()
@then("I should see edit profile page")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/edit-profile')
    assert context.browser.current_url == 'http://127.0.0.1:8000/edit-profile'
@when("I fill all field in edit profile form with new data")
def step_impl(context):
    full_name  = context.browser.find_element(By.ID, 'name')
    full_name.send_keys("Maul")
    email = context.browser.find_element(By.ID, 'email')
    email.send_keys("usertesting461@gmail.com")
    phone = context.browser.find_element(By.ID, 'phone')
    phone.send_keys("082111633069")
@when("I press save change button")
def step_impl(context):
    save_button = context.browser.find_element(By.CLASS_NAME, 'edit-button')
    save_button.click()
@then("I should see user profile page again")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/user-profile')
    assert context.browser.current_url == 'http://127.0.0.1:8000/user-profile'