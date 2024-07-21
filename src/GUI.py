import tkinter as tk
from typing import Type

from game_objects import Player, Obstacle
from game import Game


class GUI:
    def __init__(self, w: int, h: int) -> None:
        self.w = w
        self.h = h

        self.root = tk.Tk(screenName="placeholder")
        self.game = Game(w, h, 100, 100, 30)

        self.root.bind("<Key>", self.game.event_handler)

        self.canvas = tk.Canvas(self.root, height=h, width=w, bg="lightblue")
        self.canvas.pack()

    def draw_player(self):  # center coordinates, radius
        x = self.game.player.x
        y = self.game.player.y
        r = self.game.player.r

        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill="red")

    def draw_obstacle(self, obstacle: Type[Obstacle]):  # center coordinates, radius
        x = obstacle.x
        h = obstacle.h
        w = obstacle.w

        x0 = x - w // 2
        y0 = self.h - h
        x1 = x + w // 2
        y1 = self.h
        return self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")

    def draw_score(self):
        self.canvas.create_text(
            self.w // 2,
            50,
            text=self.game.score,
            fill="black",
            font=("Helvetica 30 bold"),
        )

    def draw(self):
        self.draw_score()
        self.draw_player()
        for o in self.game.obstacles:
            self.draw_obstacle(o)

    def menu(self):
        pass

    def game_over(self):
        pass
