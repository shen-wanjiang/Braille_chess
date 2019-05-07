# -*- coding: utf-8 -*-
import board
import player
import random


class Game(object):
    """游戏类"""
    def __init__(self):
        self.chess_board = board.Board()  # 棋盘对象
        # self.human = player.Player('玩家1')  # 人类玩家对象1
        # self.computer = player.Player('玩家2')  # 人类玩家对象2

        # 如果是人机对战的话,用下面的对象
        self.human = player.Player('玩家')  # 人类玩家对象
        self.computer = player.AIPlayer('计算机')  # 计算机玩家对象

    def random_player(self):
        """随机先手玩家
        :return: 落子先手顺序的玩家元祖
        """
        # 如果产生的随机数为1 表示玩家先手
        if random.randint(0, 1) == 1:
            players = (self.human, self.computer)
        else:
            players = (self.computer, self.human)
        # 设置玩家棋子
        players[0].chess = 'x'
        players[1].chess = 'o'
        print('根据随机结果 %s先行' % players[0].name)
        return players

    def play_round(self):
        """一轮完整对局"""
        # 1. 显示棋盘落子位置
        self.chess_board.show_board(True)
        # 2. 随机决定先手
        current_player, next_player = self.random_player()
        # 3. 两个玩家轮流落子
        while True:
            # 落子方落子
            current_player.move(self.chess_board)
            # 显示落子结果           4

            self.chess_board.show_board()
            # 是否胜利
            if self.chess_board.is_win(current_player.chess):
                print('%s 战胜 %s ' % (current_player.name, next_player.name))
                current_player.score += 1
                break
            # 是否为平局
            if self.chess_board.is_draw():
                print('%s和%s战成平局' % (current_player.name, next_player.name))
                break

            # 交换落子方
            current_player, next_player = next_player, current_player
        # 显示比分
        print('%s 对战 %s 比分是 %d : %d' % (self.human.name, self.computer.name, self.human.score, self.computer.score))

    def start(self):
        """循环开始对局"""
        while True:
            # 一轮完整对局
            self.play_round()
            # 询问是否继续
            is_continue = input('是否再来一盘(Y/N)?').upper()
            # 判断玩家输入
            if is_continue != 'Y':
                break
            # 重置棋盘数据
            self.chess_board.reset_board()

if __name__ == '__main__':
    Game().start()
