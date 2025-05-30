Feature: Teste de Login Inválido
  Scenario: Login com credenciais inválidas
    Given que estou na página de login
    When preencho com usuário "UsuarioSoftex" e senha "Senha123"
    And clico no botão de login
    Then devo ver a mensagem de erro "Error: Incorrect login or password provided."
