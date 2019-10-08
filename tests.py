"""
Тесты для крестиков-ноликов
"""
import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """
    Класс тестов
    """
    def tests(self):
        """
        Функция с проверками
        :return: None
        """

        game = TicTacToe()

        self.assertEqual(game.is_win('x'), False)
        self.assertEqual(game.is_win('o'), False)

        game.lst = [['x', 2, 'o'], ['x', 5, 6], ['x', 'o', 9]]
        self.assertEqual(game.is_win('x'), True)
        self.assertEqual(game.is_win('o'), False)

        game.lst = [['o', 'o', 'o'], ['x', 'x', 6], [7, 'x', 9]]
        self.assertEqual(game.is_win('x'), False)
        self.assertEqual(game.is_win('o'), True)

        game.lst = [['x', 2, 3], [4, 'x', 6], ['o', 'o', 'x']]
        self.assertEqual(game.is_win('x'), True)
        self.assertEqual(game.is_win('o'), False)

        game.lst = [['x', 2, 'o'], [4, 'o', 6], ['o', 'x', 'x']]
        self.assertEqual(game.is_win('x'), False)
        self.assertEqual(game.is_win('o'), True)

        game.lst = [[1, 'x', 3], [4, 'o', 6], [7, 8, 9]]
        self.assertEqual(game.check_input('cococo', 'x'), False)
        self.assertEqual(game.check_input('', 'x'), False)
        self.assertEqual(game.check_input('13', 'x'), False)
        self.assertEqual(game.check_input('-9', 'x'), False)
        self.assertEqual(game.check_input('1.5', 'x'), False)
        self.assertEqual(game.check_input('5', 'x'), False)
        self.assertEqual(game.check_input('1', 'x'), True)


if __name__ == '__main__':
    unittest.main()
