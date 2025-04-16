from dataclasses import dataclass
import os

@dataclass
class player:
    nome : str
    vida: int 
    municao: int  # mago mana, pistoleiro municao
    classe: int  # 0 = Mago; 1 = Arqueiro; 2 = Lutador
    flag_mago_clarividencia: bool 
    flag_mago_skill: bool  # Lutador->Vida*1.5 ; Arqueiro->municao*1.5; Mago->Block 1
    nivel: int  # dias sobrevividos
    moedas: int # bolsa de dinheiro
    dano: int # dano inicial padrao


# Cadastro player
def cadastrar_jogador() -> player:
    return player(
        nome=nome,
        vida=0,  
        municao=0,
        classe=-1,  
        flag_mago_clarividencia=False,
        flag_mago_skill=False,
        nivel=1,
        moedas=0,
        dano=1
    )

# Nome
nome = input("Nome: ")
os.system('cls')
print(f"Print do servidor com IP e nome do jogador {nome}")