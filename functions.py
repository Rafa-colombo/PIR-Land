import os
import socket
import pickle
import importlib
from dataclasses import dataclass
from typing import List


@dataclass
class item:
    ID: int
    nome: str
    valor: int
    modificador: int

class itens:
    # Armaduras
    Armadura_1 = item(ID=0, nome='Cota de Malha', valor=1, modificador=1)
    Armadura_2 = item(ID=1, nome='Peitoral de Aço', valor=2, modificador=2)
    Armadura_3 = item(ID=2, nome='Armadura Imperial', valor=3, modificador=3)
    
    # Armas
    Arma_1 = item(ID=3, nome='Espada Curta', valor=2, modificador=2)
    Arma_2 = item(ID=4, nome='Espada Longa', valor=3, modificador=3)
    Arma_3 = item(ID=5, nome='Machado de Batalha', valor=4, modificador=4)
    
    # Poções
    Pocao_Vida = item(ID=6, nome='Poção de Vida', valor=2, modificador=1)

@dataclass
class classe:
    nome : str
    vida: int 
    municao: int  # mago mana, pistoleiro municao
    block: int

@dataclass
class player:
    nome : str
    flag_mago_clarividencia: bool 
    flag_mago_skill: bool 
    nivel: int  # dias sobrevividos
    moedas: int # bolsa de dinheiro
    dano: int # dano inicial padrao
    pot: int
    classe: classe
    inv: List[str]
    diario: List[int]

mapa_itens = {
    1: itens.Armadura_1,
    2: itens.Armadura_2,
    3: itens.Armadura_3,
    4: itens.Arma_1,
    5: itens.Arma_2,
    6: itens.Arma_3,
    7: itens.Pocao_Vida,
}

mapa_classes = {
   0: classe(nome = 'Mago', vida = 3, municao = 2, block = 0.5),
   1: classe(nome = 'Arqueiro', vida = 4, municao = 1, block = 0.5),
   2: classe(nome = 'Lutador', vida = 5, municao = 0, block = 0.5)
}



# Cadastro player
def cadastrar_jogador() -> player:
    # Menu
    nome = input("Escolha teu nome jogador: ")
    os.system('cls')
    falas(1)
    index = int(input(f"Faça sua escolha {nome}: "))
    escolhido = mapa_classes.get(index)
    return player(
        nome=nome,
        classe=escolhido,  
        flag_mago_clarividencia=False,
        flag_mago_skill=False,
        nivel=1,
        moedas=10,
        dano=1,
        pot=0,
        inv=[],
        diario=[]
    )



# Status player
def status(player):
    jogador = player
    print(f"STATUS {jogador.nome}\nVida = {jogador.classe.vida} / Armamento = {jogador.classe.municao} / Moedas {jogador.moedas}")
    print(f"CLASSE = {jogador.classe.nome} / Dano de ataque = {jogador.dano}\nINV:Pot {jogador.pot} + {jogador.inv}\n------------------")



