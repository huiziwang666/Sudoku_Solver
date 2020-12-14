from final_project.menu import menu
from final_project.convert_to_board import convert_board
from final_project.sudoku_solver import Sudoku
from final_project.draw_win import draw
from final_project.print_board import print_board
from final_project.timer import Timer
from final_project.clone import hint, valid


def main():
    filename = menu()
    board = convert_board(filename)
    print_board(board)
    t = Timer()
    t.start()
    sudoku = Sudoku(board)
    mistake = 0
    count = 0
    while True:
        option = input("Enter 'Row,Column,Number' or 'h' for 'Hint': ")
        if option.lower() not in 'hq':
            try:
                user_input = option.split(',')
                row = int(user_input[0])
                col = int(user_input[1])
                num = int(user_input[2])
                if valid(row, col, num, board) is True:
                    board[row-1][col-1] = num
                    print_board(board)
                    x, y = sudoku.find_next_empty()
                    if x is None:
                        sudoku.write_to_file("solution")
                        t.stop()
                        draw()
                        break
                else:
                    if mistake < 2:
                        print("There is a mistake, please try again")
                        mistake += 1
                    else:
                        print("You have failed")
                        break
            except ValueError:
                print("Invalid input")
        elif option == "h":
            if count < 3:
                hint(board)
                count += 1
            else:
                print("Maximum hint number reached")
        elif option == "q":
            print("Game over")
            break


main()


