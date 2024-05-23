usuario = {
  "William" : "12345" ,
  "ninguenzinho" : "2222"
}

def verificar_credenciais(usuario, senha):
  print("Verificar se as credenciais sao validas")
  if usuario in usuario and usuarios[usuario] == senha:
    return True
  else:
    raise ValueError("Nome de usuario e senha incorretas")

def login():
  while True:
    try:
      usuario = input("Digite seu nome de usuario (ou digite sair para encerrar): ")
      if usuario == 'sair':
        print("Encerrando o programa.")
        break
      senha = input("Digite sua senha: ")

      if verificar_credenciais(usuario,senha):
        print(f"Login bem sucedido. Bem-Vindo, {usuario}")

        break
    except ValueError as e:
      print(e)
    else:
     print("Voce esta logado com sucesso.")
    finally:
      print("Tentativa de login finalizada")

login()