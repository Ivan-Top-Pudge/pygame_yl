import os
import sys
import pygame
import pytmx


def load_image(name, colorkey=None):
    fullname = os.path.join('src', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["World Of Tanks", "(EARLY BETA 0.1)",
                  "Правила игры",
                  "Вы играете за экипаж лт,",
                  "Вы пробрались в тыл врага",
                  "Ваша цель: уничтожить артилерию врага"]

    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('sprites/fon.jpg'), (40 * 32, 35 * 32))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def end_screen():
    intro_text = ["World Of Tanks", "(EARLY BETA 0.1)",
                  "Поздравляем!",
                  "Уровень пройден",
                  "",
                  "(Нажмите любую клавишу чтобы вернуться в меню)"]

    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('sprites/fon.jpg'), (40 * 32, 35 * 32))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def final_screen():
    intro_text = ["World Of Tanks", "(EARLY BETA 0.1)",
                  "Поздравляем!",
                  "Игра пройдена!",
                  "Надеюсь она вам понравилась",
                  "(Нажмите любую клавишу чтобы выйти)"]

    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('sprites/fon.jpg'), (40 * 32, 35 * 32))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(60)


def game_over_screen():
    intro_text = ["World Of Tanks", "(EARLY BETA 0.1)",
                  "Поражение!",
                  "Вы были уничтожены!",
                  "",
                  "(Нажмите любую клавишу чтобы выйти)",
                  "(Перезапустите игру, чтобы начать сначала)"]

    _clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('sprites/fon.jpg'), (40 * 32, 35 * 32))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for _event in pygame.event.get():
            if _event.type == pygame.QUIT:
                terminate()
            elif _event.type == pygame.KEYDOWN or \
                    _event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        _clock.tick(60)


class Map:
    def __init__(self, map_name):
        self.map = pytmx.load_pygame(map_name)
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def generate_groups(self):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if self.get_tile_id((x, y)) not in (30, 31, 32, 38, 39, 47):
                    Tile(image, x, y, 'wall')
                else:
                    Tile(image, x, y, 'def')


def info_dead():
    intro_text = ["World Of Tanks", "(EARLY BETA 0.1)",
                  "Вас уничтожили",
                  "",
                  "",
                  "(Нажмите любую клавишу)"]
    font = pygame.font.Font(None, 50)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 100
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, tile_type):
        if tile_type == 'wall':
            super().__init__(walls, all_sprites)
        else:
            super().__init__(others, all_sprites)
        self.image = image
        self.rect = self.image.get_rect().move(
            pos_x * 32, pos_y * 32)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.images = (pygame.transform.rotate(player_image, 90),
                       pygame.transform.rotate(player_image, 180),
                       pygame.transform.rotate(player_image, 270),
                       pygame.transform.rotate(player_image, 360))
        self.pos = 0
        self.image = self.images[self.pos]
        self.vx, self.vy = 0, 0
        self.rect = self.image.get_rect().move(
            32 * pos_x + 15, 32 * pos_y + 5)

    def move(self, act):
        if act.key == pygame.K_LEFT:
            self.vx = -3
            self.pos = 0
        elif act.key == pygame.K_RIGHT:
            self.vx = 3
            self.pos = 2
        elif act.key == pygame.K_UP:
            self.vy = -3
            self.pos = 3
        elif act.key == pygame.K_DOWN:
            self.vy = 3
            self.pos = 1
        self.image = self.images[self.pos]

    def stop(self):
        self.vx, self.vy = 0, 0

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if pygame.sprite.spritecollideany(self, walls):
            self.rect.x = self.rect.x + -self.vx
            self.rect.y += -self.vy

    def shoot(self):
        Bullet(self.rect.x, self.rect.y, self.pos)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction):
        super().__init__(bullets, all_sprites)
        self.image = bullet_images[direction]
        self.speedx, self.speedy = 0, 0
        x, y = 0, 0
        if direction == 0:
            x, y = pos_x - 30, pos_y + 30
            self.speedx -= 10
        elif direction == 1:
            x, y = pos_x + 35, pos_y + 70
            self.speedy += 10
        elif direction == 2:
            x, y = pos_x + 70, pos_y + 30
            self.speedx += 10
        elif direction == 3:
            x, y = pos_x + 33, pos_y - 30
            self.speedy -= 10
        self.rect = self.image.get_rect().move(x, y)
        ShootBoom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x, self.rect.y - 30)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0 or self.rect.x > 40 * 32 or self.rect.y < 0 or self.rect.y > 35 * 32:
            self.kill()
        if pygame.sprite.spritecollideany(self, walls):
            LittleBoom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x, self.rect.y)
            self.kill()
        if pygame.sprite.spritecollide(self, artillery, True):
            Boom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x, self.rect.y)
            self.kill()
        if pygame.sprite.spritecollide(self, bombs, True):
            Boom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x - 30, self.rect.y)
            self.kill()


