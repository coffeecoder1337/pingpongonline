import ball
import config
import pygame
import player
from pygame.locals import *


pygame.init()
pygame.font.init()


class Game:
	def __init__(self):
		pygame.display.set_caption("Ping Pong Online")
		self.size = config.SCREEN_SIZE
		self.screen = pygame.display.set_mode(self.size)
		self.timer = pygame.time.Clock()
		self.is_running = True
		self.score = [0, 0]
		self.font = pygame.font.SysFont('Arial', 30)
		

		self.all_objects = pygame.sprite.Group()
		self.main_paddle = player.Player(3, config.SCREEN_SIZE[1]/2)
		self.second_paddle = player.AI_Player(config.SCREEN_SIZE[0] - 3 - config.PADDLE_SIZE[0], config.SCREEN_SIZE[1]/2)
		self.ball = ball.Ball(config.SCREEN_SIZE[0]/2, config.SCREEN_SIZE[1]/2)

		self.all_objects.add(self.main_paddle)
		self.all_objects.add(self.second_paddle)
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

	def check_win(self):
		if self.ball.rect.left < 0:
			self.score[1] += 1
			print(self.score)
			self.respawn()
		if self.ball.rect.right > self.screen.get_rect().right:
			self.score[0] += 1
			print(self.score)
			self.respawn()


	def respawn(self):
		self.main_paddle.respawn()
		self.second_paddle.respawn()
		self.ball.respawn()


	def scoreboard(self):
		self.score_text = self.font.render(f'{self.score[0]} : {self.score[1]}', False, (255, 255, 255))
		self.score_text_rect = self.score_text.get_rect()
		self.screen.blit(self.score_text, (self.size[0] / 2 - self.score_text_rect.width / 2, 10))


	def draw(self):
		self.screen.fill((0, 0, 0))
		self.main_paddle.update()
		self.ball.update([self.main_paddle, self.second_paddle])
		self.second_paddle.move(self.ball)
		self.check_win()
		self.scoreboard()
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

