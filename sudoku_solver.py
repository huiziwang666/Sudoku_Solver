class Sudoku:

    def __init__(self, board):
        self.board = board

    def solve_sudoku(self):
        r, c = self.find_next_empty()
        if r is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(guess, r, c):
                self.board[r][c] = guess
                if self.solve_sudoku():
                    return True
            self.board[r][c] = 0
        return False

    def find_next_empty(self):
        # finds the next row, col that's not filled yet which is 0
        # return row, col tuple (or None, None) if there is none
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None, None

    def is_valid(self, guess, r, c):
        r_nums = self.board[r]
        if guess in r_nums:
            return False
        c_nums = []
        for i in range(9):
            c_nums.append(self.board[i][c])
        if guess in c_nums:
            return False
        r_start = (r // 3) * 3
        c_start = (c // 3) * 3
        for r in range(r_start, r_start + 3):
            for c in range(c_start, c_start + 3):
                if self.board[r][c] == guess:
                    return False
        return True

    def __str__(self):
        board = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                board += "|" + str(self.board[i][j])
            board = board + "|\n"
        return board

    def write_to_file(self, filename):
        file = open(filename, "w")
        file.write(self.__str__())
        file.close()


def main():
    board_1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    sudoku = Sudoku(board_1)
    sudoku.solve_sudoku()
    print(sudoku)


if __name__ == "__main__":
    main()
