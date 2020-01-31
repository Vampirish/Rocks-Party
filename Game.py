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
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        if self.credits:
                            Credits()
                        if self.exit:
                            running = False
                        if self.start:
                            StartGame()
                        if self.rules:
                            Rules()
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


class Rules(MainMenu):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rocks Party')
        self.size = width, height = 1100, 700
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))

        self.rules_working()

    def set_img(self):
        image = self.load_image("rules_menu.png")
        self.screen.blit(image, (0, 0))

    def rules_working(self):
        self.set_img()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        running = False
            pygame.display.flip()


class Credits:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rocks Party')
        self.screen = pygame.display.set_mode((1100, 700))
        self.screen_r = self.screen.get_rect()
        self.font = pygame.font.SysFont("Arial", 40)
        self.clock = pygame.time.Clock()
        self.speed = 60

        self.start()

    def start(self):
        credit_list = ["CREDITS", " ", " ", "Created by", "KEHES GAMES", " ", "Author", "Kenes Amina", " ",
                       "Programmer", "Kenes Amina", " ", "Art designer", "Kenes Amina", " ", " ", " ",
                       "SPECIAL THANKS", " ", "Eskendir Maratovich", "Khodzhaev Damir", "Denis Suharev",
                       "Kenes Aigerim", "Zhaksybekuly Bigazi", "Abdeldinova Asem",
                       "Kenes Balzhan", "Assylbek Akzhan", "Kenes Tileugazy"]

        texts = []
        for i, line in enumerate(credit_list):
            s = self.font.render(line, 1, (255, 255, 255))
            r = s.get_rect(centerx=self.screen_r.centerx, y=self.screen_r.bottom + i * 45)
            texts.append((r, s))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    if self.speed == 60:
                        self.speed = 300
                    else:
                        self.speed = 60

            self.screen.fill((0, 0, 0))

            for r, s in texts:
                r.move_ip(0, -1)
                self.screen.blit(s, r)

            if not self.screen_r.collidelistall([r for (r, _) in texts]):
                return

            pygame.display.flip()

            self.clock.tick(self.speed)


class StartGame(MainMenu):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rocks Party')
        self.size = width, height = 1100, 700
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))

        self.all_sprites = pygame.sprite.Group()

        self.Game()

    def Game(self):
        self.all_sprites = pygame.sprite.Group()
        Player1(self.all_sprites)
        Player2(self.all_sprites)
        Maps(self.all_sprites)

        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.all_sprites.draw(self.screen)
            self.all_sprites.update(event)

            pygame.display.flip()


class Player1(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.image = self.load_image("cub1.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pl_image = self.image
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 200
        self.map = Maps(group)

    def update(self, *args):
        if args:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_a]:
                self.image = pygame.transform.flip(self.pl_image, 1, 0)
                self.rect = self.rect.move(-10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(-10, 0)
                self.rect = self.rect.move(10, 10)
            if pressed[pygame.K_d]:
                self.image = self.pl_image
                self.rect = self.rect.move(10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(10, 0)
                self.rect = self.rect.move(-10, 10)
            if pressed[pygame.K_w]:
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(0, -20)
                while pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(0, 1)
        if not pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, 10)
        while pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, -1)


class Player2(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.image = self.load_image("cub2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pl_image = self.image
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 800
        self.rect.y = 200
        self.map = Maps(group)

    def update(self, *args):
        if args:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.image = pygame.transform.flip(self.pl_image, 1, 0)
                self.rect = self.rect.move(-10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(-10, 0)
                self.rect = self.rect.move(10, 10)
            if pressed[pygame.K_RIGHT]:
                self.image = self.pl_image
                self.rect = self.rect.move(10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(10, 0)
                self.rect = self.rect.move(-10, 10)
            if pressed[pygame.K_UP]:
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(0, -20)
                while pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(0, 1)
        if not pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, 10)
        while pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, -1)


class Maps(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.image = self.load_image("Map1.png", (255, 255, 255))
        self.image = pygame.transform.scale(self.image, (SCREEN_SIZE[0], SCREEN_SIZE[1]))
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


class Bullet(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.image = self.load_image("bullet.png")
        self.image = pygame.transform.scale(self.image, (12, 2))
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.image.from_surface(self.image)

    def update(self, *args):
        pass


if __name__ == '__main__':
    MainMenu()