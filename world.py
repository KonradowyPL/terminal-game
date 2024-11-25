from colorama import Fore, Style

from gui import RenderableComponent, Renderer


class World(Renderer):
    def __init__(self) -> None:
        super().__init__(minHeight=0, minWidth=0, features=[])

        self.len = 40
        self.height = 5
        self.arr = []
        self.tiles = []
        for x in range(self.len):
            height = 1
            arr = [1] * height
            arr.extend([0] * (self.height - height))
            self.arr.append(arr)

        for index, collumn in enumerate(self.arr):
            self.tiles.append([])
            for row, tile in enumerate(collumn):
                tile = Tile(index, self.height - row, tile)
                self.tiles[index].append(Tile)
                self.addFeature(tile)
        self.render()

    def getBlockAt(self, x: int, y: int):
        return self.arr[x][y]


class Tile(RenderableComponent):
    def __init__(self, collumn, row, tile):
        if tile == 0:
            image = ["    "] * 4
        else:
            image = [Fore.LIGHTGREEN_EX + ",   ", "%@%@", Fore.RED +
                     Style.DIM + "@@#$", "&$&#", "%@%@", "@@#$", "&$&#", "%@%@"]

        super().__init__(image, collumn*4, row*4-4)
