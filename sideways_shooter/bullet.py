import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, ss_game):
		super().__init__()
		self.screen = ss_game.screen
		self.settings = ss_game.settings
		self.color = (0, 0, 0)

		self.rect = pygame.Rect(0, 0, 15, 3)
		self.rect.midright = ss_game.ship.rect.midright

		self.x = float(self.rect.x)

	def update(self):
		self.x += 1
		self.rect.x = self.x

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)