from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given('I am on SignUp Page')
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

@when('I fill all field in SignUp Form with new username')
def step_impl(context):
    context.SignUn_data = {'fullName': 'User', 'email':'usertesting461@gmail.com', 'telp': '082111533948','password': 'UserTesting123','confirm_password':'UserTesting123'}
    context.browser.get('http://127.0.0.1:8000/regist')

    # Replace these values with actual form field names and desired username
    username_input = context.browser.find_element(By.ID, 'name')
    email_input = context.browser.find_element(By.ID, 'email')
    telp_input = context.browser.find_element(By.ID, 'phone')
    password_input = context.browser.find_element(By.ID, 'password')
    confirm_password_input = context.browser.find_element(By.ID, 'passwordConfirm')

    username_input.send_keys(context.SignUn_data['name'])
    email_input.send_keys(context.SignUn_data['email'])
    telp_input.send_keys(context.SignUn_data['phone'])
    password_input.send_keys(context.SignUn_data['password'])
    confirm_password_input.send_keys(context.SignUn_data['passwordConfirm'])


@when('I fill in SignUp Form with incomplete data')
def step_impl(context):
    # Simulate incomplete data by leaving some fields blank
    context.SignUn_data = {'fullName': 'User', 'email':'', 'telp': '082111533948','password': 'UserTesting123','confirm_password':'UserTesting123'}
    context.browser.get('http://127.0.0.1:8000/regist')

    # Replace these values with actual form field names and desired username
    username_input = context.browser.find_element(By.ID, 'name')
    email_input = context.browser.find_element(By.ID, 'email')
    telp_input = context.browser.find_element(By.ID, 'phone')
    password_input = context.browser.find_element(By.ID, 'password')
    confirm_password_input = context.browser.find_element(By.ID, 'passwordConfirm')

    username_input.send_keys(context.SignUn_data['name'])
    email_input.send_keys(context.SignUn_data['email'])
    telp_input.send_keys(context.SignUn_data['phone'])
    password_input.send_keys(context.SignUn_data['password'])
    confirm_password_input.send_keys(context.SignUn_data['passwordConfirm'])



@when('I press SignUp button')
def step_impl(context):
    # Replace 'signup_button' with the actual name or identifier of your signup button
    signup_button = context.browser.find_element(By.ID, 'signup_button')
    signup_button.click()

@then('I should be on SignIn')
def step_impl(context):
    # Implement the assertion for being on the SignIn page
    assert context.browser.current_url == 'http://127.0.0.1:8000/signin', f"Expected SignIn page, but got {context.browser.current_url}"

@then('I should stay on SignUp ')
def step_impl(context):
    # Implement the assertion for being on the SignUp page
    assert context.browser.current_url == 'http://127.0.0.1:8000/regist', f"Expected signup page, but got {context.browser.current_url}"
