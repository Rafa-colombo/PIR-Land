import os
from dataclasses import dataclass

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

mapa_itens = {
    1: itens.Armadura_1,
    2: itens.Armadura_2,
    3: itens.Armadura_3,
    4: itens.Arma_1,
    5: itens.Arma_2,
    6: itens.Arma_3,
    7: itens.Pocao_Vida,
}


def status(player):
    jogador = player
    print(f"---VIDA = {jogador.vida} / ARMAMENTO = {jogador.municao} / DINHEIROS {jogador.moedas} / POT {jogador.pot}---\n")


def ler_dialogo(inicio,fim):
    inicio = inicio - 1 
    fim = fim   

    with open("Dialogos.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for i in range(inicio, fim):
            if i < len(linhas):  
                print(linhas[i].strip())


def comprar_item(item, jogador, loja):
    if loja != ferreiro:
        print("Loja fechada por hora")
        return
    print(f"{item} {jogador.nome} {loja}")
    if jogador.moedas < item.valor:
        print("Não possui dinheiro suficiente, caloteiro.")
        return

    if item.ID in [0, 1, 2]:  # Armaduras
        jogador.vida += item.modificador
        tipo_bonus = "Vida"
    elif item.ID in [3, 4, 5]:  # Armas
        jogador.dano += item.modificador
        tipo_bonus = "Dano"
    elif item.ID == 6:  # Poção
        jogador.pot += item.modificador
        tipo_bonus = "Cura"
    else:
        print("Tipo de item desconhecido.")
        return


    jogador.moedas -= item.valor
    print(f"Você comprou {item.nome} (+{item.modificador} {tipo_bonus})")
    print(f"Moedas restantes: {jogador.moedas}")

            



def prologo(ind):
    index = ind
    if index == 1: ler_dialogo(2,6) # Prólogo
    if index == 2: ler_dialogo(9,10) # Turno da vila


def ferreiro(jogador):
    print("Você escolheu 1, ferreiro")
    while True:
        ler_dialogo(12,22)
        compra = int(input(f"Escolha (possui {jogador.moedas} de dinheiro): "))
        if compra == 0: 
            os.system('cls') 
            return
        item_escolhido = mapa_itens.get(compra)
        print(item_escolhido)
        if item_escolhido:
            os.system('cls')
            comprar_item(item_escolhido, jogador, ferreiro)
        else:
            os.system('cls')
            print("Item inválido.")
            print(item_escolhido)


def mago():
    print("Você escolheu 2, Loja de Magia")


def loja():
    print("Você escolheu 3, Lojista")


def B_Arena():
    print("Você escolheu 3, Black Arena")
