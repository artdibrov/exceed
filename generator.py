import random

class Generator:

    def build(self, width, height):

        grid = [

            ["#" for _ in range(width)]

            for _ in range(height)

        ]

        for y in range(2, height - 2):

            for x in range(2, width - 2):

                if random.random() > 0.35:

                    grid[y][x] = "."

        grid[height // 2][width // 2] = "@"

        grid[3][6] = "~"

        grid[8][20] = "^"

        grid[5][14] = "+"

        return grid
