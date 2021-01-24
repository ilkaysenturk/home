import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen_width=800
screen_height=500


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((40,20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
           self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

        #Define the Enemey objects by extending pygame.sprite.Sprite
        #and define the surface and other attributes for the enemy objects
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()




pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode([screen_width, screen_height])

player = Player()

#Create the sprite groups
enemies=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
all_sprites.add(player)

#Create a custom event called 'ADDENEMY' for adding enemies
ADDENEMY=pygame.USEREVENT+1
pygame.time.set_timer(ADDENEMY,500)

#Game Loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running=False
        elif event.type==pygame.QUIT:
            running=False
        elif event.type==ADDENEMY:
            #Create the new enemy and add it to sprite groups
            new_enemy=Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    enemies.update()

    screen.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    #screen.blit(player.surf,player.rect)

    pygame.display.flip()

    clock.tick(30)
