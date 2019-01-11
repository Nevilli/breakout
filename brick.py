import pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.image.load("100.png")
        # self.image = pygame.Surface((self.width, self.height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()
        # self.image.fill(self.color)

        # Fill the surface with the correct color
