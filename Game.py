"""
Módulo auxiliar para o jogo
"""
import Emojis
import Players
from colorama import init, Fore, Style

init()


def gameover_txt(players: list, winner):
    """

    :param players: lista de jogadores
    :param winner: jogador vencedor
    :return: texto que roda no final do jogo
    """
    print('-' * 200 + f"\n{Fore.CYAN}Fim de jogo! O grande vencedor foi: {winner}\n")
    print(f"{Emojis.emj_coringa * 5} PLACAR FINAL {Emojis.emj_coringa * 5}")
    for player in players:
        print(f"   {Fore.LIGHTMAGENTA_EX}{player.name}: {player.score} cérebros")


def repeat_game():
    """

    :return: retorna um booleano que verifica se um novo jogo deve ser executado
    """
    if input(f"{Fore.LIGHTYELLOW_EX}Deseja iniciar um novo jogo? (s/n): ").upper() != 'S':
        return False
    else:
        return True


def initial_txt():
    """

    :return: texto inicial
    """
    print(Fore.BLUE + '-' * 200 + Fore.BLUE + Style.BRIGHT +
          f'''\n{Emojis.zombie * 3} Bem-vindo ao Zombie Dice! {Emojis.zombie * 3}
    - Este é um jogo de dados de mesa adaptado para computadores, portanto, visando manter o máximo da originalidade dele, me chamem de PC, seu host do RPG de zumbis.
    - Minha função é rodar os dados no tubo e anotar e compartilhar suas pontuações no Zombie Dice. Não se preocupe! O jogo é totalmente à prova de cheats. {Fore.LIGHTWHITE_EX}ou será que não?
    {Fore.BLUE}- Vence quem conseguir 13 {Emojis.emj_cerebro} antes, mas tome cuidado com os tiros!
    - Se você quiser ler as regras do jogo detalhadamente, acesse: https://www.ludopedia.com.br/jogo/zombie-dice.\n''' + Fore.BLUE + '-' * 200)


def placar(players: list):
    """

    :param players: lista de jogadores
    :return: placar atual
    """
    print('-' * 200 + f"\n{Emojis.emj_coringa * 3} PLACAR {Emojis.emj_coringa * 3}")
    for player in players:
        print(f"   {Fore.LIGHTMAGENTA_EX}{player.name}: {player.score} cérebros{Fore.LIGHTBLUE_EX}")


def game():
    """

    :return: função principal que roda o game
    """
    while True:
        initial_txt()
        players = Players.make_players()

        game_over = False
        while not game_over:
            for player in players:
                Players.Player.turn(player)
                if player.score >= 13:
                    game_over = True
                    winner = player.name
            placar(players)

        gameover_txt(players, winner)

        if not repeat_game():
            break
