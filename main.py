

# program to demonstrate projectile motion of a horizontally launched body from a certain height

import pygame
from Flappy_Bird import *
from constants import *
import os
import sys
import time

os.environ['SDL_VIDEO_CENTERED'] = '1'



pygame.init()

gameDisplay = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Flappy Bird")


FPS = 60


# Custom Events
GAME_OVER = pygame.USEREVENT + 1 # GAME OVER

INITIAL_ANIMATION = True

FONT = pygame.font.SysFont("consolas", 30)




# Music Assets
BACKGROUND_MUSIC = pygame.mixer.Sound(fileLocation + "/Assets/sounds" + "/background_music.ogg")
BACKGROUND_MUSIC.set_volume(0.7)
GAME_OVER_MUSIC = pygame.mixer.Sound(fileLocation + "/Assets/sounds" + "/cheering.wav")
GAME_OVER_MUSIC.set_volume(1)
JUMP_MUSIC = pygame.mixer.Sound(fileLocation + "/Assets/sounds" + "/bullet_fire_sound.ogg")
JUMP_MUSIC.set_volume(1)

channel1 = pygame.mixer.Channel(0) # Background music channel
channel2 = pygame.mixer.Channel(1) # jump sound


def draw_display(bird, pipes):
    gameDisplay.fill(BLACK)
    gameDisplay.blit(BACKGROUND_IMG, (0, 0))
    bird.draw_bird()
    pygame.draw.line(gameDisplay, RED, (0, 0), (WIDTH, 0), width=10)
    pygame.draw.line(gameDisplay, RED, (0, HEIGHT), (WIDTH, HEIGHT), width=10)
    global PIPE_IMG_UP
    global PIPE_IMG_DOWN
    for pipe_pair in pipes:
        PIPE_IMG_UP = pygame.transform.scale(PIPE_IMG, (PIPE_WIDTH, pipe_pair.upper_pipe_length))
        PIPE_IMG_DOWN = pygame.transform.scale(PIPE_IMG, (PIPE_WIDTH, pipe_pair.lower_pipe_length))
        gameDisplay.blit(PIPE_IMG_UP, (pipe_pair.x, pipe_pair.upper_pipe_y))
        gameDisplay.blit(PIPE_IMG_DOWN, (pipe_pair.x, pipe_pair.lower_pipe_y))
        pygame.draw.line(gameDisplay, (156,105,57), (pipe_pair.x, pipe_pair.upper_pipe_length-6), (pipe_pair.x + PIPE_WIDTH, pipe_pair.upper_pipe_length-6), width=10) # To give a border to the pipe's upper end
        pygame.draw.line(gameDisplay, (156,105,57), (pipe_pair.x, pipe_pair.lower_pipe_y), (pipe_pair.x + PIPE_WIDTH, pipe_pair.lower_pipe_y), width=10) # To give a border to the pipe's lower end

    pygame.display.update()




def check_for_events(bird, pipes):
    # Creating Rects ----------------------------------
    bird_Rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
    for pipe_pair in pipes:
        upper_pipe_Rect = pygame.Rect(pipe_pair.x, pipe_pair.upper_pipe_y, PIPE_WIDTH, pipe_pair.upper_pipe_length)
        lower_pipe_Rect = pygame.Rect(pipe_pair.x, pipe_pair.lower_pipe_y, PIPE_WIDTH, pipe_pair.lower_pipe_length)
    # Creating Rects ----------------------------------

    if bird_Rect.colliderect(upper_pipe_Rect) or bird_Rect.colliderect(lower_pipe_Rect): # collided with pipes
        pygame.event.post(pygame.event.Event(GAME_OVER))
    if (bird.y < BOUNDARIES_WIDTH) or (bird.y + BIRD_HEIGHT > HEIGHT- BOUNDARIES_WIDTH): # Crossed boundaries
        pygame.event.post(pygame.event.Event(GAME_OVER))


def draw_end(winner_text):
    gameDisplay.fill(BLACK)
    gameDisplay.blit(BACKGROUND_IMG, (0, 0))
    blit_text(gameDisplay, winner_text, (20, 20), FONT, BLACK)
    pygame.display.update()
    pygame.time.delay(1000*3) # 3 seconds

def ask_restart():
    end_text = "\n\n\n\n\n\n\n\n\nRestart The Game Press SpaceBar\nEnter Any Other Key To Quit.\n"
    while True:
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BACKGROUND_IMG, (0, 0))
        blit_text(gameDisplay, end_text, (20, 20), FONT, BLACK)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                else:
                    pygame.quit()
                    sys.exit(0)



