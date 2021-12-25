import pygame
import sys

from settings import Settings
from rain import Rain

class Raindrops:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Raindrops')

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.rains = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		while True:
			self._check_event()
			self._update_screen()
			self._update_rain()

	def _check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _create_fleet(self):
		rain = Rain(self)
		rain_width = rain.rect.width
		# rain_height = rain.rect.height
		available_space_x = self.settings.screen_width - ( 2 * rain_width )
		count_rain_x = available_space_x // ( 2 * rain_width )

		for rain_x in range(count_rain_x):
			self._create_rain(rain_x)

	def _create_rain(self, rain_x):
		rain = Rain(self)
		rain_width, rain_height = rain.rect.size

		rain.x = rain_width + 2 * rain_width * rain_x
		rain.rect.x = rain.x

		self.rains.add(rain)

	def _update_rain(self):
		self.rains.update()
		for rain in self.rains.copy():
			if rain.rect.bottom >= self.settings.screen_height:
				self.rains.remove(rain)
			print(len(self.rains))

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.rains.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	r = Raindrops()
	r.run_game()