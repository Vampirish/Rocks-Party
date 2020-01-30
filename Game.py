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

        self.start = 1
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
                if event.type == pygame.KEYDOWN:
                    if self.start:
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            self.start = 0
                            self.credits = 1
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            self.start = 0
                            self.rules = 1
                    if self.credits:
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            self.start = 1
                            self.credits = 0
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            self.credits = 0
                            self.exit = 1
                    if self.rules:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            self.start = 1
                            self.rules = 0
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            self.rules = 0
                            self.exit = 1
                    if self.exit:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            self.credits = 1
                            self.exit = 0
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            self.rules = 1
                            self.exit = 0

                    self.set_img()

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