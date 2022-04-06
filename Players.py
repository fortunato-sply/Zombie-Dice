"""
Módulo para jogadores
"""
import Dices
import time
from Emojis import *
from random import choice, shuffle
from colorama import init, Style, Fore
init()


def txt_color(dice_color):
    """

    :param dice_color: cor do dado
    :return: comando para o Colorama alterar a cor
    """
    if dice_color == 'vermelho':
        return Fore.RED
    elif dice_color == 'verde':
        return Fore.LIGHTGREEN_EX
    else:
        return Fore.YELLOW


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # Inicia o turno do jogador
    def turn(self):
        """

        :return: função de rodada para o jogador
        """
        time.sleep(0.5)
        print(f'{Fore.LIGHTBLUE_EX}-' * 200 + f"\n{emj_coringa * 3} Vez de {self.name} {emj_coringa * 3}")
        input(f"{Fore.LIGHTYELLOW_EX}Pressione enter para continuar")
        tempscore = {'cerebros': 0, 'tiros': 0}
        dices = Dices.make_dice()
        dices_in_hand = []

        while True:
            Dices.shuffle_dices(dices)
            while len(dices_in_hand) < 3:
                dices_in_hand.append(dices.pop())

            n = 1
            for each_dice in reversed(dices_in_hand):
                print(f"{Fore.LIGHTBLUE_EX}Jogando dado {n}...\n")
                n += 1
                time.sleep(0.5)

                color = each_dice.color
                Dices.shuffle_sides(each_dice)
                side = choice(each_dice.sides)
                print(f"{txt_color(color)}   Dado {color}\n   Face: {side}\n")

                if side == 'cerebro':
                    tempscore['cerebros'] += 1
                    dices.append(dices_in_hand.pop(dices_in_hand.index(each_dice)))
                elif side == 'tiro':
                    tempscore['tiros'] += 1
                    dices.append(dices_in_hand.pop(dices_in_hand.index(each_dice)))

            print(f"{Fore.LIGHTYELLOW_EX}\nPontuação atual:\n   {Fore.LIGHTMAGENTA_EX}Cérebros: {tempscore['cerebros']}\n   {Fore.RED}Tiros: {tempscore['tiros']}{Fore.LIGHTBLUE_EX}")
            if tempscore['tiros'] >= 3:
                print(f"\nVocê morreu! Cérebros perdidos: {tempscore['cerebros']}")
                break
            else:
                if input("\nDeseja continuar jogando? (s/n): ").upper() != 'S':
                    self.score += tempscore['cerebros']
                    break


# constructor
def make_players():
    """

    :return: lista de jogadores embaralhada
    """
    while True:
        try:
            num_players = int(input("Digite quantos players irão jogar: "))
            if num_players > 1:
                break
            else:
                print("Você precisa de pelo menos dois players para jogar este jogo.")
        except ValueError:
            print("O número de players precisa ser um número inteiro!")

    list_players = []
    for i in range(num_players):
        name = input(f"Digite o nome do player {i+1}: ").capitalize()
        player = Player(name, 0)
        list_players.append(player)

    shuffle(list_players)
    print("*** ORDEM PARA JOGAR ***")
    for i in range(len(list_players)):
        print(f"{i+1}. {list_players[i].name}")
    return list_players
