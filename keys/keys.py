import pygame
import sys

class Keys:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Keys')

		# Settings
		self.screen_width = 900
		self.screen_height = 600

		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

	def run_game(self):
		while True:
			self._check_events()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				print(event.key)

if __name__ == '__main__':
	k = Keys()
	k.run_game()