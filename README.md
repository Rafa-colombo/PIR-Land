# ⚔️ PIR-Land: RPG Multiplayer de Arena

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Redes](https://img.shields.io/badge/Redes-Cliente%2FServidor-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green?style=for-the-badge)

## 📖 Sobre o Projeto
**PIR-Land** é um jogo RPG multiplayer com foco em gerenciamento de recursos e combates PVP (Player vs Player). Desenvolvido como projeto prático para a disciplina de Redes 1, o jogo utiliza uma arquitetura **Cliente-Servidor** para conectar os jogadores em uma arena de batalha simultânea.

---

## 🎮 Como Funciona o Jogo (Gameplay)

O jogo opera em um sistema de gerenciamento de tempo diário seguido por um combate obrigatório.

### ⏳ Fase 1: Turnos Diários
Você inicia o dia com **4 turnos**. Cada ação na cidade consome 1 turno. Use-os com sabedoria nos seguintes locais:
* ⚒️ **Ferreiro:** Compre equipamentos para aumentar sua Vida Máxima e/ou Dano.
* 🧙‍♂️ **Loja do Mago:** Dê upgrade nas skills da sua classe ou adquira a *Clarividência* (permite ver os status ocultos do adversário no PVP).
* 🕶️ **Black Market:** Participe de lutas clandestinas para dobrar suas moedas ou compre poções proibidas e cargas extras para a arena.
* 🛡️ **Guilda:** Complete até 3 missões diárias para farmar moedas.

### ⚔️ Fase 2: A Arena PVP
Ao zerar seus turnos, você é transportado automaticamente para o combate contra outro jogador conectado ao servidor. A batalha segue uma mecânica tática de *"Carrega, Defende, Atira"*:
* **Carregar:** Gera uma carga de ataque baseada na sua classe.
* **Defender:** Bloqueia parcialmente o dano inimigo (se usado enquanto o inimigo carrega, a ação é desperdiçada).
* **Atacar:** Gasta suas cargas acumuladas para desferir dano.

*Vence quem permanecer com a vida acima de zero ao final do embate!*

---

## ⚙️ Arquitetura e Tecnologias

O coração do PIR-Land é a sua comunicação em rede. O projeto foi estruturado para suportar partidas multiplayer assíncronas/síncronas.

* **Linguagem:** 100% Python.
* **Comunicação em Rede (Sockets / gRPC):** O jogo implementa uma comunicação direta para gerenciar o estado das partidas.
* **Estrutura de Arquivos:**
  * `servidor.py`: Gerencia as conexões, pareamento de jogadores (matchmaking) na arena e validação de regras.
  * `client.py`: Interface do jogador, onde as decisões de turnos e inputs de combate são computados e enviados ao servidor.
  * `functions.py`: Biblioteca de funções auxiliares (cálculo de dano, economia, status).
  * `Dialogos.txt`: Banco de dados de textos e lore da interface.

---

## 🚀 Como Instalar e Jogar

Por se tratar de um jogo multijogador em rede, você precisará inicializar o servidor antes de conectar os clientes (jogadores).

### Pré-requisitos
* Python 3.x instalado na máquina.
* Clone este repositório:
  ```bash
  git clone [https://github.com/Rafa-colombo/PIR-Land.git](https://github.com/Rafa-colombo/PIR-Land.git)
  cd PIR-Land
  ```
  Passo 1: Iniciando o Servidor
Abra um terminal na pasta do projeto e inicie o ambiente hospedeiro:
  ```bash
  python servidor.py
  ```
(O servidor ficará escutando as conexões e aguardando os aventureiros).

  Passo 2: Conectando os Jogadores
Em outros terminais (na mesma máquina ou em computadores diferentes na mesma rede), inicie o cliente do jogo:
```bash
python client.py
```
Abra pelo menos duas instâncias do client.py para testar o combate PVP na Arena!

## 🔮 Atualizações Futuras (Roadmap)   
[ ] Implementar passagem de dias contínua após as vitórias na arena.

[ ] Sistema de experiência (XP) e nivelamento do jogador.

[ ] Criação de um Placar Global (Leaderboard) ranqueando os melhores guerreiros de PIR.


### 📜 A Lore: A Cidade de PIR
Você, audaz aventureiro, acaba de pisar na lendária cidade de PIR!
Uma metrópole de esplendor inigualável, onde a glória e a fama se entrelaçam. Suas ruas ecoam com os ecos de antigas conquistas, e cada esquina sussurra segredos de feitos heroicos e riquezas imensuráveis. Aqui, o destino dos mais corajosos é forjado nas labaredas da ambição e do poder.
PIR, com sua imponente arquitetura de mármore e ferro, não é apenas uma cidade, mas um império de oportunidades, onde o ouro reluz em cada mercado e as lendas são escritas a cada amanhecer. E é claro, não poderia faltar sua arena de batalha, o palco onde guerreiros de todo o mundo vêm testar sua força, coragem e honra. Um lugar onde sangue, suor e glória se misturam em um espetáculo de tirar o fôlego.
Prepare-se, aventureiro, pois em PIR, o destino é tão grandioso quanto a própria cidade!


<div align="center">
      <em>"Um lugar onde sangue, suor e glória se misturam em um espetáculo de tirar o fôlego."</em>
</div>