def main():
    channel1.play(BACKGROUND_MUSIC, -1)
    clock = pygame.time.Clock()
    running = True
    start = True

    bird = Bird(INITIAL_POS)
    pipes = [] # list of all the pipes that are on the screen
    global SCORE
    SCORE = 0
    global HIGH_SCORE

    with open(fileLocation + "/.HighScore.txt", "a+") as file1: # To create HighScore.txt file if it didn't exist
        print(file1.read())
    with open(fileLocation + "/.HighScore.txt", "r") as file1:
        if file1.read() == "":
            HIGH_SCORE = 0
        else:
            with open(fileLocation + "/.HighScore.txt", "r") as file2:
                HIGH_SCORE = int(file2.read())


    while start:
        text =  "\n\n\n    Welcome To Flappy Bird\n\n"\
                "Rules: \n1.Don't Touch Pipes\n2.Don't Touch The Red Lines\n3.Press 'Spacebar' to Jump\n\n"\
                "'SpaceBar'-> Start The Game"
        
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BACKGROUND_IMG, (0, 0))
        bird.draw_bird()
        blit_text(gameDisplay, text, (20, 20), FONT, BLACK)
        pygame.draw.line(gameDisplay, RED, (0, 0), (WIDTH, 0), width=10)
        pygame.draw.line(gameDisplay, RED, (0, HEIGHT), (WIDTH, HEIGHT), width=10)
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = False
        pygame.display.update()
    
    initial_time = time.time()
    
    while INITIAL_ANIMATION:
        clock.tick(FPS)
        jump = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                    jump = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True
            if event.type == GAME_OVER: 
                channel1.play(GAME_OVER_MUSIC)
                if SCORE > HIGH_SCORE:
                    text = "Congratulations! You beat the High Score, Your Score is " + str(SCORE)
                    print(text)
                    text = "\n\n\n\n\n\n\n\n\nCongratulations! You beat the High Score, Your Score is " + str(SCORE)
                    with open(fileLocation + "/.HighScore.txt", "w") as file1:
                        file1.write(str(SCORE))
                else:
                    text = "Your Score: " + str(SCORE) + ", High Score: " + str(HIGH_SCORE)
                    print(text)
                    text = "\n\n\n\n\n\n\n\n\nYour Score: " + str(SCORE) + ", High Score: " + str(HIGH_SCORE)
                running = False
                draw_end(text)
                ask_restart()



        bird.bird_jump(jump) # bird's movement
        gameDisplay.fill(BLACK)
        gameDisplay.blit(BACKGROUND_IMG, (0, 0))
        bird.draw_bird()
        pygame.draw.line(gameDisplay, RED, (0, 0), (WIDTH, 0), width=10)
        pygame.draw.line(gameDisplay, RED, (0, HEIGHT), (WIDTH, HEIGHT), width=10)
        if (bird.y < BOUNDARIES_WIDTH) or (bird.y + BIRD_HEIGHT > HEIGHT- BOUNDARIES_WIDTH): # Crossed boundaries
            pygame.event.post(pygame.event.Event(GAME_OVER))
        pygame.display.update() 
        if (time.time() - initial_time) > INITIAL_ANIMATION_TIME:
            break
            


    while running:
        clock.tick(FPS)
        jump = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                    jump = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump = True
            if event.type == GAME_OVER: 
                channel1.play(GAME_OVER_MUSIC)
                if SCORE > HIGH_SCORE:
                    text = "Congratulations! You beat the High Score, Your Score is " + str(SCORE)
                    print(text)
                    text = "\n\n\n\n\n\n\n\n\nCongratulations! You beat the High Score, Your Score is " + str(SCORE)
                    with open(fileLocation + "/.HighScore.txt", "w") as file1:
                        file1.write(str(SCORE))
                else:
                    text = "Your Score: " + str(SCORE) + ", High Score: " + str(HIGH_SCORE)
                    print(text)
                    text = "\n\n\n\n\n\n\n\n\nYour Score: " + str(SCORE) + ", High Score: " + str(HIGH_SCORE)
                running = False
                draw_end(text)
                ask_restart()


        
        # Creation Of Pipes ####################################################
        if len(pipes) == 0: # at the start of the game
            pipe = Pipes()
            pipes.append(pipe) # the first pipe
        else:
            if (pipes[-1]).x + PIPE_WIDTH <= HORIZONTAL_GAP_BETWEEN_PIPE_PAIRS: # this implies old pipe has been crossed => SCORE is added
                pipe = Pipes()
                pipes.append(pipe)
                SCORE += 10
        # Creation Of Pipes ####################################################
        Pipes.pipe_movement(pipes)
        Pipes.pipe_destroy(pipes)
        bird.bird_jump(jump) # bird's movement
        draw_display(bird, pipes)
        check_for_events(bird, pipes)
    pygame.quit()


if __name__=='__main__':
    main()