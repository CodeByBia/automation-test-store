Feature: Pesquisa com Termo Inexistente
    Scenario: Pesquisar por termo inexistente
        Given que estou na página inicial
        When pesquiso pelo termo "SOFTEX-123"
        Then devo ver a mensagem "Products meeting the search criteria"