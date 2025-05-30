from behave import when, then
from features.pages.teste_link_quebrado import *

@when('verifico os links do footer')
def step_impl(context):
    context.links = get_all_links()

@then('nenhum link deve estar quebrado')
def step_impl(context):
    broken_links = []
    for link in context.links:
        url = link.get_attribute('href')
        if url and url.startswith('http'):
            status = verificar_status_link(url)
            print(f"Verificando {url} - Status: {status}")
            if status == 404:
                broken_links.append(url)
    assert len(broken_links) == 0, f"Links quebrados encontrados: {broken_links}"
