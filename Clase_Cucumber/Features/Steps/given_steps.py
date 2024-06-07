from behave import given
from lib.pages.home_page import HomePage
from selenium import webdriver

@given('I open Google homepage')
def open_google_homepage(context):
    context.driver = webdriver.Chrome()
    context.home_page = HomePage(context.driver)
    context.home_page.open_google()