import os
import sys
import pygame
import pytmx

# todo: 2.Сделать взрывы снарядов


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


class Map:
    def __init__(self):
        self.map = pytmx.load_pygame("map2.tmx")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def generate_groups(self):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                if self.get_tile_id((x, y)) not in (30, 31, 38, 39, 47):
                    Tile(image, x, y, 'wall')
                else:
                    Tile(image, x, y, 'def')


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

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0 or self.rect.x > 40 * 32 or self.rect.y < 0 or self.rect.y > 35 * 32:
            self.kill()
        if pygame.sprite.spritecollideany(self, walls):
            self.kill()
        if pygame.sprite.spritecollide(self, artillery, True):
            self.kill()


class Arta(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(artillery, all_sprites)
        self.image = pygame.transform.rotate(art_image, 90)
        self.rect = self.image.get_rect().move(
            32 * pos_x + 15, 32 * pos_y + 5)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Ануфриев copyright all rights reserved")
    size = width, height = 40 * 32, 35 * 32
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    karta = Map()
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    others = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    artillery = pygame.sprite.Group()
    player_image = load_image('sprites/tank_test.png', -1)
    bullet_image = load_image("sprites/bullet.png", -1)
    art_image = load_image("sprites/arta.png", -1)
    bullet_images = (pygame.transform.rotate(bullet_image, 90),
                     pygame.transform.rotate(bullet_image, 180),
                     pygame.transform.rotate(bullet_image, 270),
                     pygame.transform.rotate(bullet_image, 360))
    player = Player(5, 10)
    Arta(30, 1)
    karta.generate_groups()
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player.shoot()
            elif event.type == pygame.KEYDOWN:
                player.move(event)
            elif event.type == pygame.KEYUP:
                player.stop()
        all_sprites.draw(screen)
        artillery.draw(screen)
        player_group.draw(screen)
        artillery.update()
        all_sprites.update()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
