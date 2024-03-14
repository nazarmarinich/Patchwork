from typing import Type

import numpy as np
import math
import pygame
import uuid
import random
import time

# Mode
VISUAL = True
RANDOM = True
TILES = np.arange(0, 33)

# Bonus patches on the game timeline
PATCHES = [26, 32, 38, 44, 50]
# Game timeline
timeline = np.arange(1, 54)

patchwork_pieces = [
    {"ID": 0, "Name": "ladder", "Square": 5, "Buttons": 3, "Cost_b": 10, "Cost_t": 4, 'Weight': 0.0,
     "Shape": [[1, 1, 0], [0, 1, 1], [0, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 1, "Name": "corner5", "Square": 5, "Buttons": 2, "Cost_b": 10, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[1, 1, 1, 1], [0, 0, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 2, "Name": "corner10", "Square": 4, "Buttons": 2, "Cost_b": 4, "Cost_t": 6, 'Weight': 0.0,
     "Shape": [[1, 1, 1], [0, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 3, "Name": "line3", "Square": 3, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 4, "Name": "strange6", "Square": 6, "Buttons": 0, "Cost_b": 2, "Cost_t": 1, 'Weight': 0.0,
     "Shape": [[0, 0, 1, 0], [1, 1, 1, 1], [0, 1, 0, 0]], "Color": (0, 0, 0)},
    {"ID": 5, "Name": "line4", "Square": 4, "Buttons": 1, "Cost_b": 3, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[1, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 6, "Name": "z2", "Square": 4, "Buttons": 1, "Cost_b": 3, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 0], [0, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 7, "Name": "cross4", "Square": 7, "Buttons": 1, "Cost_b": 1, "Cost_t": 4, 'Weight': 0.0,
     "Shape": [[0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0]], "Color": (0, 0, 0)},
    {"ID": 8, "Name": "line5", "Square": 5, "Buttons": 1, "Cost_b": 7, "Cost_t": 1, 'Weight': 0.0,
     "Shape": [[1, 1, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 9, "Name": "square", "Square": 4, "Buttons": 2, "Cost_b": 6, "Cost_t": 5, 'Weight': 0.0,
     "Shape": [[1, 1], [1, 1]], "Color": (0, 0, 0)},
    {"ID": 10, "Name": "trapezia7", "Square": 6, "Buttons": 2, "Cost_b": 7, "Cost_t": 4, 'Weight': 0.0,
     "Shape": [[0, 1, 1, 0], [1, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 11, "Name": "corner2", "Square": 4, "Buttons": 1, "Cost_b": 4, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 1], [0, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 12, "Name": "fat_z", "Square": 6, "Buttons": 0, "Cost_b": 4, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 1, 0], [0, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 13, "Name": "z8", "Square": 6, "Buttons": 3, "Cost_b": 8, "Cost_t": 6, 'Weight': 0.0,
     "Shape": [[1, 0, 0], [1, 1, 1], [0, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 14, "Name": "n", "Square": 5, "Buttons": 0, "Cost_b": 1, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 1], [1, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 15, "Name": "cross0", "Square": 6, "Buttons": 1, "Cost_b": 0, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[0, 1, 0, 0], [1, 1, 1, 1], [0, 1, 0, 0]], "Color": (0, 0, 0)},
    {"ID": 16, "Name": "z5", "Square": 5, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 1, 1], [0, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 17, "Name": "corner3", "Square": 3, "Buttons": 0, "Cost_b": 3, "Cost_t": 1, 'Weight': 0.0,
     "Shape": [[1, 1], [0, 1]], "Color": (0, 0, 0)},
    {"ID": 18, "Name": "z7", "Square": 4, "Buttons": 3, "Cost_b": 7, "Cost_t": 6, 'Weight': 0.0,
     "Shape": [[1, 1, 0], [0, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 19, "Name": "corner1", "Square": 3, "Buttons": 0, "Cost_b": 1, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[1, 1], [0, 1]], "Color": (0, 0, 0)},
    {"ID": 20, "Name": "corner4", "Square": 5, "Buttons": 1, "Cost_b": 3, "Cost_t": 4, 'Weight': 0.0,
     "Shape": [[0, 1, 0, 0], [1, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 21, "Name": "long_z", "Square": 5, "Buttons": 1, "Cost_b": 2, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[1, 1, 0, 0], [0, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 22, "Name": "big_t", "Square": 6, "Buttons": 2, "Cost_b": 7, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]], "Color": (0, 0, 0)},
    {"ID": 23, "Name": "small_t", "Square": 5, "Buttons": 2, "Cost_b": 5, "Cost_t": 5, 'Weight': 0.0,
     "Shape": [[1, 0, 0], [1, 1, 1], [1, 0, 0]], "Color": (0, 0, 0)},
    {"ID": 24, "Name": "huge_z", "Square": 6, "Buttons": 0, "Cost_b": 1, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 25, "Name": "line2", "Square": 2, "Buttons": 0, "Cost_b": 2, "Cost_t": 1, 'Weight': 0.0,
     "Shape": [[1, 1]], "Color": (0, 0, 0)},
    {"ID": 26, "Name": "trapezia2", "Square": 4, "Buttons": 0, "Cost_b": 2, "Cost_t": 2, 'Weight': 0.0,
     "Shape": [[0, 1, 0], [1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 27, "Name": "H", "Square": 7, "Buttons": 0, "Cost_b": 2, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[1, 0, 1], [1, 1, 1], [1, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 28, "Name": "trapezia8", "Square": 8, "Buttons": 1, "Cost_b": 5, "Cost_t": 3, 'Weight': 0.0,
     "Shape": [[0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 0]], "Color": (0, 0, 0)},
    {"ID": 29, "Name": "corner6", "Square": 6, "Buttons": 3, "Cost_b": 10, "Cost_t": 5, 'Weight': 0.0,
     "Shape": [[1, 1, 1, 1], [0, 0, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 30, "Name": "long_n", "Square": 6, "Buttons": 1, "Cost_b": 1, "Cost_t": 5, 'Weight': 0.0,
     "Shape": [[1, 0, 0, 1], [1, 1, 1, 1]], "Color": (0, 0, 0)},
    {"ID": 31, "Name": "zz", "Square": 6, "Buttons": 2, "Cost_b": 3, "Cost_t": 6, 'Weight': 0.0,
     "Shape": [[0, 1, 0], [1, 1, 1], [1, 0, 1]], "Color": (0, 0, 0)},
    {"ID": 32, "Name": "cross5", "Square": 5, "Buttons": 2, "Cost_b": 5, "Cost_t": 4, 'Weight': 0.0,
     "Shape": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "Color": (0, 0, 0)},
]
for tile_id in TILES:
    tile_info = patchwork_pieces[tile_id]
    tile_info['Color'] = (random.randint(25, 225), random.randint(25, 225), random.randint(25, 225))


class Game:

    def __init__(self):
        self.id = uuid.uuid4().hex
        self.visual = VISUAL
        self.patches = [26, 32, 38, 44, 50]
        self.timeline = np.arange(1, 54)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.tiles = tiles_shuffle(TILES)
        self.sc = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.game_result = Type[str]

    def calc_game_results(self, player):
        p1_result = self.player1.buttons - (81 - min(self.player1.square, 81)) * 2
        p2_result = self.player2.buttons - (81 - min(self.player2.square, 81)) * 2
        if p1_result > p2_result:
            game_result = "\nРезультат игрока 1: " + str(p1_result) + "\nРезультат игрока 2: " + str(
                p2_result) + "\nПобедил игрок 1!"
        elif p1_result == p2_result and player == 1:
            game_result = "\nРезультат игрока 1: " + str(p1_result) + "\nРезультат игрока 2: " + str(
                p2_result) + "\nПобедил игрок 1!"
        else:
            game_result = "\nРезультат игрока 1: " + str(p1_result) + "\nРезультат игрока 2: " + str(
                p2_result) + "\nПобедил игрок 2!"
        print(game_result)
        self.game_result = game_result.replace('\n', '  ')

    def emulate_game(self):
        # patches order
        tiles = self.tiles

        player = 1
        while self.player1.time_count + self.player2.time_count > 0:
            # time.sleep(0.15)
            if player == 1:
                # print(tiles)
                while self.player1.time_count >= self.player2.time_count:
                    n = 0
                    # Player 1 uses greedy sorting
                    tiles_s = self.player1.greedy_sorting(tiles[0:3])
                    for i in tiles_s[0:3]:
                        # for i in tiles[0:3]:
                        tile = patchwork_pieces[i]
                        tile_to_place = np.array(tile['Shape'])
                        if (self.player1.buttons >= tile['Cost_b'] and self.player1.time_count > 0
                                and self.player1.place_tile(tile_to_place, tile['Color'], game.sc) is not None):
                            self.player1.tiles.append(tile)
                            tiles = np.roll(tiles, -np.where(tiles == i)[0][0])
                            tiles = tiles[1::]
                            # print(tiles)
                            self.player1.buttons -= tile['Cost_b']
                            self.player1.buttons_aimed += tile['Buttons']
                            self.player1.square += tile['Square']
                            self.player1.calc_aimed_patch(tile['Cost_t'])
                            self.player1.calc_aimed_buttons(tile['Cost_t'])
                            self.player1.time_count -= tile['Cost_t']
                            self.player1.print_turn_results(tile['ID'], tile['Cost_b'], tile['Cost_t'])
                            if self.player1.time_count < self.player2.time_count:
                                player = 2
                            break
                        if n == 2 and self.player1.time_count >= self.player2.time_count:
                            a = (self.player1.time_count - self.player2.time_count + 1)
                            self.player1.buttons += a
                            self.player1.calc_aimed_patch(a)
                            self.player1.calc_aimed_buttons(a)
                            self.player1.time_count -= a
                            self.player1.print_turn_results("-", "-", "-")
                            player = 2
                            break
                        n += 1
            else:
                # print(tiles)
                while self.player2.time_count >= self.player1.time_count:
                    n = 0
                    # Player 2 uses greedy sorting
                    # tiles_s = self.player1.greedy_sorting(tiles[0:3])
                    # for i in tiles_s[0:3]:
                    for i in tiles[0:3]:
                        tile = patchwork_pieces[i]
                        tile_to_place = np.array(tile['Shape'])
                        if (self.player2.buttons >= tile['Cost_b'] and self.player2.time_count > 0
                                and self.player2.place_tile(tile_to_place, tile['Color'], game.sc) is not None):
                            self.player2.tiles.append(tile)
                            tiles = np.roll(tiles, -np.where(tiles == i)[0][0])
                            tiles = tiles[1::]
                            # print(tiles)
                            self.player2.buttons -= tile['Cost_b']
                            self.player2.buttons_aimed += tile['Buttons']
                            self.player2.square += tile['Square']
                            self.player2.calc_aimed_patch(tile['Cost_t'])
                            self.player2.calc_aimed_buttons(tile['Cost_t'])
                            self.player2.time_count -= tile['Cost_t']
                            self.player2.print_turn_results(tile['ID'], tile['Cost_b'], tile['Cost_t'])
                            if self.player2.time_count < self.player1.time_count:
                                player = 1
                            break
                        if n == 2 and self.player2.time_count >= self.player1.time_count:
                            a = (self.player2.time_count - self.player1.time_count + 1)
                            self.player2.buttons += a
                            self.player2.calc_aimed_patch(a)
                            self.player2.calc_aimed_buttons(a)
                            self.player2.time_count -= a
                            self.player2.print_turn_results("-", "-", "-")
                            player = 1
                            break
                        n += 1
        print(tiles)
        print(Game.calc_game_results(self, player))

        print(print_board(self.player1.field))
        print(print_board(self.player2.field))

    def visual_run(self):
        pygame.init()
        pro_version = "1.0.0"
        pygame.display.set_caption("Patchwork MNG " + pro_version)
        clock = pygame.time.Clock()
        fps = 60
        game_font = pygame.font.SysFont('Calibri', 16)
        tile_size = 7  # tile size
        margin = 1  # margin between tiles
        x, y = 50, 10  # initial coordinates

        # draw game patches (tiles)
        for idx, i in enumerate(self.tiles):
            tile = patchwork_pieces[i]
            shape = tile["Shape"]
            draw_tile(tile["Shape"], tile["Color"], x, 10, tile_size, self.sc)
            pygame.display.update()
            x += (len(shape[0]) * (tile_size + margin))

        pygame.draw.rect(self.sc, 'White', (48, 68, 278, 278), 4)
        pygame.draw.rect(self.sc, 'White', (348, 68, 278, 278), 4)
        p1_signboard = game_font.render('Player 1', 1, "White")
        p2_signboard = game_font.render('Player 2', 1, "White")
        self.sc.blit(p1_signboard, (48, 48))
        self.sc.blit(p2_signboard, (348, 48))
        pygame.display.update()

        self.emulate_game()

        visual_game_result = game_font.render(self.game_result, 1, "White")
        self.sc.blit(visual_game_result, (48, 348))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        exit()

            clock.tick(fps)


class Player:
    def __init__(self, number):
        self.number = number
        self.time_count = 53
        self.buttons_aimed = 0
        self.buttons = 5
        self.tiles = []
        self.field = np.zeros((9, 9), dtype=int)
        self.field_to_draw = np.zeros((9, 9), dtype=int)
        self.square = 0

    def place_tile(self, tile, color, surface):
        # mirroring
        for _ in range(2):
            # for each rotate position
            for _ in range(4):
                tile_rows, tile_cols = tile.shape
                mask = tile == 1
                for row in range(9):
                    for col in range(9):
                        # check if there is a place for a tile
                        if row + tile_rows <= 9 and col + tile_cols <= 9:
                            # check if it is possible to place
                            if np.all(self.field[row:row + tile_rows, col:col + tile_cols][mask] == 0):
                                self.field[row:row + tile_rows, col:col + tile_cols] += tile
                                self.field_to_draw[row:row + tile_rows, col:col + tile_cols] += tile
                                if VISUAL:
                                    if self.number == 1:
                                        draw_tile(self.field_to_draw, color, 50, 70, 30, surface)
                                    else:
                                        draw_tile(self.field_to_draw, color, 350, 70, 30, surface)
                                    self.field_to_draw[row:row + tile_rows, col:col + tile_cols] -= tile
                                    pygame.display.update()
                                return not None
                # rotate 90 degrees
                tile = np.rot90(tile)
            tile = np.fliplr(tile)
        return None

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
        - time_cost (int): Time cost of the tile being placed.
        Returns:
        - square_sum (int): Updated number of square
        """
        global PATCHES
        for tn in timeline[(53 - self.time_count):(53 - self.time_count + time_cost)]:
            if tn in PATCHES:  # Check if the player time position is an aimed button position
                self.square += 1
                Player.place_tile(self, np.array([[1]]), 'White', surface=game.sc)
                Player.print_turn_results(self, "99", "-", "-")
                PATCHES = np.delete(PATCHES, 0)

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

    def print_turn_results(self, tile, buttons, time_spent):
        # Print the player actions

        print("Игрок: " + str(self.number) + " BB:" + str(self.buttons) + "/" + str(self.buttons_aimed) + " BT:"
              + str(self.time_count) + " Square: " + str(self.square) + " Buttons: "
              + str(buttons) + " Time: " + str(time_spent) + " Tile: " + str(tile))


# _______________functions _______________________

def tiles_shuffle(tiles):
    if RANDOM:
        np.random.shuffle(tiles)
    while tiles[32] != 25:
        tiles = np.roll(tiles, 1)
    return tiles


def print_board(board):
    """
    Print the game board.
    """
    for row in board:
        print("  ".join(str(cell) for cell in row))


def draw_tile(shape, color, x, y, tile_size, surface):
    for row_idx, row_cell in enumerate(shape):
        for col_idx, cell in enumerate(row_cell):
            if cell == 1:
                tile_rect = pygame.Rect(x + col_idx * tile_size, y + row_idx * tile_size, tile_size, tile_size)
                pygame.draw.rect(surface, color, tile_rect)
    x += (len(shape[0]) * (tile_size + 1))


if __name__ == '__main__':
    if VISUAL is True:
        game = Game()
        Game.visual_run(game)
    else:
        game = Game()
        game.emulate_game()
