from features.pages.base_page import *

CAMPO_PESQUISA = "#filter_keyword"
BOTAO_PESQUISA = ".button-in-search"
MENSAGEM_NENHUM_RESULTADO = ".contentpanel"

def pesquisar_termo(termo):
    find_element(CAMPO_PESQUISA).send_keys(termo)
    find_element(BOTAO_PESQUISA).click()

def verificar_mensagem():
    return get_element_text(MENSAGEM_NENHUM_RESULTADO)