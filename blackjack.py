# BLACK JACK - Jogo de cassino!!!
from time import sleep
# BLACK JACK - CASINO
import random
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(deck)
print(f'{"*"*58} \n Bem vindo ao cassino do Jack - BLACK JACK ! \n{"*"*58}')
sleep(2)
print("Você tem que aceitar a fortuna")
sleep(2)
print("Qual sua maior fortuna?")
sleep(2)
print("Você sabe qual sua maior fortuna? Teste sua sorte")
sleep(2)
print("Carregando---")
sleep(2)

print("Aguarde carregando---")
sleep(2)
print(
    "Então você ainda está aqui, não se foi. Eu te dei uma chance, mas não tem problema. Talvez você confie muito na sua sorte. \nVamos começar então."
)
sleep(2)
d_cards = []  
p_cards = []  
sleep(2)
while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print("As cartas que o dealer tem são X ", d_cards[1])

while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print("O total de jogadores é ", sum(p_cards))
        print("As cartas que o jogador tem são ", p_cards)

if sum(p_cards) > 21:
    print(f"Você ESTOROU!\n  {'*'*14}Dealer Ganhou!!{'*'*14}\n")
    exit()

if sum(d_cards) > 21:
    print(f"Dealer Ganhou!\n   {'*'*14} Você ganhou !!{'*'*18}\n")
    exit()

if sum(d_cards) == 21:
    print(f"{'*'*24}Dealer é o ganhador!!{'*'*14}")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print(f"{'*'*17}A partida está empatada!!{'*'*25}")
    exit()

def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print("Dealer tem o total " + str(sum(d_cards)) + "com as cartas ", d_cards)

    if sum(p_cards) == sum(d_cards):
        print(f"{'*'*15}A partida está empatada!!{'*'*15}")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print(f"{'*'*23}Dealer é o ganhador!!{'*'*18}")
        elif sum(p_cards) == 21:
            print(f"{'*'*20}There is tie!!{'*'*26}")
        else:
            print(f"{'*'*23}Dealer é o ganhandor!!{'*'*18}")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print(f"{'*'*23}Dealer é o ganhandor !!{'*'*18}")
        if sum(p_cards) == 21:
            print(f"{'*'*22}Player é o ganhandor !!{'*'*22}")
        if 21 > sum(p_cards) > sum(d_cards):
            print(f"{'*'*22}Player é o ganhandor !!{'*'*22}")

    else:
        if sum(p_cards) < 21:
            print(f"{'*'*22}Player é o ganhandor!!{'*'*22}")
        elif sum(p_cards) == 21:
            print(f"{'*'*22}Player é o ganhandor!!{'*'*22}")
        else:
            print(f"{'*'*23}Dealer é o ganhandor!!{'*'*18}")

while sum(p_cards) < 21:

    k = input("Quer bater ou ficar?\n Pressione 1 para bater e 0 para ficar ")
    if k == "1":
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print("Você tem o total " + str(sum(p_cards)) + " com as cartas ", p_cards)
        if sum(p_cards) > 21:
            print(f'{"*"*13}Você é o perdedor!{"*"*13}\n Dealer ganhou !!')
        if sum(p_cards) == 21:
            print(f'{"*"*19}Você é o ganhador!!{"*"*29}')
    else:
        dealer_choice()
        break