from behave import given
from features.pages.base_page import acessar_site

@given('que estou na página inicial')
def step_impl(context):
    acessar_site()