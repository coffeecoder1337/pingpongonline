import config
import pygame
from random import choice
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.size = config.BALL_SIZE
		self.image = pygame.Surface(self.size)
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.basespeed = 5
		self.speed = self.basespeed
		self.direction = [choice([-1, 1]), choice([-1, 1])]


	def check_collide(self, players):
		for player in players:
			if pygame.sprite.collide_rect(player, self):
				self.direction[0] = -self.direction[0]
			if any([self.rect.top < 0, self.rect.bottom > config.SCREEN_SIZE[1]]):
				self.direction[1] = -self.direction[1]


	def update(self, players):
		self.rect.x += self.speed * self.direction[0]
		self.rect.y += self.speed * self.direction[1]
		self.check_collide(players)



