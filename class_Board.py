import sys

import functions as f


class Board:
    def __init__(self, name):
        self.name = name
        self.board_attack = [
            {"1A": " ", "1B": " ", "1C": " ", "1D": " ", "1E": " ", "1F": " ", "1G": " ", "1H": " ", "1I": " ",
             "1J": " "},
            {"2A": " ", "2B": " ", "2C": " ", "2D": " ", "2E": " ", "2F": " ", "2G": " ", "2H": " ", "2I": " ",
             "2J": " "},
            {"3A": " ", "3B": " ", "3C": " ", "3D": " ", "3E": " ", "3F": " ", "3G": " ", "3H": " ", "3I": " ",
             "3J": " "},
            {"4A": " ", "4B": " ", "4C": " ", "4D": " ", "4E": " ", "4F": " ", "4G": " ", "4H": " ", "4I": " ",
             "4J": " "},
            {"5A": " ", "5B": " ", "5C": " ", "5D": " ", "5E": " ", "5F": " ", "5G": " ", "5H": " ", "5I": " ",
             "5J": " "},
            {"6A": " ", "6B": " ", "6C": " ", "6D": " ", "6E": " ", "6F": " ", "6G": " ", "6H": " ", "6I": " ",
             "6J": " "},
            {"7A": " ", "7B": " ", "7C": " ", "7D": " ", "7E": " ", "7F": " ", "7G": " ", "7H": " ", "7I": " ",
             "7J": " "},
            {"8A": " ", "8B": " ", "8C": " ", "8D": " ", "8E": " ", "8F": " ", "8G": " ", "8H": " ", "8I": " ",
             "8J": " "},
            {"9A": " ", "9B": " ", "9C": " ", "9D": " ", "9E": " ", "9F": " ", "9G": " ", "9H": " ", "9I": " ",
             "9J": " "},
            {"10A": " ", "10B": " ", "10C": " ", "10D": " ", "10E": " ", "10F": " ", "10G": " ", "10H": " ", "10I": " ",
             "10J": " "}]
        self.board_set = [{"1A": " ", "1B": " ", "1C": " ", "1D": " ", "1E": " ", "1F": " ", "1G": " ", "1H": " ", "1I": " ",
                      "1J": " "},
                     {"2A": " ", "2B": " ", "2C": " ", "2D": " ", "2E": " ", "2F": " ", "2G": " ", "2H": " ", "2I": " ",
                      "2J": " "},
                     {"3A": " ", "3B": " ", "3C": " ", "3D": " ", "3E": " ", "3F": " ", "3G": " ", "3H": " ", "3I": " ",
                      "3J": " "},
                     {"4A": " ", "4B": " ", "4C": " ", "4D": " ", "4E": " ", "4F": " ", "4G": " ", "4H": " ", "4I": " ",
                      "4J": " "},
                     {"5A": " ", "5B": " ", "5C": " ", "5D": " ", "5E": " ", "5F": " ", "5G": " ", "5H": " ", "5I": " ",
                      "5J": " "},
                     {"6A": " ", "6B": " ", "6C": " ", "6D": " ", "6E": " ", "6F": " ", "6G": " ", "6H": " ", "6I": " ",
                      "6J": " "},
                     {"7A": " ", "7B": " ", "7C": " ", "7D": " ", "7E": " ", "7F": " ", "7G": " ", "7H": " ", "7I": " ",
                      "7J": " "},
                     {"8A": " ", "8B": " ", "8C": " ", "8D": " ", "8E": " ", "8F": " ", "8G": " ", "8H": " ", "8I": " ",
                      "8J": " "},
                     {"9A": " ", "9B": " ", "9C": " ", "9D": " ", "9E": " ", "9F": " ", "9G": " ", "9H": " ", "9I": " ",
                      "9J": " "},
                     {"10A": " ", "10B": " ", "10C": " ", "10D": " ", "10E": " ", "10F": " ", "10G": " ", "10H": " ",
                      "10I": " ", "10J": " "}]

    def print_board_attack(self):
        """Function prints the current state of board_attack"""
        counter = 1
        print("   A B C D E F G H I J")
        for element in self.board_attack:
            if counter != 10:
                print(" ",sep=' ', end='', flush=True)
            print(str(counter) + " ", sep=' ', end='', flush=True)
            for value in element.values():
                print(value + "|", sep=' ', end='', flush=True)
            counter += 1
            print()

    def print_board_set(self):
        """Function prints the current state of board_set"""
        counter = 1
        print("   A B C D E F G H I J")
        for element in self.board_set:
            if counter != 10:
                print(" ", sep=' ', end='', flush=True)
            print(str(counter) + " ", sep=' ', end='', flush=True)
            for value in element.values():
                print(value + "|", sep=' ', end='', flush=True)
            counter += 1
            print()

    def set_ship_up(self, length, x, y):
        """Sets the ship up on a board"""
        if f.check_if_key(self.board_set, x, y) and f.check_range(x, y, length, "up") and f.check_if_free(self.board_set, x, y, length, "up"):
            counter = int(x)
            for i in range(length):
                coordinates = str(counter) + y
                self.board_set[counter-1][coordinates] = "X"
                counter -= 1
            return True
        else:
            return False

    def set_ship_down(self, length, x, y):
        """Sets the ship down on a board"""
        if f.check_if_key(self.board_set, x, y) and f.check_range(x, y, length, "down") and f.check_if_free(self.board_set, x, y, length, "down"):
            counter = int(x)
            for i in range(length):
                coordinates = str(counter) + y
                self.board_set[counter-1][coordinates] = "X"
                counter += 1
            return True
        else:
            return False

    def set_ship_right(self, length, x, y):
        """Sets the ship right on a board"""
        letters = "ABCDEFGHIJ"
        letter_index = letters.index(y)
        if f.check_if_key(self.board_set, x, y) and f.check_range(x, y, length, "right") and f.check_if_free(self.board_set, x, y, length, "right"):
            for i in range(length):
                coordinates = x + letters[letter_index]
                self.board_set[int(x) - 1][coordinates] = "X"
                letter_index += 1
            return True
        else:
            return False

    def set_ship_left(self, length, x, y):
        """Sets the ship down on a board"""
        letters = "ABCDEFGHIJ"
        letter_index = letters.index(y)
        if f.check_if_key(self.board_set, x, y) and f.check_range(x, y, length, "left") and f.check_if_free(self.board_set, x, y, length, "left"):
            for i in range(length):
                coordinates = x + letters[letter_index]
                self.board_set[int(x) - 1][coordinates] = "X"
                letter_index -= 1
            return True
        else:
            return False

    def set_board(self):
        """Function sets the location of all the ships on the board"""
        f.print_description()
        for num in [5, 4, 3, 3, 2]:
            while True:
                self.print_board_set()
                print("It's " + self.name + " move!")
                print("Where do you want to place size " + str(num) + " ship?")
                x = str(input("Give me the starting row (it has to be a number): "))
                y = str(input("Give me the starting column (it has to be a big letter): ")).upper()
                direction = str(input("Give me the direction: ")).lower()
                if direction == "up":
                    if self.set_ship_up(num, x, y):
                        break
                    else:
                        f.quick_clean()
                        print("You tried to place the ship in a wrong place, try again!")
                        continue
                elif direction == "down":
                    if self.set_ship_down(num, x, y):
                        break
                    else:
                        f.quick_clean()
                        print("You tried to place the ship in a wrong place, try again!")
                        continue
                elif direction == "right":
                    if self.set_ship_right(num, x, y):
                        break
                    else:
                        f.quick_clean()
                        print("You tried to place the ship in a wrong place, try again!")
                        continue
                elif direction == "left":
                    if self.set_ship_left(num, x, y):
                        break
                    else:
                        f.quick_clean()
                        print("You tried to place the ship in a wrong place, try again!")
                        continue
                else:
                    print("You passed wrong direction, try again!")
                    continue

    def attack(self, name):
        """Method that allows the opponent to attack your board"""
        hit = True
        while hit:
            print("It's " + name + " move!")
            self.print_board_attack() # print the board to see where you can attack
            x = str(input("Give me the starting row where you wanna attack: "))
            y = str(input("Give me the starting column where you wanna attack: ")).upper()
            coordinates = x + y
            if f.check_if_key(self.board_attack, x, y) and f.check_if_empty(self.board_attack, x, y): # checking if the coordinates given are valid and if the place where you wanna attack is empty
                if f.check_if_hit_the_mark(self.board_set, x, y): # check if you hit the ship on which was set on board set
                    self.board_attack[int(x) - 1][coordinates] = "X" # 'X' means you hit a ship
                    print("You hit the ship!")
                    if f.check_if_won(self.board_attack):
                        print(name + " won the game, congrats!!!")
                        sys.exit(0)
                    else:
                        print("You are given another attack!")
                        f.quick_clean()
                else:
                    print("You didn't hit the ship!")
                    self.board_attack[int(x) - 1][coordinates] = "O" # 'O' means you missed a shot
                    hit = False
                    f.quick_clean()
            else:
                f.quick_clean()
                print("You passed wrong coordinates or the attack spot is not empty.")
                print("Try again")


class Game:
    player1 = Board("Mateusz")
    player2 = Board("Julia")

    def game(self):
        # First the players need to place the ships on the board
        self.player1.set_board()
        f.quick_clean()
        self.player2.set_board()
        f.quick_clean()
        # Then we can start the attacks
        while True:
            self.player1.attack(self.player2.name)
            self.player2.attack(self.player1.name)


