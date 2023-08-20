"""
Game stone scissors paper

Moved to a separate module
"""
import random


def game_stone_scissors_paper():
    """
    Play the game "Rock, Paper, Scissors" with the user.

    This function simulates the game "Rock, Paper, Scissors" where the user plays
    against the computer. The user can choose to play or exit the game.
    The scores are displayed after each round, and the user can also request to see the score.
    The game continues until the user decides to exit.
    """
    start = input('Ви запустили гру "Камень, ножниці, папір". Бажаєте пограти? (Введіть + або -): ')

    if start == '+':
        print('Загрузка...')
        print("Загрузка завершена! Починаємо!")
        print("3...2...1...")
        print('Якщо забажаєте завершити введіть "-".')
        print('Якщо забажаєте подивитися рахунок введіть "с".')
        user_ball = 0
        rand_ball = 0
        while True:
            user = input("Камень, ножниці, папір? (Вводите к, н или п): ")
            list_play = ['к', 'н', 'п']
            if user in list_play:
                rand = random.choice(list_play)
                print(rand)

                if rand == 'к' and user == 'н':
                    rand_ball += 1
                if rand == 'к' and user == 'п':
                    user_ball += 1
                if rand == 'н' and user == 'к':
                    user_ball += 1
                if rand == 'н' and user == 'п':
                    rand_ball += 1
                if rand == 'п' and user == 'н':
                    user_ball += 1
                if rand == 'п' and user == 'к':
                    rand_ball += 1
            elif user == 'с':
                print('Ваші бали - ', user_ball, '. Бали Вашого суперника - ', rand_ball, ".")
            elif user == '-':
                print('Ваші бали - ', user_ball, '. Бали Вашего суперника - ', rand_ball, ".")
                print('Кінець гры! Заходьте ще!')
                break
            else:
                print('Введіть к, н или п')
