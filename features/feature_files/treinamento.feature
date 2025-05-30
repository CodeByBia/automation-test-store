Funcionalidade: Login no site Automation Test Store
@login
  Cenário: Autenticação bem-sucedida com credenciais válidas
    Dado que o usuário esteja na página inicial do site
    E clique em "Login or register"
    E esteja na página de login
    Quando o usuário preencher o campo "Username" com "usuario_valido"
    E preencher o campo "Password" com "senha_valida"
    E clicar no botão "Login"
    Então o usuário deve ver a mensagem "Welcome back"



