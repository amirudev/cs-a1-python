import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self, ss_game):
		super().__init__()
		self.screen = ss_game.screen

		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		self.rect.size = ( self.rect.x, self.rect.y )

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)