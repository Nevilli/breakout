import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.radius = radius
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.speedx = 5
        self.speedy = 5

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill ((0, 0, 0))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        pygame.display.update()

    def move(self):
        self.rect.top += self.speedy
        self.rect.left += self.speedx

        if self.rect.top < 0:
            self.speedy = -self.speedy
        elif self.rect.bottom > self.windowHeight:
            self.rect.x = 200
            self.rect.y = 200
        elif self.rect.left < 0 or self.rect.right > self.windowWidth:
            self.speedx = -self.speedx

    def collide(self, paddle_group, brick_group):
        if pygame.sprite.spritecollide(self, brick_group, True):
            self.speedy = -self.speedy
        if pygame.sprite.spritecollide(self, paddle_group, False):
            self.speedy = -self.speedy

