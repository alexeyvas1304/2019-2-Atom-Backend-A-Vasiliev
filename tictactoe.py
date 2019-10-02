class TicTacToe:

    def __init__(self):
        self.lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.first_player = input("Введите имя первого игрока (крестик): ")
        self.second_player = input("Введите имя второго игрока (нолик): ")
        self.d = dict(zip(['x', 'o'], [self.first_player, self.second_player]))

    def paint(self):
        print('-' * 13)
        for i in range(3):
            print('| ', end='')
            print(*self.lst[i], sep=' | ', end='')
            print(' |')
            print('-' * 13)

    def is_win(self, sign):
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

    def game(self):
        variants = list(self.d.keys())
        cnt = 0
        self.paint()
        while True:
            sign = variants[cnt % 2]
            print(f"Ходит {self.d[sign]}")
            place = self.inputting(sign)
            print('-' * 49)
            self.lst[(place - 1) // 3][(place - 1) % 3] = sign
            self.paint()
            cnt += 1
            if self.is_win(sign):
                print(f"Победил {self.d[sign]}")
                break
            elif cnt == 9:
                print("Ничья")
                break
        print('-' * 13)
        print("Игра окончена")

    def inputting(self, sign):
        place = input(f"Введите номер поля, куда Вы хотите поставить {sign}: ")
        try:
            n = int(place)
            if 1 <= n <= 9 and self.lst[(n - 1) // 3][(n - 1) % 3] not in ['x', 'o']:
                return n
            else:
                print(f"{self.d[sign]}, Вы ошиблись с числом")
                return self.inputting(sign)
        except ValueError:
            print(f"{self.d[sign]}, Вы ввели не натуральное число")
            return self.inputting(sign)


if __name__ == '__main__':
    game = TicTacToe()
    game.game()
