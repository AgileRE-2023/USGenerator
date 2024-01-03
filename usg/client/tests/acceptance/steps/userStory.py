from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given("i am on Dashboard Page")
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

@when("i press add project button")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

    context.browser.get('http://127.0.0.1:8000/dashboard/') 
    # Example: Use Selenium to click the SignIn button
    add_project = context.browser.find_element(By.ID, 'add')
    add_project.click()

@then("i should be on input user story page")
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/inputUserStory'

@when("i fill all field in User Story Form with title and apps desc")
def step_impl(context):
    context.client = Client()
    context.browser = webdriver.Chrome()

    context.browser.get('http://127.0.0.1:8000/inputUserStory') 
    title_input = context.browser.find_element(By.ID, 'ProjectTitle')
    title_input.send_keys('Facebook')
    desc_input = context.browser.find_element(By.ID, 'inputParagraf')
    desc_input.send_keys('Facebook is a dynamic social media platform designed for fostering connections and sharing experiences.  Instagram provides a space where individuals can engage with one another through various features for users seeking meaningful interactions. You can post captivating photos and videos for showcasing moments that matter to you. The platform facilitates seamless communication, allowing you to connect with friends, family, and even new acquaintances, so that your memories endure.')

@when("i press generate button")
def step_impl(context):
    # Instead of directly clicking the button, submit the form through Selenium
    form = context.browser.find_element(By.TAG_NAME, 'form')
    form.submit()
    # print(context.browser.current_url)

@then("i should see user story list")
def step_impl(context):
    # context.browser.get('http://127.0.0.1:8000/postInputStory')
    assert context.browser.current_url == 'http://127.0.0.1:8000/postInputStory/'
    # assert context.browser.find_element(By.CLASS_NAME, 'output-user-story')
