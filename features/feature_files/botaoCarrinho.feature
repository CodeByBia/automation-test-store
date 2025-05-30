Funcionalidade: Botão carrinho

    @botao
    Cenário: Verificar botão desabilitado
        Dado que o user está na página do produto
        Quando todas as opções estiverem desabilitadas
        Então o botão adicionar ao carrinho deve estar desabilitado