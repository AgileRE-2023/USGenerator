from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

use_step_matcher("re")

@given("I am on login page")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    #login page
    context.selenium.get(f'{context.host}')

@when("I fill in 'Email' with 'usertesting461@gmail.com'")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    #fill login information
    context.selenium.find_element_by_id('email').send_keys('darfito.jkt2003@gmail.com')
@when("I fill in 'Password' with 'UserTesting123'")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    #fill login information
    context.selenium.find_element_by_id('password').send_keys('GadinG564')

@when("I press 'Login Button'")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    #fill login information
    context.selenium.find_element_by_class_name('login-button').click()

@then("I should see 'Project List Page")
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    assert context.selenium.title == ' Dashboard '

