from sys import platform
from gui import RenderableComponent
from enemy import Enemy


class Projectile(RenderableComponent):
    def __init__(self, image: list[str], x: int, y: int, vx: int = 0, vy: int = 0, empty=[], damage=1,  **kwargs):
        self.vx = vx
        self.vy = vy
        self.empty = empty
        self.damage = damage
        super().__init__(image, x, y, **kwargs)

    def frame(self):
        newX = self.vx + self.x
        newY = self.vy + self.y

        # out of bounds
        if newX >= self.renderer.len*4 or newX < 0 or newY >= self.renderer.height*4 or newY < 0:
            return self.renderer.removeFeature(self)

        # check entity collision
        for entity in self.renderer.entities:
            if not issubclass(type(entity), Enemy):
                continue
            # player collision:
            if abs(newX - entity.x) < self.vx:
                self.renderer.removeFeature(self)
                entity.health -= self.damage
                return

        self.x = newX
        self.y = newY


class Arrow(Projectile):
    def __init__(self, x: int, y: int, vx: int = 0, vy: int = 0, damage: int = 1, ** kwargs):
        image = ["--=>"]
        empty = ["    "]

        super().__init__(image, x, y, vx, vy, empty, damage, ** kwargs)
