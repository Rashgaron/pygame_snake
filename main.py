import pygame
from pygame.locals import *
import time

SIZE = 40

class Snake:
    def __init__(self, surface, length ):
        self.parent_screen = surface
        self.length = length  
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE] * length 
        self.y = [SIZE] * length 
        self.direction = 'down'
    
    def draw(self):
        self.parent_screen.fill((110, 110, 255))

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.update()
    
    def move_up(self):
        self.direction = 'up'

    # create function to move snake down
    def move_down(self):
        self.direction = 'down'

    # create function to move snake left
    def move_left(self):
        self.direction = 'left'

    # create function to move snake right
    def move_right(self):
        self.direction = 'right'

    # create function to make snake walk
    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1] 
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE  
        if self.direction == 'down':
            self.y[0] += SIZE  
        if self.direction == 'left':
            self.x[0] -= SIZE  
        if self.direction == 'right':
            self.x[0] += SIZE 
        
        self.draw()


class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.apple= pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3 
        self.y = SIZE * 3 
    
    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        surface = pygame.display.set_mode((1000, 1000))
        surface.fill((110, 110, 255))
        self.snake = Snake(surface, 2);
        self.snake.draw()
        self.apple = Apple(surface)
        self.apple.draw()

    def check_collision(self):
        if self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y:
            self.apple.x = SIZE * 3 
            self.apple.y = SIZE * 3 
            self.snake.length += 1

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.check_collision()


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                        pass
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        pass
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        pass
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        pass

                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            self.play()

            time.sleep(.2)


if __name__ == "__main__":

    game = Game()
    game.run()


