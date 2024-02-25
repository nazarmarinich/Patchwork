import random
import numpy as np
import math

# Bonus patches on the game timeline
patches = [26, 32, 38, 44, 50]
# Game timeline
timeline = np.arange(1, 54)

# Patches order
tiles = np.arange(0, 33)
# random.shuffle(tiles)

patchwork_pieces = [
    {"ID": 0, "Name": "ladder", "Square": 5, "Buttons": 3, "Cost_b": 10, "Cost_t": 4, 'Weight': 0.0},
    {"ID": 1, "Name": "corner5", "Square": 5, "Buttons": 2, "Cost_b": 10, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 2, "Name": "corner10", "Square": 4, "Buttons": 2, "Cost_b": 4, "Cost_t": 6, 'Weight': 0.0},
    {"ID": 3, "Name": "line3", "Square": 3, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 4, "Name": "strange6", "Square": 6, "Buttons": 0, "Cost_b": 2, "Cost_t": 1, 'Weight': 0.0},
    {"ID": 5, "Name": "line4", "Square": 4, "Buttons": 1, "Cost_b": 3, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 6, "Name": "z2", "Square": 4, "Buttons": 1, "Cost_b": 3, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 7, "Name": "cross4", "Square": 7, "Buttons": 1, "Cost_b": 1, "Cost_t": 4, 'Weight': 0.0},
    {"ID": 8, "Name": "line5", "Square": 5, "Buttons": 1, "Cost_b": 7, "Cost_t": 1, 'Weight': 0.0},
    {"ID": 9, "Name": "square", "Square": 4, "Buttons": 2, "Cost_b": 6, "Cost_t": 5, 'Weight': 0.0},
    {"ID": 10, "Name": "trapez7", "Square": 6, "Buttons": 2, "Cost_b": 7, "Cost_t": 4, 'Weight': 0.0},
    {"ID": 11, "Name": "corner2", "Square": 4, "Buttons": 1, "Cost_b": 4, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 12, "Name": "fatz", "Square": 6, "Buttons": 0, "Cost_b": 4, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 13, "Name": "z8", "Square": 8, "Buttons": 3, "Cost_b": 8, "Cost_t": 6, 'Weight': 0.0},
    {"ID": 14, "Name": "n", "Square": 5, "Buttons": 0, "Cost_b": 1, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 15, "Name": "cross0", "Square": 6, "Buttons": 1, "Cost_b": 0, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 16, "Name": "z5", "Square": 5, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 17, "Name": "corner3", "Square": 3, "Buttons": 0, "Cost_b": 3, "Cost_t": 1, 'Weight': 0.0},
    {"ID": 18, "Name": "z7", "Square": 4, "Buttons": 3, "Cost_b": 7, "Cost_t": 6, 'Weight': 0.0},
    {"ID": 19, "Name": "corner1", "Square": 3, "Buttons": 0, "Cost_b": 1, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 20, "Name": "corner4", "Square": 5, "Buttons": 1, "Cost_b": 3, "Cost_t": 4, 'Weight': 0.0},
    {"ID": 21, "Name": "longz", "Square": 5, "Buttons": 1, "Cost_b": 2, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 22, "Name": "bigt", "Square": 6, "Buttons": 2, "Cost_b": 7, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 23, "Name": "smallt", "Square": 5, "Buttons": 2, "Cost_b": 5, "Cost_t": 5, 'Weight': 0.0},
    {"ID": 24, "Name": "hugez", "Square": 6, "Buttons": 0, "Cost_b": 1, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 25, "Name": "line2", "Square": 2, "Buttons": 0, "Cost_b": 2, "Cost_t": 1, 'Weight': 0.0},
    {"ID": 26, "Name": "trapez2", "Square": 4, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0},
    {"ID": 27, "Name": "H", "Square": 7, "Buttons": 0, "Cost_b": 2, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 28, "Name": "trapez8", "Square": 8, "Buttons": 1, "Cost_b": 5, "Cost_t": 3, 'Weight': 0.0},
    {"ID": 29, "Name": "corner6", "Square": 6, "Buttons": 3, "Cost_b": 10, "Cost_t": 5, 'Weight': 0.0},
    {"ID": 30, "Name": "longn", "Square": 6, "Buttons": 1, "Cost_b": 1, "Cost_t": 5, 'Weight': 0.0},
    {"ID": 31, "Name": "zz", "Square": 6, "Buttons": 2, "Cost_b": 3, "Cost_t": 6, 'Weight': 0.0},
    {"ID": 32, "Name": "cross5", "Square": 5, "Buttons": 2, "Cost_b": 5, "Cost_t": 4, 'Weight': 0.0},
]