# Ler txt dialogo
def ler_dialogo(inicio,fim):
    inicio = inicio - 1 
    fim = fim   

    with open("Dialogos.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for i in range(inicio, fim):
            if i < len(linhas):  
                print(linhas[i].strip())



# Compra de itens
def comprar_item(item, jogador, loja):
    
    print(f"{item.nome} {item.valor} {jogador.nome} {loja}")
    if jogador.moedas < item.valor:
        print("Não possui dinheiro suficiente, caloteiro.")
        return
    if item.nome in jogador.inv and loja != 'BM':
        print(f"Você já possui o item '{item.nome}' no inventário.")
        return

    if loja == 'ferreiro':
        if item.ID in [0, 1, 2]:  # Armaduras
            jogador.classe.vida += item.modificador
            tipo_bonus = "Vida"
            jogador.inv.append(item.nome)
        elif item.ID in [3, 4, 5]:  # Armas
            jogador.dano += item.modificador
            tipo_bonus = "Dano"
            jogador.inv.append(item.nome)
        else:
            print("Tipo de item desconhecido.")
            return
    if loja == 'BM':
        if item.ID  == 6:  # Poção
            jogador.pot += 1
            jogador.inv.append(item.nome) 
            tipo_bonus = "Cura"
        else:
            print("Tipo de item desconhecido.")
            return


    jogador.moedas -= item.valor
    print(f"\nVocê comprou {item.nome} (+{item.modificador} {tipo_bonus})")
    print(f"Moedas restantes: {jogador.moedas}")



# Ler trechos
def falas(ind):
    index = ind
    if index == 0: ler_dialogo(1,21) # Info
    if index == 1: ler_dialogo(23,28) # Prólogo classe
    if index == 2: ler_dialogo(30,32) # Turno da vila
    if index == 3: ler_dialogo(34,44) # Ferreiro full
    if index == 4: ler_dialogo(37,44) # Ferreiro catálogo
    if index == 5: ler_dialogo(46,53) # Mago full
    if index == 6: ler_dialogo(48,53) # Mago catálogo
    if index == 7: ler_dialogo(55,60) # BM full
    if index == 8: ler_dialogo(57,60) # BM catálogo
    if index == 9: ler_dialogo(62,68) # Guilda full
    if index == 10: ler_dialogo(64,68) # Guilda catálogo
    if index == 11: return ler_dialogo(70,71) # Entrada arena PVP
 
    


# Loja ferreiro
def ferreiro(jogador):
    print("Você escolheu 1, ferreiro")
    rodando = 0
    while True:
        if rodando == 0: falas(3) # Ferreiro completo
        else: falas(4) # Ferreiro catalogo
        rodando = rodando + 1
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        item_escolhido = mapa_itens.get(compra)
        if item_escolhido:
            comprar_item(item_escolhido, jogador, 'ferreiro')
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        else:
            print("Item inválido.")
            print(item_escolhido)
            input("\nPressione ENTER para continuar...")
            os.system('cls')



# Loja Mago
def mago(jogador):
    print("Você escolheu 2, Loja de Magia")
    rodando = 0
    while True:
        if rodando == 0: falas(5) # Mago completo
        else: falas(6) # Mago catalogo
        rodando = rodando + 1
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        elif compra == 1:
            if jogador.flag_mago_clarividencia == 1: print("Você já possui essa habilidade")
            else: 
                jogador.flag_mago_clarividencia = 1
                print(f"Acaba de adquirir pergaminho da clarividencia, use com sabedoria {jogador.nome}")
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        elif compra == 2:
            if jogador.flag_mago_skill == 1: print("Você já possui a habilidade")
            else: 
                if jogador.moedas < 5: print("Não possui moedas suficientes")
                else:
                    jogador.flag_mago_skill = 1
                    print(f"Acaba de adquirir sua habilidadede de classe {jogador.nome}")
                    if jogador.classe.nome == 'Mago': jogador.classe.block = 1
                    elif jogador.classe.nome == 'Arqueiro': jogador.classe.municao *= 2
                    else: jogador.classe.vida *= 2
                    jogador.moedas -= 5
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        else:
            print(compra)
            print("Item inválido.")
            input("\nPressione ENTER para continuar...")
            os.system('cls')



#  Guilda
def Guilda(jogador):
    print("Você escolheu 3, Guilda")
    rodando = 0
    while True:
        if rodando == 0: falas(7) # Guilda completo
        else: falas(8) # Guilda introdução
        rodando = rodando + 1
        escolha = int(input(f"Escolha: "))
        if escolha == 0: 
            os.system('cls') 
            return
        elif escolha in [1, 2, 3]:
            # Verifica se missão já foi feita
            if escolha in jogador.diario:
                print("Você já completou essa missão!")
                input("\nPressione ENTER para continuar...")
                os.system('cls')
                continue
            if escolha in [1, 2]:
                jogador.moedas += 3
                mensagem = "resgatou o gato" if escolha == 1 else "pegou 2 coelhos"
                print(f"Missão bem sucedida, {jogador.nome} {mensagem} e ganhou 3 moedas\nBolsa({jogador.moedas})")
            elif escolha == 3:
                if jogador.classe.vida > 1:
                    jogador.moedas += 5
                    jogador.classe.vida -= 1
                    print(f"Após um encontro com o mestre dos magos, o real vilão, {jogador.nome} ganhou 5 moedas\nVida restante = {jogador.classe.vida}")
                else:
                    print("Você não possui vida suficiente ladrão")
                    input("\nPressione ENTER para continuar...")
                    os.system('cls')
                    continue

            # Registra a missão no diário
            jogador.diario.append(escolha)
            input("\nPressione ENTER para continuar...")
            os.system('cls')
            return
        else:
            os.system('cls')
            print(escolha)
            print("Escolha inválida.")



# Loja Black Market
def B_Market(jogador):
    print("Você escolheu 3, Black Market")
    rodando = 0
    while True:
        if rodando == 0: falas(9) # B_market completo
        else: falas(10) # B_market catalogo
        rodando = rodando + 1
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        elif compra == 1:
            if jogador.classe.vida > 2:
                jogador.moedas = jogador.moedas * 2
                jogador.classe.vida = jogador.classe.vida - 2
                print(f"\nApós uma ardua batalha, {jogador.nome} ganhou 2x sua aposta\nVida restante = {jogador.classe.vida}")
            else: print("Você não possui vida suficiente ladrão")
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        elif compra == 2:
            item_escolhido = mapa_itens[7]
            comprar_item(item_escolhido, jogador, 'BM')
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        elif compra == 3:
            print(f"\nVocê comprou munição (+2) para {jogador.classe}\nMunição: {jogador.municao}")
            jogador.municao += 2
            input("\nPressione ENTER para continuar...")
            os.system('cls')
        else:
            print(compra)
            print("Item inválido.")
            input("\nPressione ENTER para continuar...")
            os.system('cls')



def PVP(jogador1, jogador2):
    # Inic
    msg = falas(11)
    jogadores = [jogador1, jogador2]
    if msg:
        for linha in msg:
            for jogador in jogadores:
                jogador.socket.send((linha + "\n").encode())
    else: print("Nenhuma mensagem retornada.")
    batalha = True
    while batalha:

        # Recebendo ações dos jogadores
        jogador1.socket.send(b"\nSua vez! Digite sua ação (0 = Defender, 1 = Atacar, 2 = Carregar): ")
        acao1 = int(jogador1.socket.recv(1024).decode())

        jogador2.socket.send(b"\nSua vez! Digite sua ação (0 = Defender, 1 = Atacar, 2 = Carregar): ")
        acao2 = int(jogador2.socket.recv(1024).decode())

        mensagens = []

        # Jogador 1 
        if acao1 == 2:      # Carregamento jogador 1
            jogador1.municao += 1
            mensagens.append("Jogador 1 carregou a arma!")
        elif acao1 == 1:        # Ataque jogador 1
            if jogador1.municao > 0:
                jogador1.municao -= 1
                if acao2 == 0:      # Defesa jogador 2
                    dano = jogador1.dano * jogador2.block
                    jogador2.classe.vida -= dano
                    mensagens.append(f"Jogador 2 defendeu! Dano reduzido para {dano:.1f}")
                else:
                    jogador2.classe.vida -= jogador1.dano
                    mensagens.append(f"Jogador 2 foi atingido! Sofreu {jogador1.dano} de dano.")
            else:
                mensagens.append("Jogador 1 tentou atacar, mas está sem munição!")
        else:
            mensagens.append("Ação inválida. Jogador 1 perdeu a vez!")

        # Jogador 2 
        if acao2 == 2:         # Carregamento jogador 2
            jogador2.municao += 1
            mensagens.append("Jogador 2 carregou a arma!")
        elif acao2 == 1:        # Ataque jogador 2
            if jogador2.municao > 0:
                jogador2.municao -= 1
                if acao1 == 0:      # Defesa jogador 1
                    dano = jogador2.dano * jogador1.block
                    jogador1.classe.vida -= dano
                    mensagens.append(f"Jogador 1 defendeu! Dano reduzido para {dano:.1f}")
                else:
                    jogador1.classe.vida -= jogador2.dano
                    mensagens.append(f"Jogador 1 foi atingido! Sofreu {jogador2.dano} de dano.")
            else:
                mensagens.append("Jogador 2 tentou atacar, mas está sem munição!")
        else:
            mensagens.append("Ação inválida. Jogador 2 perdeu a vez!")

        # Enviar mensagens para ambos os jogadores
        for msg in mensagens:
            jogador1.socket.send((msg + "\n").encode())
            jogador2.socket.send((msg + "\n").encode())

        # Fim da batalha
        if jogador1.classe.vida <= 0 or jogador2.classe.vida <= 0:
            print("Mensagem do servidor:\n--- Fim da Batalha ---")
            resultado = "\n--- Fim da Batalha ---\n"
            if jogador1.classe.vida <= 0 and jogador2.classe.vida <= 0:
                print("Empate! Ambos caíram ao mesmo tempo.")
                resultado += "Empate! Ambos caíram ao mesmo tempo."
            elif jogador1.classe.vida <= 0:
                print("Jogador 2 venceu!")
                resultado += "Jogador 2 venceu!"
            else:
                print("Jogador 1 venceu!")
                resultado += "Jogador 1 venceu!"
            jogador1.socket.send(resultado.encode())
            jogador2.socket.send(resultado.encode())
            batalha = False
