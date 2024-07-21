class GameLogic:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        lines = self.board + [list(col) for col in zip(*self.board)] + [
            [self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]
        ]
        for line in lines:
            if line[0] == line[1] == line[2] != '':
                return line[0]
        return None

    def is_draw(self):
        return all(all(cell != '' for cell in row) for row in self.board)
