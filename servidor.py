from functions import *

# criação servidor
socket_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
endereco = ('',50000)
socket_conexao.bind(endereco)
socket_conexao.listen(2)
print("Servidor aguardando conexões...")
jogadores = []

# conexão jogadores
while len(jogadores) < 2:
        socket_jogador, _ = socket_conexao.accept()
        print(f"Jogador conectado: {_}")

        # Recebe os dados do jogador (já serializados do client)
        dados_recebidos = socket_jogador.recv(4096)  # buffer maior para dados serializados
        jogador_recebido = pickle.loads(dados_recebidos)

        # Atribui o socket ao jogador
        jogador_recebido.socket = socket_jogador  # adiciona conexão ao jogador
        jogadores.append(jogador_recebido)
        print(f"Jogador {jogador_recebido.nome} conectado.")

# enviar uma mensagem dizendo o ID do jogador
for i in enumerate(jogadores):
    msg = int.to_bytes(2,1,'big') + int.to_bytes(i,1,'big')
    jogadores[i].socket.send(msg)


# Identificação
nome_servidor = "PIR Land"
print(f"Servidor '{nome_servidor}' recebeu os jogadores nos IPs:")
for i, socket_jogador in enumerate(jogadores):
    ip, porta = socket_jogador.getpeername()
    print(f"Jogador {i} - IP: {ip}, Porta: {porta}")


# PVP
print(f"Iniciando PVP entra jogadores {jogadores[0].nome} vs {jogadores[1].nome}")
PVP(jogadores[0], jogadores[1])
