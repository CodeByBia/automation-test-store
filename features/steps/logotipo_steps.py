import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.treinamento_page import *


@given(u'que o user está em uma página diferente da home page')
def acessar_site_step(context):
    get_driver().get("https://automationteststore.com/index.php?rt=product/category&path=68")
    

@when(u'a logo é clicada')
def clicar_logo_step(context):
    clicar_logo()
    time.sleep(4)

    
@then(u'o user deve ser redirecionado para a home page')
def direcionar_para_home_step(context):
    atual_url = get_driver().current_url
    url_esperada = "https://automationteststore.com/"
    assert atual_url == url_esperada, f"Esperado: {url_esperada}, mas foi: {atual_url}"
    time.sleep(3)


