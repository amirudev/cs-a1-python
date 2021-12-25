import pygame
import sys

from ship import Ship
from settings import Settings
from bullet import Bullet

class SidewayShooter():
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("Sideway Shooter")

		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullet()
	
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		if len(self.bullets) < 2:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullet(self):
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.settings.screen_width:
				self.bullets.remove(bullet)
			print(len(self.bullets))

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		pygame.display.flip()

if __name__ == '__main__':
	ss = SidewayShooter()
	ss.run_game()