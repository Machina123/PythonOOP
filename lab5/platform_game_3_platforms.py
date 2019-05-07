import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'          # centrowanie okna
pygame.init()

## ustawienia ekranu i gry
screen = pygame.display.set_mode(gm.SIZESCREEN)
pygame.display.set_caption('Prosta gra platformowa...')
clock = pygame.time.Clock()

PLAYER_ACCEL = 6

# klasa gracza
class Player(pygame.sprite.Sprite):
    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self.count = 0
        self.lifes = 3
        self.level = None
        self.direction_of_movement = 'right'

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def turn_right(self):
        self.movement_x = PLAYER_ACCEL
        self.direction_of_movement = 'right'

    def turn_left(self):
        self.movement_x = -1 * PLAYER_ACCEL
        self.direction_of_movement = 'left'

    def stop(self):
        if self.movement_x > 0:
            self.image = gm.STAND_R
        elif self.movement_x < 0:
            self.image = gm.STAND_L
        self.movement_x = 0

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        else:
            self.image = image_list[1]

        self.count += 1
        if self.count > 8:
            self.count = 0

    def update(self):
        self.rect.x += self.movement_x
        if self.movement_x > 0:
            self._move(gm.IMAGES_R)
        elif self.movement_x < 0:
            self._move(gm.IMAGES_L)

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.turn_left()
            elif event.key == pygame.K_RIGHT:
                self.turn_right()
        elif event.type == pygame.KEYUP:
            self.stop()

class Platform(pygame.Surface):

    def __init__(self, colour, width, height, rect_x, rect_y):
        self.width = width
        self.height = height
        self.rect = pygame.Surface([width, height])
        self.rect_rect = self.rect.get_rect()
        self.rect_rect.x = rect_x
        self.rect_rect.y = rect_y
        self.rect.fill(colour)

    def draw(self, surface):
        surface.blit(self.rect, self.rect_rect)

    def update(self):
        pass

class Level():

    def __init__(self, player:Player):
        self.player = player
        self.set_of_platforms = set()

    def update(self):
        for platform in self.set_of_platforms:
            platform.update()

    def draw(self, surface):
        for platform in self.set_of_platforms:
            platform.draw(surface)

class Level_1(Level):
    def __init__(self, player:Player):
        super().__init__(player)
        self.set_of_platforms.add(Platform(gm.DARKRED, 350, 70, 0, 280))
        self.set_of_platforms.add(Platform(gm.DARKRED, 420, 70, 280, 490))
        self.set_of_platforms.add(Platform(gm.DARKRED, 280, 70, 700, 200))


# konkretyzacja obiektów
player = Player(gm.STAND_R)
player.rect.center = screen.get_rect().center
level = Level_1(player)
# głowna pętla gry
window_open = True
while window_open:
    screen.fill(gm.LIGHTBLUE)
    player.update()
    level.update()
    # pętla zdarzeń
    for event in pygame.event.get():
        player.get_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif event.type == pygame.QUIT:
            window_open = False

    # rysowanie i aktualizacja obiektów
    player.draw(screen)
    level.draw(screen)

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()