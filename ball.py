import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        radius = 10

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((windowWidth, windowHeight))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, color, self.rect, radius)

    def move(self):
        pass
