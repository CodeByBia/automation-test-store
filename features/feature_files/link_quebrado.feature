Feature: Teste de Links Quebrados

  Scenario: Verificar links do footer
    Given que estou na página inicial
    When verifico os links do footer
    Then nenhum link deve estar quebrado
