Funcionalidade: Login no site Automation Test Store
  @login1
  Cenário: Autenticação com credenciais inválidas
    Dado que o usuário esteja na página inicial do site
    E clique em "Login or register"
    E esteja na página de login
    Quando o usuário preencher o campo "Username" com "invalido"
    E preencher o campo "Password" com "1234"
    E clicar no botão "Login"
    Então o usuário deve ver a mensagem "Error: Incorrect login or password provided."