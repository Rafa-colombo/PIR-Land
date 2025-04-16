import os

def status(player):
    jogador = player
    print(f"---VIDA = {jogador.vida} / ARMAMENTO = {jogador.municao} / DINHEIROS {jogador.moedas}---\n")


def ler_dialogo(inicio,fim):
    inicio = inicio - 1 
    fim = fim   

    with open("Dialogos.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for i in range(inicio, fim):
            if i < len(linhas):  # evitar erro se passar do tamanho do arquivo
                print(linhas[i].strip())


def comprar_item(opcao, jogador, loja):
    match opcao:
        case 1: # Armadura 1    /
            if jogador.moedas >= 1:
                if loja == ferreiro:
                    jogador.vida += 1
                    jogador.moedas -= 1
                    print(f"Você comprou Armadura 1 (+1 Vida)\n Moedas {jogador.moedas}")
                elif loja == mago:
                    print("Loja fechada por hora")
            else: print("Não possui dinheiro suficiente, caloteiro.")
        case "Armadura 2":
            if jogador.moedas >= 2:
                jogador.vida += 2
                jogador.moedas -= 2
                print("Você comprou Armadura 2 (+2 Vida)")
        case "Armadura 3":
            if jogador.moedas >= 3:
                jogador.vida += 3
                jogador.moedas -= 3
                print("Você comprou Armadura 3 (+3 Vida)")
        case "Arma 1":
            if jogador.moedas >= 1:
                jogador.dano += 1
                jogador.moedas -= 1
                print("Você comprou Arma 1 (+1 Dano)")
        case "Arma 2":
            if jogador.moedas >= 2:
                jogador.dano += 2
                jogador.moedas -= 2
                print("Você comprou Arma 2 (+2 Dano)")
        case "Arma 3":
            if jogador.moedas >= 3:
                jogador.dano += 3
                jogador.moedas -= 3
                print("Você comprou Arma 3 (+3 Dano)")
        case _:
            print("Item inválido.")
            



def prologo(ind):
    index = ind
    if index == 1: ler_dialogo(2,6) # Prólogo
    if index == 2: ler_dialogo(9,10) # Turno da vila


def ferreiro(jogador):
    print("Você escolheu 1, ferreiro")
    ler_dialogo(12,21)
    while True:
        compra = int(input("Escolha: "))
        if compra == 0: break
        os.system('cls')
        comprar_item(compra, jogador, ferreiro)

def mago():
    print("Você escolheu 2, Loja de Magia")


def loja():
    print("Você escolheu 3, Lojista")


def B_Arena():
    print("Você escolheu 3, Black Arena")
