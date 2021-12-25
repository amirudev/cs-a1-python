import pygame
import sys

from settings import Settings
from player import Player

class GuyBros:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Guy Bros')

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.player = Player(self)

	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.player.blitme()

		pygame.display.flip()

if __name__ == '__main__':
	p = GuyBros()
	p.run_game()