class Player:
    def __init__(self, number):
        self.number = number
        self.time_count = 53
        self.buttons_aimed = 0
        self.buttons = 5
        self.tiles = []
        self.field = np.zeros((9, 9), dtype=int)
        self.square = 0

    def greedy_sorting(self, tiles_to_sort):
        """
        Let's sort tiles based on calculated weight
        """
        tiles_sorted = []
        for i in tiles_to_sort:
            ts = patchwork_pieces[i]
            if self.time_count > 0:
                weight = ((ts['Square'] + (ts['Buttons'] * math.pow(self.time_count, .2)))
                          / (ts['Cost_b'] + ts['Cost_t']))
            else:
                weight = 0
            tiles_sorted.append([weight, i])
        tiles_sorted.sort(reverse=True)
        tiles_sorted = [sublist[1] for sublist in tiles_sorted]

        return tiles_sorted

    def calc_aimed_patch(self, time_cost):
        """
        Calculate if the player aimed a patch based on the timeline position.
        Args:
        - time_position (int): Current position on the timeline.
        - time_cost (int): Time cost of the tile being placed.
        Returns:
        - square_sum (int): Updated number of square
        """
        global patches
        for tn in timeline[(53 - self.time_count):(53 - self.time_count + time_cost)]:
            if tn in patches:  # Check if the player time position is an aimed button position
                self.square += 1
                patches = np.delete(patches, 0)

    def calc_aimed_buttons(self, time_cost):
        """
        Calculate the total number of buttons aimed by the player based on the timeline position.
        Args:
        - time_position (int): Current position on the timeline.
        - time_cost (int): Time cost of the tile being placed.
        - buttons (int): Current number of buttons the player has.
        - aimed (int): Number of buttons aimed by the tile.
        Returns:
        - buttons (int): Updated number of buttons after considering aimed buttons based on the timeline position.
        """
        for tn in timeline[(53 - self.time_count):(53 - self.time_count + time_cost)]:
            if tn % 6 == 5:  # Check if the player time position is an aimed button position
                self.buttons += self.buttons_aimed

    def print_turn_results(self, tile, buttons, time):
        # Print the player actions

        print("Игрок: " + str(self.number) + " BB:" + str(self.buttons) + "/" + str(self.buttons_aimed) + " BT:"
              + str(self.time_count) + " Square: " + str(self.square) + " Buttons: "
              + str(buttons) + " Time: " + str(time) + " Tile: " + str(tile))


# _______________functions _______________________

def print_board(board):
    """
    Print the game board.
    """
    for row in board:
        print("  ".join(str(cell) for cell in row))


def calc_results():
    p1_result = player1.buttons - (81 - min(player1.square, 81)) * 2
    p2_result = player2.buttons - (81 - min(player2.square, 81)) * 2
    if p1_result > p2_result:
        print("\n" + "Результат игрока 1: " + str(p1_result) + "\n" + "Результат игрока 2: " + str(
            p2_result) + "\n" + "Победил игрок 1!")
    elif p1_result == p2_result and player == 1:
        print("\n" + "Результат игрока 1: " + str(p1_result) + "\n" + "Результат игрока 2: " + str(
            p2_result) + "\n" + "Победил игрок 1!")
    else:
        print("\n" + "Результат игрока 1: " + str(p1_result) + "\n" + "Результат игрока 2: " + str(
            p2_result) + "\n" + "Победил игрок 2!")
    return


# a = greedy_sorting(tiles[0:3])
# print(a)

"________________Game Logic ________________"

# print(tiles)
player1 = Player(1)
player2 = Player(2)

player = 1
while player1.time_count + player2.time_count > 0:
    if player == 1:
        # print(tiles)
        while player1.time_count >= player2.time_count:
            n = 0
            # Player 1 uses greedy sorting
            tiles_s = player1.greedy_sorting(tiles[0:3])
            for i in tiles_s[0:3]:
                # for i in tiles[0:3]:
                tile = patchwork_pieces[i]
                if player1.buttons >= tile['Cost_b'] and player1.time_count > 0:
                    player1.tiles.append(tile)
                    tiles = np.roll(tiles, -np.where(tiles == i)[0][0])
                    tiles = tiles[1::]
                    # print(tiles)
                    player1.buttons -= tile['Cost_b']
                    player1.buttons_aimed += tile['Buttons']
                    player1.square += tile['Square']
                    player1.calc_aimed_patch(tile['Cost_t'])
                    player1.calc_aimed_buttons(tile['Cost_t'])
                    player1.time_count -= tile['Cost_t']
                    player1.print_turn_results(tile['ID'], tile['Cost_b'], tile['Cost_t'])
                    if player1.time_count < player2.time_count:
                        player = 2
                    break
                if n == 2 and player1.time_count >= player2.time_count:
                    a = (player1.time_count - player2.time_count + 1)
                    player1.buttons += a
                    player1.calc_aimed_patch(a)
                    player1.calc_aimed_buttons(a)
                    player1.time_count -= a
                    player1.print_turn_results("-", "-", "-")
                    player = 2
                    break
                n += 1

    else:
        # print(tiles)
        while player2.time_count >= player1.time_count:
            n = 0
            for i in tiles[0:3]:
                tile = patchwork_pieces[i]
                if player2.buttons >= tile['Cost_b'] and player2.time_count > 0:
                    player2.tiles.append(tile)
                    tiles = np.roll(tiles, -np.where(tiles == i)[0][0])
                    tiles = tiles[1::]
                    # print(tiles)
                    player2.buttons -= tile['Cost_b']
                    player2.buttons_aimed += tile['Buttons']
                    player2.square += tile['Square']
                    player2.calc_aimed_patch(tile['Cost_t'])
                    player2.calc_aimed_buttons(tile['Cost_t'])
                    player2.time_count -= tile['Cost_t']
                    player2.print_turn_results(tile['ID'], tile['Cost_b'], tile['Cost_t'])
                    if player2.time_count < player1.time_count:
                        player = 1
                    break
                if n == 2 and player2.time_count >= player1.time_count:
                    a = (player2.time_count - player1.time_count + 1)
                    player2.buttons += a
                    player2.calc_aimed_patch(a)
                    player2.calc_aimed_buttons(a)
                    player2.time_count -= a
                    player2.print_turn_results("-", "-", "-")
                    player = 1
                    break
                n += 1
print(tiles)
print(calc_results())

# print(print_board(player1.field))
