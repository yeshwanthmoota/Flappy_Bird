

from constants import *
from main import JUMP_MUSIC, gameDisplay, channel2
import random

class Bird:
    def __init__(self, pos):
        self.x = pos[0] # x position
        self.y = pos[1] # y position
        self.vel_y = -10 # initial y velocity
    def bird_jump(self, jump): # changes the x and y positions of the ball according to gravity
        if jump:
            self.vel_y = INITIAL_Y_VEL
            channel2.play(JUMP_MUSIC)
        self.y += self.vel_y
        self.vel_y += GRAVITY
    def draw_bird(self):
        gameDisplay.blit(FLAPPY_BIRD, (self.x, self.y))

class Pipes: # one pipe object applies to a pair of pipes
    def __init__(self): # a Random pipe should be generated
        random_length = (random.random())*((7/8)*(HEIGHT/1.5)) + (HEIGHT/8) # some random length is generated
        # Let's say the minimum value of upper_pipe_length = 100px => HEIGHT/8
        # => x + (0-1)y = HEIGHT/1.5 & x + y(1) = HEIGHT/1.5 && x + y(0) = HEIGHT/8 => x = HEIGHT/8 and y = (7/8) * HEIGHT
        # now a pipe of random length but a fixed gap can be generated since we have the random length
        print(random_length)
        self.upper_pipe_length = random_length
        self.lower_pipe_length = HEIGHT - VERTICAL_GAP_BETWEEN_PIPES - random_length
        self.x = WIDTH
        self.upper_pipe_y = 0
        self.lower_pipe_y = HEIGHT - self.lower_pipe_length

    @staticmethod
    def pipe_movement(pipes):
        for pipe_pair in pipes:
            pipe_pair.x -= PIPE_SPEED


    @staticmethod
    def pipe_destroy(pipes):
        for pipe_pair in pipes:
            if pipe_pair.x <= 0 - PIPE_WIDTH:
                pipes.remove(pipe_pair)
        return pipes




def blit_text(gameDisplay, text, pos, font, color=pygame.Color('black')): # function borrowed from stack overflow 😅
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = gameDisplay.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            gameDisplay.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.