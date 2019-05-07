# -*- coding: utf-8 -*-
import board
import random

class Player(object):
    """玩家类"""
    def __init__(self, name):
        self.name = name  # 姓名
        self.score = 0  # 成绩
        self.chess = None  # 棋子

    def move(self, chess_board):
        """在棋盘上落子
        :param chess_board
        """
        # 1. 由用户输入要落子索引
        index = -1
        while index not in chess_board.movable_list:
            try:
                index = int(input('请%s输入落子位置%s:' % (self.name, chess_board.movable_list)))
            except ValueError:
                pass
        # 2. 在指定位置落子
        chess_board.move_down(index, self.chess)


class AIPlayer(Player):
    """智能玩家"""

    def move(self, chess_board):
        """在棋盘上落子

        :param chess_board:
        """
        print("%s 正在思考落子位置..." % self.name)
        # 从棋盘对象的可落子索引列表中随机选择一个索引
        index = random.choice(chess_board.movable_list)
        # 在指定位置落子
        chess_board.move_down(index, self.chess)

if __name__ == '__main__':
    # 1. 创建棋盘对象
    chess_board = board.Board()
    # 2. 创建玩家对象
    human = Player('玩家')
    human.chess = 'x'
    # 3. 玩家在棋盘上循环落子,直到玩家胜利
    while not chess_board.is_win(human.chess):
        human.move(chess_board)
        # 显示棋盘
        chess_board.show_board()


