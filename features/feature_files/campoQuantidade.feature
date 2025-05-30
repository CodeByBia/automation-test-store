Funcionalidade: Campo de quantidade

   @campo
    Cenário: Verificar se o campo de quantidade aceita valores decimais
        Dado que o user está na home page
        Quando o user clicar no item
        E clicar no botão de adicionar ao carrinho
        E digitar um número decimal no campo de quantidade
        E clicar em update
        Então o sistema deve corrigir o número para um inteiro
