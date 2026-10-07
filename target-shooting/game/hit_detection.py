
"""
hit_detection: figures out whether a click landed on a target.
"""


def check_hit(targets, click_pos):
    """
    Returns the target that was clicked, or None if the click missed
    every target.
    """
    for target in targets:
        x, y = target.x, target.y
        radius = target.radius

        dx = click_pos[0] - x
        dy = click_pos[1] - y

        if dx * dx + dy * dy <= radius * radius:
            return target

    return None

