import pygame

class Player:
	def __init__(self, p_game):
		self.screen = p_game.screen
		self.screen_rect = p_game.screen.get_rect()

		self.image = pygame.image.load('images/character.bmp')
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom

	def blitme(self):
		self.screen.blit(self.image, self.rect)