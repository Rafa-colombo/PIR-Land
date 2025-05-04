from functions import *

# criação servidor
socket_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endereco = ('',50000)
socket_conexao.bind(endereco)
socket_conexao.listen(2)
print("Servidor criado\nAguardando conexões...")
jogadores = []

try:
    # conexão jogadores
    while len(jogadores) < 2:
        socket_jogador, _ = socket_conexao.accept()

        # Recebe os dados do jogador (já serializados do client)
        dados_recebidos = socket_jogador.recv(4096)  # buffer maior para dados serializados
        jogador_recebido = pickle.loads(dados_recebidos)

        # Atribui o socket ao jogador
        jogador_recebido.socket = socket_jogador  # adiciona conexão ao jogador
        jogadores.append(jogador_recebido)
        print(f"Jogador {jogador_recebido.nome} conectado {_}.")

        # enviar uma mensagem dizendo o ID do jogador
        for i, jogador in enumerate(jogadores):
            msg = int.to_bytes(2,1,'big') + int.to_bytes(i,1,'big')
            jogadores[i].socket.send(msg)


        # Identificação
        nome_servidor = "PIR Land"
        print(f"Servidor '{nome_servidor}' recebeu os jogadores nos IPs:")
        for i, socket_jogador in enumerate(jogadores):
            ip, porta = jogador.socket.getpeername()
            print(f"Jogador {i} - IP: {ip}, Porta: {porta}")


        # PVP
        if (len(jogadores) < 2):
            msg_arena = "Procurando oponente digno..." #  Aguardando jogador 2
            jogadores[0].socket.send(msg_arena.encode('utf-8'))
        else:
            print(f"Iniciando PVP entre jogadores {jogadores[0].nome} vs {jogadores[1].nome}")
            PVP(jogadores[0], jogadores[1])

except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário.")
    socket_conexao.close()
finally:
    # Garantir que o servidor feche todos os sockets corretamente
    print("Fechando servidor e sockets.")
    socket_conexao.close()
    for jogador in jogadores:
        if jogador.socket:
            jogador.socket.close()

