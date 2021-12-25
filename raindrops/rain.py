import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	def __init__(self, r_game):
		super().__init__()

		self.screen = r_game.screen
		self.settings = r_game.settings

		self.image = pygame.image.load('images/raindrop.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.rect.size = (self.rect.x, self.rect.y)

		self.y = float(self.rect.y)

	def update(self):
		self.y += self.settings.raindrop_speed
		self.rect.y = self.y