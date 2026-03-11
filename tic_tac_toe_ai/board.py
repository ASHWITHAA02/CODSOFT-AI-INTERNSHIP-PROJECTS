class Board:

    def __init__(self):
        self.board = [" " for _ in range(9)]

    def display(self):
        b = self.board
        print()
        print(f"{b[0]} | {b[1]} | {b[2]}")
        print("--+---+--")
        print(f"{b[3]} | {b[4]} | {b[5]}")
        print("--+---+--")
        print(f"{b[6]} | {b[7]} | {b[8]}")
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def winner(self, player):
        win_conditions = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]

        for cond in win_conditions:
            if all(self.board[i] == player for i in cond):
                return True
        return False

    def is_full(self):
        return " " not in self.board