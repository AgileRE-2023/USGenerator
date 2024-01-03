from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.test import Client

@given("i am on User Stories Page")
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

    add_project = context.browser.find_element(By.ID, 'add')
    add_project.click()

    assert context.browser.current_url == 'http://127.0.0.1:8000/inputUserStory'

    title_input = context.browser.find_element(By.ID, 'ProjectTitle')
    title_input.send_keys('Facebook')
    desc_input = context.browser.find_element(By.ID, 'inputParagraf')
    desc_input.send_keys('Facebook is a dynamic social media platform designed for fostering connections and sharing experiences.  Instagram provides a space where individuals can engage with one another through various features for users seeking meaningful interactions. You can post captivating photos and videos for showcasing moments that matter to you. The platform facilitates seamless communication, allowing you to connect with friends, family, and even new acquaintances, so that your memories endure.')

    form = context.browser.find_element(By.TAG_NAME, 'form')
    form.submit()

    assert context.browser.current_url == 'http://127.0.0.1:8000/postInputStory/'
@when("I press one of an user stories")
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/postInputStory/')
    story_value = context.browser.find_element(By.CLASS_NAME, 'numof-container 0')
    story_value.click()
@then("i should be on input user story Scenario")
def step_impl(context):
    assert context.browser.current_url == 'http://127.0.0.1:8000/input-scenario/0'

@when("i fill all field in User Story Scenario Form with title and apps desc")
def step_impl(context):
    title_input = context.browser.find_element(By.ID, 'ScenarioTitle')
    title_input.send_keys('Login Success')
    desc_input = context.browser.find_element(By.ID, 'inputParagraf')
    desc_input.send_keys("With a registered user having valid credentials. User open the application. They will encounter the login screen. The user inputs their registered username and password. The system will verifies the provided information against the database. Upon successful authentication, the user will gains access to the application's main interface, enabling seamless exploration of its functionalities.")

@when("i press generate button in user scenario story")
def step_impl(context):
    # Instead of directly clicking the button, submit the form through Selenium
    form = context.browser.find_element(By.TAG_NAME, 'form')
    form.submit()
    # print(context.browser.current_url)

@then("i should see user story Scenario list")
def step_impl(context):
    # context.browser.get('http://127.0.0.1:8000/postInputStory')
    assert context.browser.current_url == 'http://127.0.0.1:8000/output-scenario/0'
    # assert context.browser.find_element(By.CLASS_NAME, 'output-user-story')