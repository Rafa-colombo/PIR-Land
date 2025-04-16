from servidor import *
from functions import *


jogador = cadastrar_jogador()

# Menu
print(f"Bem vindo a PIR Land!\nPlayer {jogador.nome}")
prologo(1)
jogador.classe = int(input())

# Escolha de classe
if jogador.classe == 0:  # Mago
    os.system('cls')
    print("Escolheu Mago")
    jogador.vida = 3
    jogador.municao = 2
elif jogador.classe == 1:  # Arqueiro
    os.system('cls')
    print("Escolheu Arqueiro")
    jogador.vida = 4
    jogador.municao = 1
else:                       # Lutador
    os.system('cls')
    print("Escolheu Lutador")
    jogador.vida = 5
    jogador.municao = 0


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
            mago()
            Dia = Dia - 1
        case 3:
            os.system('cls')
            loja()
            Dia = Dia - 1
        case 4:
            os.system('cls')
            B_Arena()
            Dia = Dia - 1
        case 5:
            os.system('cls')
            status(jogador)
        case _:
            os.system('cls')
            print("Opção inválida")





