import pygame
import os

fileLocation = os.path.dirname(os.path.abspath(__file__))

GRAY = (180,180,180)
BLACK = (0,0,0)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN= (0,255,0)


WIDTH = 600
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
BIRD_WIDTH = HEIGHT/20 # 50
BIRD_HEIGHT = HEIGHT/20 # 50
INITIAL_POS = (WIDTH/2-BIRD_WIDTH - 20, HEIGHT*0.5 - BIRD_HEIGHT/2)
GRAVITY = 0.5 # px/frame^2
INITIAL_Y_VEL = -10
VERTICAL_GAP_BETWEEN_PIPES = HEIGHT/5 # 160
HORIZONTAL_GAP_BETWEEN_PIPE_PAIRS = WIDTH/2.3 # 260
PIPE_SPEED = 5
PIPE_WIDTH = WIDTH/6.67 # 90
BOUNDARIES_WIDTH = 10
INITIAL_ANIMATION_TIME = 2.0

# Visual Assets
FLAPPY_BIRD = pygame.image.load(fileLocation + "/Assets/images" + "/flappy_bird.png")
FLAPPY_BIRD = pygame.transform.scale(FLAPPY_BIRD, (BIRD_WIDTH, BIRD_HEIGHT))
BACKGROUND_IMG = pygame.image.load(fileLocation + "/Assets/images" + "/background_image.png")
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (WIDTH, HEIGHT))
PIPE_IMG = pygame.image.load(fileLocation + "/Assets/images" + "/pipe_img_2.png")
