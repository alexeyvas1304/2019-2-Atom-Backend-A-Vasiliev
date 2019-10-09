"""
Программа для игры в крестики-нолики
"""


class TicTacToe:
    """
    Класс для игры в крестики-нолики
    """

    def __init__(self, warnings=False, first_player=None, second_player=None):
        self.lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.first_player = input("Введите имя первого игрока (крестик): ") \
            if first_player is None else first_player
        self.second_player = input("Введите имя второго игрока (нолик): ") \
            if second_player is None else second_player
        self.players = dict(zip(['x', 'o'],
                                [self.first_player, self.second_player]))
        self.warnings = warnings

    def paint(self):
        """
        Функция для рисования поля
        :return: None
        """
        print('-' * 13)
        for i in range(3):
            print('| ', end='')
            print(*self.lst[i], sep=' | ', end='')
            print(' |')
            print('-' * 13)

    def is_win(self, sign):
        """
        Функция, определяющая, есть победитель или нет
        :param sign: знак крестика или нолика
        :return: True/False
        """
        first_diag, second_diag = 0, 0
        lst_t = list(map(list, zip(*self.lst)))
        for i in range(3):
            if sum(self.lst[i][j] == sign for j in range(3)) == 3 or \
                    sum(lst_t[i][j] == sign for j in range(3)) == 3:
                return True
            first_diag += self.lst[i][i] == sign
            second_diag += self.lst[i][2 - i] == sign
        if first_diag == 3 or second_diag == 3:
            return True
        return False

    def play(self):
        """
        Функция, отвечающая за процесс игры
        :return: None
        """
        variants = list(self.players.keys())
        cnt = 0
        self.paint()
        while True:
            sign = variants[cnt % 2]
            print(f"Ходит {self.players[sign]}")
            place = self.input_position(sign)
            while not self.check_input(place, sign):
                place = self.input_position(sign)
            num = int(place)
            print('-' * 49)
            self.lst[(num - 1) // 3][(num - 1) % 3] = sign
            self.paint()
            cnt += 1
            if self.is_win(sign):
                print(f"Победил {self.players[sign]}")
                break
            elif cnt == 9:
                print("Ничья")
                break
        print('-' * 13)
        print("Игра окончена")

    @staticmethod
    def input_position(sign):
        """
        Функция ввода позиции на поле
        :return: номер позиции, куда надо поставить крестик/нолик
        """
        place = input(f"Введите номер поля, куда Вы хотите поставить {sign}: ")
        return place

    def check_input(self, place, sign):
        """
        Проверка введенной позиции
        :param place: позиция
        :param sign: крестик или нолик
        :return: True/False
        """
        try:
            num = int(place)
            if 1 <= num <= 9 and \
                    self.lst[(num - 1) // 3][(num - 1) % 3] not in ['x', 'o']:
                return True
            else:
                if self.warnings:
                    print(f"{self.players[sign]}, Вы ошиблись с числом")
                return False
        except ValueError:
            if self.warnings:
                print(f"{self.players[sign]}, Вы ввели не натуральное число")
            return False


if __name__ == '__main__':
    GAME = TicTacToe(warnings=True)
    GAME.play()
