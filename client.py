from functions import *


jogador = cadastrar_jogador()
os.system('cls')

# Vila
Dia = 4
while Dia >= 0:
    if Dia == 0: 
        print("Não possui mais turnos\nIndo a arena...")  
        break #implementa goto arena
    elif Dia == 4: print(f"Player {jogador.nome} você chegou ao centro da vila de PIR\nVoce possui {Dia} ações")
    else: print(f"Player {jogador.nome} você voltou ao centro da vila de PIR\nVoce possui {Dia} ações")
    prologo(2)
    acao_dia = int(input("Escolha sua jornada:  ")) 
    match acao_dia:
        case 1:
            os.system('cls')
            ferreiro(jogador)
            Dia = Dia - 1
        case 2:
            os.system('cls')
            mago(jogador)
            Dia = Dia - 1
        case 3:
            os.system('cls')
            B_Market(jogador)
            Dia = Dia - 1
        case 4:
            os.system('cls')
            Guilda(jogador)
            Dia = Dia - 1
        case 5:
            os.system('cls')
            status(jogador)
        case _:
            os.system('cls')
            print("Opção inválida")
            break





