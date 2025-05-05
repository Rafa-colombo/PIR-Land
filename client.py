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
        input("\nPressione ENTER para continuar jogador")
        os.system('cls')

        # Conectar ao servidor
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cliente.connect(('192.168.1.105', 50000))  # localhost ou IP do servidor (192.168.1.105)
        jogador.socket = None  # impede erro de pickle

        # Enviar o jogador serializado
        dados = pickle.dumps(jogador)
        socket_cliente.send(dados)

        # Associar o socket local ao jogador após o envio
        jogador.socket = socket_cliente

        print("Conectado ao servidor. Aguardando mensagens...")

        while True:
            msg_recebida = socket_cliente.recv(4096)  # Buffer maior para mensagem
            if not msg_recebida: 
                print("Servidor desconectou.")
                break
            msg_txt = msg_recebida.decode('utf-8')
            print("Mensagem do servidor:", msg_txt)
            if "Sua vez!" in msg_txt:
                acao = input("Digite sua jogada (0 = Defender, 1 = Atacar, 2 = Carregar, 4 = Cura): ")
                os.system('cls')
                print("Aguardando jogada...")
                socket_cliente.send(acao.encode('utf-8')) # Envia a ação de volta para o servidor

        socket_cliente.close()
        break
        

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
            Dia = 0
            





