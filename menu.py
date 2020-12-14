def menu():
    print("Welcome to Sudoku game!\nA sudoku solution must satisfy all of the following rules:\
\nEach of the digits 1-9 must occur exactly once in each row.\
\nEach of the digits 1-9 must occur exactly once in each column.\
\nEach of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid\
\nAllow maximum 3 mistakes\
\nEnter h or H for hint (maximum 3 times)\
\n\
\nPlease choose the level of difficulty")
    print('1. Easy Level\n2. Medium Level\n3. Hard Level\nEnter "Q" or "q" to quit at any time')
    option = input("Option: ")
    filename = ''
    while option not in '123Qq':
        print("Invalid option")
        print('1. Easy Level\n2. Medium Level\n3. Hard Level\nEnter "Q" or "q" to quit at any time')
        option = input("Option: ")
    if option == '1':
        filename = "sudoku_easy"
    elif option == '2':
        filename = "sudoku_medium"
    elif option == '3':
        filename = "sudoku_hard"
    elif option == 'Q' or 'q':
        print("Game over")
        exit()
    return filename


def main():
    print(menu())


if __name__ == "__main__":
    main()
