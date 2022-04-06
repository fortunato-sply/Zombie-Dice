'''
Módulo para dados
'''

from random import shuffle


class Dice(object):
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides


# constructor
def make_dice():
    """

    :return: lista com 13 dados
    """
    def red_dice():
        color = 'vermelho'
        sides = ['cerebro', 'tiro', 'tiro', 'tiro', 'passo', 'passo']
        dice = Dice(color, sides)
        return dice

    def green_dice():
        color = 'verde'
        sides = ['cerebro', 'cerebro', 'cerebro', 'tiro', 'passo', 'passo']
        dice = Dice(color, sides)
        return dice

    def yellow_dice():
        color = 'amarelo'
        sides = ['cerebro', 'cerebro', 'tiro', 'tiro', 'passo', 'passo']
        dice = Dice(color, sides)
        return dice

    red = red_dice()
    green = green_dice()
    yellow = yellow_dice()
    dices = [red, red, red, green, green, green, green, green, green, yellow, yellow, yellow, yellow]
    return dices


def shuffle_dices(dices: list):
    """

    :param dices: lista de dados
    :return: lista de dados embaralhada
    """
    return shuffle(dices)


def shuffle_sides(dice: Dice):
    """

    :param dice: dado
    :return: dado com as faces embaralhadas
    """
    return shuffle(dice.sides)
