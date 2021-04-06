import random


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1350
        self.screen_height = 900
        self.bg_color = (25, 25, 25)

        # Ship settings
        # self.ship_speed = 1.5
        self.ship_limit = 2

        # Bullet settings
        # self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (180, 180, 180)
        self.bullets_allowed = 3

        # Fire bullet settings
        self.fire_bullet_width = 3.0
        self.fire_bullet_height = 7.5
        self.fire_bullet_color = (255, 100, 100)
        self.fire_bullets_allowed = 1

        # Alien settings
        # self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1.0

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.speedup_extra_scale = 1.5

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.fire_bullet_speed = 3.0

        self.alien_speed = 1.0
        self.extra_alien_speed = 1.75

        # Scoring
        self.alien_points = 50

        # fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1
        self.extra_alien_direction = -1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fire_bullet_speed *= self.speedup_extra_scale
        self.alien_speed *= self.speedup_scale
        self.extra_alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

