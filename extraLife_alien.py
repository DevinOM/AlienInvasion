import pygame
from pygame.sprite import Sprite


class ExtraLifeAlien(Sprite):
    """A class to represent a single extra life alien"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/extraLifeAlienTransparent.bmp')
        self.rect = self.image.get_rect()

        # Start the extra life alien at the top
        self.rect.x = 650
        self.rect.y = 95

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.extra_alien_speed * self.settings.extra_alien_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_alien(self):
        """Center the ship on the screen."""
        self.rect.y = 95
        self.rect.x = 650