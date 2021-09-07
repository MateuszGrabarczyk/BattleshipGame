def check_if_key(board, row, column):
    """Checks if the key given in input matches a key on the set board"""
    start = row + column
    check = False
    for element in board:
        if start in element.keys():
            return True


def check_if_empty(board, row, column):
    """Checks if the key given in attack input is empty on the board"""
    start = row + column
    check = True
    if board[int(row) - 1][start] == "X" or board[int(row) - 1][start] == "O":
        check = False
    return check


def check_range(row, column, length, direction):
    """Checks if the coordinates given is in the range of our game board"""
    check = True
    numbers = range(0, 12)
    letters = "ABCDEFGHIJ"
    letter_index = letters.index(column)
    # Checking the range for up
    if direction == "up":
        if int(row) - length not in numbers:
            check = False
    # Checking the range for down
    elif direction == "down":
        if int(row) + length not in numbers:
            check = False
    # Checking the range for right
    elif direction == "right":
        if int(letter_index) + length not in range(0, 11):
            check = False
    # Checking the range for left
    elif direction == "left":
        if int(letter_index) + 1 - length not in range(0, 10):
            check = False
    return check


def check_space_around(row, column, length):
    """Every ship needs to have one free spot around and this function checks that"""
    check = True
    numbers = range(1, 11)
    letters = "ABCDEFGHIJ"
    letter_index = letters.index(column)
    # Checking corners


def check_if_free(board, row, column, length, direction):
    """Checks if the spots where we want to put the boats are empty"""
    letters = "ABCDEFGHIJ"
    letter_index = letters.index(column)
    check = True
    # Checking if free for up
    if direction.lower() == "up":
        x = int(row)
        for i in range(length):
            if board[x - 1][str(x) + column] == "X":
                check = False
                break
            x -= 1

    # Checking if free for down
    elif direction.lower() == "down":
        x = int(row)
        for i in range(length):
            if board[x - 1][str(x) + column] == "X":
                check = False
                break
            x += 1

    # Checking if free for right
    elif direction.lower() == "right":
        for i in range(length):
            if board[int(row) - 1][row + letters[letter_index]] == "X":
                check = False
                break
            letter_index += 1

    # Checking if free for left
    elif direction.lower() == "left":
        for i in range(length):
            if board[int(row) - 1][row + letters[letter_index]] == "X":
                check = False
                break
            letter_index -= 1

    return check


def list_of_keys(board, row, column, length, direction):
    """Returns a list with all the keys where the ship is placed on board"""
    key_list = []
    if direction.lower() == "up":
        num = row - length + 1
        if check_if_key(board, str(row), column) and check_if_key(board, str(num), column):
            for i in range(length):
                temp = str(row) + column
                row -= 1
                key_list.append(temp)
        return key_list
    elif direction.lower() == "down":
        num = row + length - 1
        if check_if_key(board, str(row), column) and check_if_key(board, str(num), column):
            for i in range(length):
                temp = str(row) + column
                row += 1
                key_list.append(temp)
        return key_list
    elif direction.lower() == "right":
        letters = "ABCDEFGHIJKLMNOP"
        start_letter_index = letters.index(column)
        end_letter_index = start_letter_index + length - 1
        if check_if_key(board, str(row), column) and check_if_key(board, str(row), letters[end_letter_index]):
            x = 0
            for i in range(length):
                temp = str(row) + letters[start_letter_index + x]
                x += 1
                key_list.append(temp)
            return key_list
    elif direction.lower() == "left":
        letters = "ABCDEFGHIJKLMNOP"
        start_letter_index = letters.index(column)
        end_letter_index = start_letter_index - length + 1
        if check_if_key(board, str(row), column) and check_if_key(board, str(row), letters[end_letter_index]):
            x = 0
            for i in range(length):
                temp = str(row) + letters[start_letter_index - x]
                x += 1
                key_list.append(temp)
            return key_list



def check_if_hit_the_mark(board, row, column):
    """Checks if the place where you decided to attack matches the ship on board_set"""
    start = row + column
    check = False
    if board[int(row) - 1][start] == "X":
        check = True
    return check


def check_if_won(board):
    """Checks if one of the players has won the game"""
    num_of_x = 0
    for row in board:
        for value in row.values():
            if value == "X":
                num_of_x += 1
    if num_of_x == 17:
        return True
    else:
        return False


# Short functions
def print_description():
    """Prints a description of placing the ships on a board"""
    print("You have to place:\n- A carrier (size 5)\n- A battleship (size 4)"
          "\n- A cruiser (size 3)\n- A submarine (size 3)\n- A destroyer (size 2)")
    print("You can place the ship giving the starting point\nand then choosing the direction (up, down, right, left)")


def quick_clean():
    """Function to go down 20 new lines to clean the console"""
    print(20*"\n")