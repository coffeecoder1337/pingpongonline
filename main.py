import pygame
from pygame.locals import *

pygame.init()


class Game:
	def __init__(self):
		pygame.display.set_caption("Ping Pong Online")
		self.size = (1000, 500)
		self.screen = pygame.display.set_mode(self.size)
		self.timer = pygame.time.Clock()
		self.all_objects = pygame.sprite.Group()
		self.is_running = True


	def event(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				self.is_running = False


	def draw(self):
		self.screen.fill((0, 0, 0))
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

