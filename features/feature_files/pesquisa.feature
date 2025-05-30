Funcionalidade: Pesquisar produtos
@pesquisa
  Cenário: Teste de pesquisa de produtos
    Dado que o usuário está na página inicial da loja
    Quando ele pesquisa por "shampoo"
    Então os resultados da pesquisa devem conter o termo "shampoo"