from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_pos(self):
        return (self.x, self.y)

    @abstractmethod
    def update(self):
        pass


class Player(Entity):
    def __init__(self, gh: int, x: int = 100, y: int = 100, r: int = 30) -> None:
        super().__init__(x, y)
        # Game height
        self.gh = gh

        # Radius of object
        self.r = r

        # Vertical velocity and acceleration
        self.v = 0
        self.a = 4

    def jump(self):
        # Set velocity, disregarding current velocity
        self.v = 30

    def update(self):
        self.v = max(self.v - self.a, -50)

        new_y = self.y - self.v
        new_y = max(0, new_y)
        new_y = min(self.gh, new_y)
        self.y = new_y

class Obstacle(Entity):
    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super().__init__(x, y)

        # Dimensions
        self.h = h
        self.w = w

        # Velocity is constant
        self.v = 15

    def update(self):
        self.x -= self.v
