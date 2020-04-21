"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class LotoGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self.numbers_count = 90  # количество ходов
        self.human_count = 15
        self.computer_count = 15
        self.bag = random.sample([i for i in range(1, 92)], 91)  # мешок с бочонками

    def start(self):
        for step in range(1, 91):
            stop = False
            self.numbers_count -= 1
            print(' ' * 14 + 'ХОД ' + str(step) + ' ' * 14)
            print('Новый бочонок:', self.bag[step - 1], '(осталось', str(self.numbers_count) + ')')
            print(self._player)
            print(self._computer)
            b = input('Зачеркнуть цифру?   y/n   ')
            card_human = getattr(human_player, '_card_list')
            card_computer = getattr(computer_player, '_card_list')
            x = 0
            for el in range(0, 3):
                if card_human[el].count(self.bag[step - 1]) == 1:
                    x = x + 1
                else:
                    x = x + 0
            if b == 'y' and x == 1:
                for el in card_human:
                    for i in el:
                        if b == 'y' and i == self.bag[step - 1]:
                            card_human[card_human.index(el)][el.index(self.bag[step - 1])] = '-'
                            self.human_count = self.human_count - 1
                            if self.human_count == 0:
                                stop = True
                                print(self._player, 'выиграл!')
                print('Цифра зачеркнута! Игра продолжается')
            elif b == 'y' and x != 1:
                print('Игра окончена! Игрок проиграл - на карточке не было такой цифры')
                stop = True
            elif b == 'n' and x == 1:
                print('Игра окончена! Игрок проиграл - выбрано "n" но на карточке была такая цифра')
                stop = True
            elif b == 'n' and x != 1:
                print('Правильно! Игра продолжается')
            else:
                print('Игра окончена! Игрок проиграл - Вы ответили что то не внятное - не "y" и не "n"')
                stop = True

            y = 0
            i = 0
            for el in range(0, 3):
                if card_computer[el].count(self.bag[step - 1]) == 1:
                    y = y + 1
                    i = el
                else:
                    y = y + 0
            if y == 1:
                card_computer[i][card_computer[i].index(self.bag[step - 1])] = '-'
                self.computer_count = self.computer_count - 1
                if self.computer_count == 0:
                    stop = True
                    print('Компьютер выиграл!')

            if stop == True:
                break
        return


class LotoCard:
    def __init__(self, name):
        self._name = name
        self._card_list = self.create_card  # список списков - карточка

    def __str__(self):
        self.b = 36  # количество тире сверху и внизу карточки
        self.c = int((self.b - len(self._name) - 2) / 2)  # количество тире справа и слева имени игрока
        self.up = '-' * self.c + ' ' + self._name + ' ' + '-' * self.c
        self.a = self.up + '\n' + '\n'.join(['\t'.join([str(j) for j in i]) for i in self._card_list]) + '\n' + '-' * self.b
        return self.a

    @property
    def create_card(self):
        a = random.sample([i for i in range(1, 91)], 27)
        b = [a[0:9], a[9:18], a[18:27]]
        for i in range(3):
            c = random.sample(range(9), 4)
            for j in c:
                b[i].pop(j)
                b[i].insert(j, ' ')
        return b


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()