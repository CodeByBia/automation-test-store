Funcionalidade: Teste de Login Inválido

  Cenário: Login com credenciais inválidas
    Dado que estou na página de login
    Quando preencho com usuário "UsuarioSoftex" e senha "Senha123"
    E clico no botão de login
    Então devo ver a mensagem de erro "Error: Incorrect login or password provided."
