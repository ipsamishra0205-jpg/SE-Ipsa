
"""
GameEngine: owns the targets and handles player clicks.

Targets move continuously and bounce off the play-area edges.
"""

import random

from game.target import Target
from game.hit_detection import check_hit
from game.renderer import WIDTH, HEIGHT

NUM_TARGETS = 3
TARGET_RADIUS = 28


class GameEngine:
    def __init__(self):
        self.targets = [
            self._random_target() for _ in range(NUM_TARGETS)
        ]
        self.hits = 0
        self.misses = 0

    def _random_target(self):
        x = random.randint(
            TARGET_RADIUS + 10, WIDTH - TARGET_RADIUS - 10
        )
        y = random.randint(
            TARGET_RADIUS + 10, HEIGHT - TARGET_RADIUS - 10
        )
        return Target(x, y, radius=TARGET_RADIUS)

    def handle_click(self, pos):
        target = check_hit(self.targets, pos)

        if target is not None:
            self.hits += 1
            self.targets.remove(target)
            self.targets.append(self._random_target())
        else:
            self.misses += 1

    def update(self):
        """Move every target once per game frame."""
        for target in self.targets:
            target.move(WIDTH, HEIGHT)

    def draw(self, surface, font):
        """Draw targets and the current hit/miss counts."""
        from game import renderer

        renderer.draw_scene(surface, self.targets)
        renderer.draw_text(
            surface,
            font,
            f"Hits: {self.hits}  Misses: {self.misses}",
            (10, 10),
        )