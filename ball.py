import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        super().__init__()

        # class variables
        self.color = color
        self.radius = radius
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.speedx = 5
        self.speedy = 5

        # size and shape of the ball and puts it on screen
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill ((0, 0, 0))
        self.rect = self.image.get_rect()

        # makes the ball a circle
        pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)
        pygame.display.update()

    def move(self):
        """
        This function allows the ball to move and bounce off of the walls and bricks
        :return: none
        """
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
        """
        This function lets the ball collide with bricks on screen and remove them and with the paddle
        :param paddle_group: ball bounces off of paddle
        :param brick_group: balls hits bricks and removes them from screen
        :return: none
        """
        if pygame.sprite.spritecollide(self, brick_group, True):
            self.speedy = -self.speedy
        if pygame.sprite.spritecollide(self, paddle_group, False):
            self.speedy = -self.speedy

