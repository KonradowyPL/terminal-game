import os
import signal
import sys


class RenderableComponent:
    def __init__(self, image: list[str], x: int, y: int, **kwargs):
        self.image = image
        self.x = x
        self.y = y
        self.renderer: Renderer

        self.update(**kwargs)

    def update(self, **kwargs):
        # on update rerender
        self.__dict__.update(kwargs)
        self.render()

    def move_cursor(self, row, col):
        # util function to move cursor
        sys.stdout.write(f"\x1b[{row};{col}H")

    def render(self):
        col = self.x
        row = self.y

        # loop for each row and print
        for y, imgRow in enumerate(self.image):
            self.move_cursor(row + y, col)
            sys.stdout.write(imgRow)

    def frame(self):
        pass


class Renderer:
    def __init__(self, minHeight: int, minWidth: int, features: list[RenderableComponent]):
        self.minHeight = minHeight
        self.minWidth = minWidth
        self.features = features
        self.entities = []

    def render(self):
        for feature in self.features:
            feature.render()
        sys.stdout.flush()

    def addFeature(self, feature: RenderableComponent):
        feature.renderer = self
        self.features.append(feature)

    def removeFeature(self, feature):
        if feature in self.features:
            self.features.pop(self.features.index(feature))
        if feature in self.entities:
            self.entities.pop(self.entities.index(feature))

    def addEntity(self, feature: RenderableComponent):
        feature.renderer = self
        self.features.append(feature)
        self.entities.append(feature)
