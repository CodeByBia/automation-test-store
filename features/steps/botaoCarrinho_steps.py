import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.treinamento_page import *

@given(u'que o user está na página do produto')
def acessar_pag_produto_step(context):
    get_driver().get("https://automationteststore.com/index.php?rt=product/product&path=68_70&product_id=123")

@when(u'todas as opções estiverem desabilitadas')
def verificar_opcoes_desabilitadas_step(context):
    verificar_opcoes_desabilitadas()
           

@then(u'o botão adicionar ao carrinho deve estar desabilitado')
def botao_desabilitado_step(context):
      assert botao_add_to_cart_desabilitado(), "Botão 'Add to Cart' está habilitado: BUG"