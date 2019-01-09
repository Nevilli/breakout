import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    # Constants that will be used in the program

    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # colors used
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GOLD = (255, 209, 63)

    colors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]
    whites = [WHITE]

    # Breakout window
    pygame.init()
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Trumpy")


    background_image = pygame.image.load("Background.pn")
    background_rect = background_image.get_rect()
    background_rect.x = 0
    background_rect.y = 0
    mainSurface.blit(background_image, background_rect)


    x = 0
    y = BRICK_Y_OFFSET

    # This creates the paddle and places it on the screen
    q = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    r = (APPLICATION_WIDTH/2)
    chad = paddle.Paddle(mainSurface, whites[0], PADDLE_WIDTH, PADDLE_HEIGHT)
    chad.rect.x = r
    chad.rect.y = q
    mainSurface.blit(chad.image, chad.rect)
    pygame.display.update()
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    paddle_group.add(chad)
    # This creates the ball
    balls = ball.Ball(GOLD, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    balls.rect.x = 205
    balls.rect.y = 300
    mainSurface.blit(balls.image, balls.rect)

    # This loop creates the brick rows
    for m in range(BRICKS_PER_ROW):
        x = 0
        color = colors[m]
        for b in range(BRICKS_PER_ROW):
            bricks = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            brick_group.add(bricks)
            bricks.rect.x = x
            bricks.rect.y = y
            mainSurface.blit(bricks.image, bricks.rect)
            # This spaces out the bricks in each row
            x = x + BRICK_WIDTH + BRICK_SEP
            pygame.display.update()
        # This spaces out the rows of bricks
        y = y + BRICK_HEIGHT + BRICK_SEP

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(BLACK)
        mainSurface.blit(balls.image, balls.rect)
        for bricks in brick_group:
            mainSurface.blit(bricks.image, bricks.rect)
        chad.move()
        balls.move()
        mainSurface.blit(balls.image, balls.rect)
        mainSurface.blit(chad.image, chad.rect)
        pygame.display.update()
        # This allows the ball to remove the bricks that it hits on screen
        balls.collide(paddle_group, brick_group)
        # These if statements set the number of turns for the game and will end it if the limit is reached
        if balls.rect.bottom >= APPLICATION_HEIGHT:
            balls.rect.x = 205
            balls.rect.y = 300
            NUM_TURNS -= 1
            if NUM_TURNS == 0:
                pygame.quit()
                sys.exit()
        if len(brick_group) == 0:
            pygame.quit()
            sys.exit()


main()
