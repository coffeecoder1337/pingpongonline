import config
import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.start_position = (x, y)
		self.size = config.PADDLE_SIZE
		self.image = pygame.Surface(self.size)
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.centery = y
		self.speed = 5
		self.up = False
		self.down = False


	def check_collide(self):
		if self.rect.bottom > config.SCREEN_SIZE[1]:
			self.down = False
		if self.rect.top < 0:
			self.up = False


	def respawn(self):
		self.rect.x, self.rect.y = self.start_position


	def update(self):
		if self.up:
			self.rect.y -= self.speed
			self.check_collide()

		if self.down:
			self.rect.y += self.speed
			self.check_collide()



class AI_Player(Player):
	def __init__(self, x, y):
		Player.__init__(self, x, y)

	def move(self, ball):
		self.rect.centery = ball.rect.centery
		self.check_collide()

