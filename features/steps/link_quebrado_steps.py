from behave import when, then
from features.pages.link_quebrado_page import LinkQuebradoPage

@when('verifico os links do footer')
def step_impl(context):
    context.link_page = LinkQuebradoPage(context.driver)
    context.links = context.link_page.get_all_links()

@then('nenhum link está quebrado')
def step_impl(context):
    broken_links = []
    for link in context.links:
        url = link.get_attribute('href')
        if url and url.startswith('http'):
            status = context.link_page.verificar_status_link(url)
            if status == 404:
                broken_links.append(url)
    assert len(broken_links) == 0