from functions import *

# Cadástro
jogador = cadastrar_jogador()
os.system('cls')


# Vila
status(jogador)
Dia = 4
while Dia >= 0:
    if Dia == 0: # conexão no servidor
        print("Não possui mais turnos\nIndo a arena...") 

        player_mod = importlib.import_module("player")
        Player = getattr(player_mod, "Player")
        jogador = Player("NomeDoJogador")  # ou carregue o estado real dele

        jogador.socket = None  # impede erro de pickle
        socket_jogador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_jogador.connect(("localhost", 50000))
        socket_jogador.send(pickle.dumps(jogador))

        break  # Sai do loop após enviar jogador

    elif Dia == 4: print(f"Player {jogador.nome} você chegou ao centro da vila de PIR\nVoce possui {Dia} ações")
    else: print(f"Player {jogador.nome} você voltou ao centro da vila de PIR\nVocê possui {Dia} ações")
    falas(2)
    acao_dia = int(input("Escolha sua jornada:  ")) 
    match acao_dia:
        case 0:
            os.system('cls')
            falas(0)
            input("Pressione ENTER para continuar...")
            os.system('cls')
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





