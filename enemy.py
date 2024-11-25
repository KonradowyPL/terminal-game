from gui import RenderableComponent
from colorama import Fore
from endgame import end


class Enemy(RenderableComponent):
    def __init__(self, image: list[str], x: int, y: int, vx: int, player, health, strenght, value, empty=[],  **kwargs):
        self.vx = vx
        self.empty = empty
        self.player = player
        self.health = health
        self.value = value
        self.strenght = strenght
        super().__init__(image, x, y, **kwargs)

    def frame(self):
        newX = self.vx + self.x
        newY = self.y

        img = self.image
        self.image = self.empty
        self.render()

        # died
        if self.health <= 0:
            self.player.money += self.value
            return self.renderer.removeFeature(self)

        # loose
        if newX < 0:
            end(self.player)

        # player collision:
        if abs(self.player.x - newX) < 4:
            self.player.health -= self.strenght

        # out of bounds
        if newX >= self.renderer.len*4 or newX < 0 or newY >= self.renderer.height*4 or newY < 0:
            return self.renderer.removeFeature(self)

        self.image = img
        self.x = newX
        self.y = newY


class Zomie(Enemy):
    def __init__(self,  x: int, y: int, vx: int, player, **kwargs):
        image = [
            "   ",
            "   ",
            Fore.GREEN + " 0 " + Fore.RESET,
            Fore.GREEN + "-| " + Fore.RESET,
            Fore.GREEN + "/ \\" + Fore.RESET]
        empty = ['   '] * 5
        health = 1
        value = 1
        strenght = 1
        super().__init__(image, x, y, vx, player, health, value, strenght,  empty, **kwargs)


class Spider(Enemy):
    def __init__(self,  x: int, y: int, vx: int, player, **kwargs):
        image = ["      ",
                 "      ",
                 "      ",
                 " _"+Fore.RED+"^^"+Fore.RESET+"_ ",
                 "//||\\",
                 ]
        empty = ['      '] * 5
        health = 3
        value = 2
        strenght = 2
        vx = -2
        super().__init__(image, x, y, vx, player, health, value, strenght,  empty, **kwargs)


class Creeper(Enemy):
    def __init__(self,  x: int, y: int, vx: int, player, **kwargs):
        image = ["   ", "   ",
                 Fore.LIGHTGREEN_EX + " # " + Fore.RESET,
                 Fore.LIGHTGREEN_EX + " # " + Fore.RESET,
                 Fore.LIGHTGREEN_EX + "/ \\" + Fore.RESET,
                 ]
        empty = ['   '] * 5
        health = 4
        value = 7
        strenght = 10
        vx = -2
        super().__init__(image, x, y, vx, player, health, value, strenght,  empty, **kwargs)
