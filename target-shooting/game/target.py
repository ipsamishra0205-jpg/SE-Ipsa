
"""
Target: a circular target that moves and bounces within the play area.
(x, y) is the CENTER of the circle.
"""

import random
import pygame


class Target:
    def __init__(self, x, y, radius=28, color=(230, 90, 70)):
        self.x = float(x)
        self.y = float(y)
        self.radius = radius
        self.color = color

        # Different targets get different speeds and directions.
        speed = random.choice([2.0, 3.0, 4.0])
        self.dx = random.choice([-1, 1]) * speed
        self.dy = random.choice([-1, 1]) * random.choice([1.5, 2.5, 3.5])

    def move(self, width, height):
        """Move the target and bounce off the play-area edges."""
        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius <= 0:
            self.x = self.radius
            self.dx = abs(self.dx)
        elif self.x + self.radius >= width:
            self.x = width - self.radius
            self.dx = -abs(self.dx)

        if self.y - self.radius <= 0:
            self.y = self.radius
            self.dy = abs(self.dy)
        elif self.y + self.radius >= height:
            self.y = height - self.radius
            self.dy = -abs(self.dy)

    def get_bounding_rect(self):
        """Return the square bounding box around the circle."""
        return pygame.Rect(
            round(self.x - self.radius),
            round(self.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )