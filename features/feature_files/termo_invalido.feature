Funcionalidade: Pesquisa com Termo Inexistente
  @termo
  Cenário: Pesquisar por "SOFTEX-123"
    Dado que estou na página inicial
    Quando pesquiso pelo termo "SOFTEX-123"
    Então devo ver a mensagem "Products meeting the search criteria"