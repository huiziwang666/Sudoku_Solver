from final_project.sudoku_solver import Sudoku


def hint(board):
    clo_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            row.append(board[i][j])
        clo_board.append(row)
    sudoku = Sudoku(clo_board)
    r, c = sudoku.find_next_empty()
    sudoku.solve_sudoku()
    value = clo_board[r][c]
    print(f"The value at row: {r+1}, column: {c+1} is {value}")


def valid(r, c, num, board):
    clo_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[0])):
            row.append(board[i][j])
        clo_board.append(row)
    sudoku = Sudoku(clo_board)
    sudoku.solve_sudoku()
    if clo_board[r-1][c-1] == num:
        return True
    else:
        return False


def main():
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print(board)
    hint(board)
    print(valid(1, 3, 4, board))


if __name__ == "__main__":
    main()
