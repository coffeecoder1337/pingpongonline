import ball
import config
import pygame
import player
from pygame.locals import *


pygame.init()


class Game:
	def __init__(self):
		pygame.display.set_caption("Ping Pong Online")
		self.size = config.SCREEN_SIZE
		self.screen = pygame.display.set_mode(self.size)
		self.timer = pygame.time.Clock()
		self.all_objects = pygame.sprite.Group()
		self.is_running = True
		self.main_paddle = player.Player(3, config.SCREEN_SIZE[1]/2)
		self.ball = ball.Ball(config.SCREEN_SIZE[0]/2, config.SCREEN_SIZE[1]/2)
		self.all_objects.add(self.main_paddle)
		self.all_objects.add(self.ball)


	def event(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				self.is_running = False

			if e.type == KEYDOWN:
				if e.key in [K_UP, K_w]:
					self.main_paddle.up = True
				if e.key in [K_DOWN, K_s]:
					self.main_paddle.down = True

			if e.type == KEYUP:
				if e.key in [K_UP, K_w]:
					self.main_paddle.up = False
				if e.key in [K_DOWN, K_s]:
					self.main_paddle.down = False


	def draw(self):
		self.screen.fill((0, 0, 0))
		self.main_paddle.update()
		self.ball.update([self.main_paddle])
		self.all_objects.draw(self.screen)
		self.timer.tick(60)
		pygame.display.update()


	def loop(self):
		while self.is_running:
			self.event()
			self.draw()


	def run(self):
		self.loop()


if __name__ == '__main__':
	game = Game()
	game.run()

