import os


def convert_board(filename):
    try:
        if not os.path.exists(filename):
            print("File", filename, "was not found")
        else:
            file = open(filename)
            board = []
            for line in file.readlines():
                lt = []
                for num in line.split("|"):
                    if num in "0123456789" and num != "":
                        lt.append(int(num))
                board.append(lt)
            file.close()
            return board

    except PermissionError:
        print("Permission denied for ", filename)
    except OSError:
        print("Error occurred while reading ", filename)
    except ZeroDivisionError:
        print(filename, "file is empty")


def main():
    print(convert_board("sudoku_easy"))


if __name__ == "__main__":
    main()
