import pygame
import sys

from settings import Settings
from star import Star

class Stars:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Stars')

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.stars = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		while True:
			self._update_screen()
			self._check_events()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _create_fleet(self):
		star = Star(self)
		star_width = star.rect.width
		star_height = star.rect.height
		available_space_x = self.settings.screen_width - ( 2 * star_width )
		available_space_y = self.settings.screen_height / 2
		number_star_x = int(available_space_x // ( 2 * star_width ))
		number_star_y = int(available_space_y // ( 2 * star_height ))

		for index_star_y in range(number_star_y):
			for index_star_x in range(number_star_x):
				self._create_star(index_star_x, index_star_y)

	def _create_star(self, index_star_x, index_star_y):
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = star_width + 2 * star_width * index_star_x
		star.y = star_height + 2 * star_height * index_star_y
		star.rect.x = star.x
		star.rect.y = star.y

		self.stars.add(star)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)

		self.stars.draw(self.screen)
		pygame.display.flip()

if __name__ == '__main__':
	s = Stars()
	s.run_game()