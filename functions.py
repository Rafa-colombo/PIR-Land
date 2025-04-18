import os
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

@dataclass
class player:
    nome : str
    flag_mago_clarividencia: bool 
    flag_mago_skill: bool  # Lutador->Vida*1.5 ; Arqueiro->municao*1.5; Mago->Block 1
    nivel: int  # dias sobrevividos
    moedas: int # bolsa de dinheiro
    dano: int # dano inicial padrao
    pot: int
    classe: classe
    inv: List[str]

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
   0: classe(nome = 'Mago', vida = 3, municao = 2),
   1: classe(nome = 'Arqueiro', vida = 4, municao = 1),
   2: classe(nome = 'Lutador', vida = 5, municao = 0)
}


# Cadastro player
def cadastrar_jogador() -> player:
    # Menu
    nome = input("Escolha teu nome jogador: ")
    os.system('cls')
    prologo(1)
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
        inv=[]
    )

# Status player
def status(player):
    jogador = player
    print(f"---VIDA = {jogador.classe.vida} / ARMAMENTO = {jogador.classe.municao} / DINHEIROS {jogador.moedas}---")
    print(f"+CLASSE = {jogador.classe.nome}+\nINV:Pot {jogador.pot}\n{jogador.inv}\n")

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
    print(f"Você comprou {item.nome} (+{item.modificador} {tipo_bonus})")
    print(f"Moedas restantes: {jogador.moedas}")

            


# Ler trechos
def prologo(ind):
    index = ind
    if index == 0: ler_dialogo(1,20)
    if index == 1: ler_dialogo(25,30) # Prólogo
    if index == 2: ler_dialogo(33,34) # Turno da vila

# Loja ferreiro
def ferreiro(jogador):
    print("Você escolheu 1, ferreiro")
    rodando = 0
    while True:
        if rodando == 0: ler_dialogo(36,46) # Ferreiro completo
        else: ler_dialogo(39,46) # Ferreiro catalogo
        rodando = rodando + 1
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        item_escolhido = mapa_itens.get(compra)
        if item_escolhido:
            os.system('cls')
            comprar_item(item_escolhido, jogador, 'ferreiro')
        else:
            os.system('cls')
            print("Item inválido.")
            print(item_escolhido)

# Loja Mago
def mago(jogador):
    print("Você escolheu 2, Loja de Magia")
    ler_dialogo(48,51)

# Loja Lojista
def Guilda(jogador):
    print("Você escolheu 3, Guilda")
    ler_dialogo(59,64)

# Loja Black Market
def B_Market(jogador):
    print("Você escolheu 3, Black Market")
    rodando = 0
    while True:
        if rodando == 0: ler_dialogo(53,57) # B_market completo
        else: ler_dialogo(54,57) # B_market catalogo
        rodando = rodando + 1
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        elif compra == 1:
            os.system('cls')
            print("Calma ladrao, estamos sem luta no momento")
        elif compra == 2:
            item_escolhido = mapa_itens[7]
            os.system('cls')
            comprar_item(item_escolhido, jogador, 'BM')
        else:
            os.system('cls')
            print(compra)
            print("Item inválido.")

