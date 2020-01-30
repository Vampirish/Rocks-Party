import os
import pygame
import random


SCREEN_SIZE = [1100, 700]


class MainMenu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rocks Party')
        self.size = width, height = 1100, 700
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))

        self.start = 0
        self.exit = 0
        self.rules = 0
        self.credits = 0

        self.menu_working()

    def menu_working(self):
        self.set_img()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()

    def set_img(self):
        image = self.load_image("rock.png", (255, 255, 255))
        image = pygame.transform.scale(image, (1100, 700))
        self.screen.blit(image, (0, 0))

        image1 = self.load_image("start" + str(self.start) + ".png", (255, 255, 255))
        image1 = pygame.transform.scale(image1, (300, 100))
        self.screen.blit(image1, (50, 100))

        image1 = self.load_image("exit" + str(self.exit) + ".png", (255, 255, 255))
        image1 = pygame.transform.scale(image1, (300, 100))
        self.screen.blit(image1, (750, 500))

        image1 = self.load_image("rules" + str(self.rules) + ".png", (255, 255, 255))
        image1 = pygame.transform.scale(image1, (300, 100))
        self.screen.blit(image1, (50, 500))

        image1 = self.load_image("credits" + str(self.credits) + ".png", (255, 255, 255))
        image1 = pygame.transform.scale(image1, (300, 100))
        self.screen.blit(image1, (750, 100))

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname).convert()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


if __name__ == '__main__':
    MainMenu()