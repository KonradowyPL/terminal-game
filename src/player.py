from src.gui import RenderableComponent


class Player(RenderableComponent):
    def __init__(self, x: int = 1, y: int = 1, maxHelath=10, maxArrows=10, money=0, damage=0):
        image = [" @ ",
                 " |c",
                 " | ",
                 "/ \\",
                 ]
        self.empty =["   "] * 4
        self.maxHealth = maxHelath
        self.health = self.maxHealth
        self.maxArrows = maxArrows
        self.arrows = self.maxArrows
        self.money = money
        self.damage = damage
        self.kills = 0
        self.infinity = 9999999999
        super().__init__(image, x, y)

    def move(self, charDir):
        oldX = self.x

        if charDir == "M":  # right
            self.x += 2
        elif charDir == "K":  # left
            self.x -= 2

        if self.x >= self.renderer.len*4 or self.x < 0:
            self.x = oldX