class Arta(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(artillery, all_sprites)
        self.image = pygame.transform.rotate(art_image, 90)
        self.rect = self.image.get_rect().move(
            32 * pos_x + 15, 32 * pos_y + 5)
        self.aim = 50

    def update(self):
        self.aim -= 1
        if self.aim == 0 and player_group:
            Bomb(player.rect.x, player.rect.y)
            self.aim = 80


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos_x, target_y):
        super().__init__(all_sprites, bombs)
        self.image = bomb_image
        self.target_y = target_y
        self.rect = self.image.get_rect().move(
            pos_x, -50)

    def update(self):
        if self.target_y - 20 < self.rect.y < self.target_y + 20:
            self.kill()
            Boom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x, self.rect.y)
        self.rect.y += 10
        if pygame.sprite.spritecollide(self, player_group, True):
            Boom(load_image("sprites/boom.png", -1), 3, 1, self.rect.x, self.rect.y)
            self.kill()


class Boom(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.frame = 0
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.frame += 1
        if not self.frame % 10:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        if self.frame == 30:
            self.kill()


class LittleBoom(Boom):
    def update(self):
        self.frame += 1
        if not self.frame % 3:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        if self.frame == 6:
            self.kill()


class ShootBoom(Boom):
    def update(self):
        self.frame += 1
        if not self.frame % 2:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        if self.frame == 4:
            self.kill()


def generate_level(map_obj: Map, arta_cords: list):
    for sprite in all_sprites:
        sprite.kill()
    for cords in arta_cords:
        Arta(cords[0], cords[1])
    map_obj.generate_groups()
    return Player(5, 15)


if __name__ == '__main__':
    name = 'admin'
    pygame.init()
    pygame.display.set_caption("Ануфриев copyright all rights reserved")
    size = width, height = 40 * 32, 35 * 32
    screen = pygame.display.set_mode(size)

    start_screen()

    running = True
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    others = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    artillery = pygame.sprite.Group()
    player_image = load_image('sprites/tank_test.png', -1)
    bullet_image = load_image("sprites/bullet.png", -1)
    art_image = load_image("sprites/arta.png", -1)
    bomb_image = load_image('sprites/bomb.png', -1)
    bullet_images = (pygame.transform.rotate(bullet_image, 90),
                     pygame.transform.rotate(bullet_image, 180),
                     pygame.transform.rotate(bullet_image, 270),
                     pygame.transform.rotate(bullet_image, 360))
    levels = ((Map("src/maps/level1.tmx"), [[30, 15]]), (Map("src/maps/level2.tmx"), [[30, 15], [30, 25]]))
    points = (50, 500)
    cur_level = 0
    player = generate_level(*levels[cur_level])
    score = 0
    time = 0
    succes = False
    while running:
        screen.fill('black')
        if not artillery:
            score += points[cur_level]
            cur_level += 1
            if cur_level == 2:
                succes = True
                final_screen()
                break
            end_screen()
            player = generate_level(*levels[cur_level])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player_group:
                    player.shoot()
            elif event.type == pygame.KEYDOWN:
                if not player_group:
                    game_over_screen()
                    running = False
                player.move(event)
            elif event.type == pygame.KEYUP:
                player.stop()
        all_sprites.draw(screen)
        artillery.draw(screen)
        player_group.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    if succes:
        with open('results.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        with open('results.txt', 'w', encoding='utf-8') as file:
            file.write(data)
            file.write(f"\n{name} прошёл игру")
    else:
        with open('results.txt', 'r', encoding='utf-8') as file:
            data = file.read()
        with open('results.txt', 'w', encoding='utf-8') as file:
            file.write(data)
            file.write(f"\n{name} не прошёл игру, погиб на {cur_level + 1} уровне")
