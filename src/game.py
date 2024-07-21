import random

from game_objects import Player, Obstacle


class Game:
    def __init__(self, w: int, h: int, px: int, py: int, pr: int) -> None:
        self.h = h
        self.w = w

        self.obstacle_width = 80
        self.obstacle_max_height = h - h // 3

        self.player = Player(h, px, py, pr)

        self.max_obstacles = w // 400
        self.obstacles = [self.random_obstacle()]

        self.score = 0

        self.is_over = False

    def update(self):
        if not self.obstacles:
            self.obstacles.append(self.random_obstacle())

        self.player.update()
        for i, obstacle in enumerate(self.obstacles):
            obstacle.update()
            # Check if obstacle is off the screen
            if obstacle.x <= -obstacle.w // 2:
                self.score += 1
                del self.obstacles[i]

            # If last obstacle and far enough from right edge, add new obstacle
            if i == len(self.obstacles) - 1 and i != self.max_obstacles:
                if obstacle.x <= self.w - self.w // self.max_obstacles:
                    self.obstacles.append(self.random_obstacle())

        self.is_over = self.collision()

    def random_obstacle(self):
        return Obstacle(
            self.w,
            0,
            self.obstacle_width,
            random.randint(self.h // 2, self.obstacle_max_height),
        )

    def collision(self):
        px, py = self.player.get_pos()
        r = self.player.r

        # Check player to obstacle collision
        for obstacle in self.obstacles:
            ox, _ = obstacle.get_pos()
            ow = obstacle.w
            oh = obstacle.h

            if (ox + ow // 2) - (px + r) <= 0 and py >= oh:
                return True

        # Check floor collision
        if self.player.y >= self.h:
            return True

        return False
    
    def event_handler(self, event):
        if event.keysym == "space":
            self.player.jump()

