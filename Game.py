import os
import pygame
import random


SCREEN_SIZE = [1100, 700]
check = None


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
                       "Lira Khairullina", "Kenes Balzhan", "Assylbek Akzhan", "Kenes Tileugazy"]

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

        self.counting = PointCount(self.screen)
        self.playerf_points = 0
        self.players_points = 0

        self.game()

    def game(self):
        self.all_sprites = pygame.sprite.Group()
        Maps(self.all_sprites)
        Player1(self.all_sprites)
        Player2(self.all_sprites)
        background = Backgroud()
        global check
        check = None

        self.pause = False
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(background.draw(), (0, 0))
            event = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = not self.pause
            if not self.pause:
                self.all_sprites.update(event)

            self.all_sprites.draw(self.screen)

            # PAUSE
            if self.pause:
                image = self.load_image("pause.png", (255, 255, 255))
                self.screen.blit(image, (0, 0))
            else:
                self.all_sprites.draw(self.screen)

            if check:
                if check == 2:
                    self.playerf_points += 1
                if check == 1:
                    self.players_points += 1
                running = False

            fplayer, splayer = self.counting.update(self.playerf_points, self.players_points)
            if fplayer == "win":
                Winner("first")
                return
            if splayer == "win":
                Winner("second")
                return

            pygame.display.flip()
        if check:
            self.start_again()

    def start_again(self):
        self.game()

    def checking(self):
        if check == 0:
            return None
        if check == 1:
            return "Player1"
        if check == 2:
            return "Player2"
        if check == 3:
            return "Draw"


class Winner(MainMenu):
    def __init__(self, player):
        pygame.init()
        self.size = width, height = 1100, 700
        pygame.display.set_caption('Rocks Party')
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))
        self.player = player

        self.winner_player()
        self.working()

    def winner_player(self):
        image2 = self.load_image("End.png")
        image2 = pygame.transform.scale(image2, (1100, 700))
        self.screen.blit(image2, (0, 0))

        if self.player == "first":
            image1 = self.load_image("win1.png", (255, 255, 255))
        elif self.player == "second":
            image1 = self.load_image("win2.png", (255, 255, 255))
        image1 = pygame.transform.scale(image1, (1000, 300))
        self.screen.blit(image1, (50, 80))

    def working(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        StartGame()
                        running = False
            pygame.display.flip()


class PointCount(MainMenu):
    def __init__(self, screen):
        self.screen = screen
        self.number = ["zero", "one", "two", "three", "four",
                       "five", "six", "seven", "eight", "nine"]

    def update(self, playerf_points, players_points):
        fplayer = splayer = None
        if playerf_points < 10:
            image1 = self.load_image(self.number[playerf_points] + ".png", (255, 255, 255))
            image1 = pygame.transform.scale(image1, (100, 100))
            self.screen.blit(image1, (50, 550))
        else:
            fplayer = "win"

        if players_points < 10:
            image2 = self.load_image(self.number[players_points] + ".png", (255, 255, 255))
            image2 = pygame.transform.scale(image2, (100, 100))
            self.screen.blit(image2, (950, 550))
        else:
            splayer = "win"
        return fplayer, splayer


class Player1(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.name = "Player1"
        self.image = self.load_image("cub1.png", (255, 255, 255))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pl_image = self.image
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 200
        self.group = group
        self.map = None
        for sprite in self.group:
            if sprite.name == "Maps":
                self.map = sprite
        self.view = "RIGHT"
        self.alive = True

    def update(self, *args):
        if args:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_a]:
                self.view = "LEFT"
                self.image = pygame.transform.flip(self.pl_image, 1, 0)
                self.rect = self.rect.move(-10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(-10, 0)
                self.rect = self.rect.move(10, 10)
            if pressed[pygame.K_d]:
                self.view = "RIGHT"
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
            if pressed[pygame.K_f]:
                Bullet(self.group, self.view, (self.rect.x, self.rect.y))
        if not pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, 10)
        while pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, -1)


class Player2(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.name = "Player2"
        self.image = self.load_image("cub2.png", (255, 255, 255))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.pl_image = self.image
        self.image = pygame.transform.flip(self.pl_image, 1, 0)
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 800
        self.rect.y = 200
        self.group = group
        self.map = None
        for sprite in self.group:
            if sprite.name == "Maps":
                self.map = sprite
        self.view = "LEFT"
        self.alive = True

    def update(self, *args):
        if args:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.view = "LEFT"
                self.image = pygame.transform.flip(self.pl_image, 1, 0)
                self.rect = self.rect.move(-10, -10)
                if not pygame.sprite.collide_mask(self, self.map):
                    self.rect = self.rect.move(-10, 0)
                self.rect = self.rect.move(10, 10)
            if pressed[pygame.K_RIGHT]:
                self.view = "RIGHT"
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
            if pressed[pygame.K_SEMICOLON]:
                Bullet(self.group, self.view, (self.rect.x, self.rect.y))
        if not pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, 10)
        while pygame.sprite.collide_mask(self, self.map):
            self.rect = self.rect.move(0, -1)


class Maps(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group):
        self.name = "Maps"
        num = random.choice([i for i in range(1, 7)])
        self.image = self.load_image("Map" + str(num) + ".png", (255, 255, 255))
        self.image = pygame.transform.scale(self.image, (SCREEN_SIZE[0], SCREEN_SIZE[1]))
        super().__init__(group)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0


class Backgroud(MainMenu):
    def __init__(self):
        self.number = random.choice([i for i in range(1, 6)])

    def draw(self):
        image = self.load_image("background" + str(self.number) + ".png")
        image = pygame.transform.scale(image, (1100, 700))
        return image


class Bullet(pygame.sprite.Sprite, MainMenu):
    def __init__(self, group, view, rect_coord):
        self.name = "Bullet"
        self.image = self.load_image("bullet.png")
        self.image = pygame.transform.scale(self.image, (12, 2))
        super().__init__(group)
        self.view = view
        self.map = None
        self.group = group
        for sprite in self.group:
            if sprite.name == "Maps":
                self.map = sprite

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = rect_coord
        self.rect.y += 34
        if self.view == "RIGHT":
            self.rect.x += 50
        if self.view == "LEFT":
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect.x -= 10
        self.mask = pygame.mask.from_surface(self.image)
        self.group = group

    def update(self, *args):
        if self.view == "RIGHT":
            self.rect = self.rect.move(50, 0)
        if self.view == "LEFT":
            self.rect = self.rect.move(-50, 0)
        if pygame.sprite.collide_mask(self, self.map):
            self.group.remove(self)
        player_sprite1 = player_sprite2 = None
        for sprite in self.group:
            if sprite.name == "Player1":
                player_sprite1 = sprite
            if sprite.name == "Player2":
                player_sprite2 = sprite
        pl1 = pl2 = True
        if player_sprite1 and pygame.sprite.collide_mask(self, player_sprite1):
            self.group.remove(self)
            self.group.remove(player_sprite1)
            pl1 = False
        if player_sprite2 and pygame.sprite.collide_mask(self, player_sprite2):
            self.group.remove(self)
            self.group.remove(player_sprite2)
            pl2 = False

        global check
        if not (pl1 and pl2):
            check = 3
        if not pl1:
            check = 1
        if not pl2:
            check = 2


if __name__ == '__main__':
    MainMenu()