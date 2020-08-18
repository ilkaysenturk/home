import pygame
import random

pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()

pygame.display.set_caption('Covid19 Spread')

red=(255,0,0)
green=(0,200,0)
amber=(255,255,0)
white = (255, 255, 255)

random_x=random.randint(0,400)
random_y=random.randint(0,300)

clock = pygame.time.Clock()
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           game_over=True
    print(event)
    random_x=10
    random_y=20
    print(random_x)
    print(random_y)
    dis.fill(white)
    pygame.draw.circle(dis,green,[random_x,random_y],1,1)
    pygame.display.update()
    pygame.draw.circle(dis,green,[random_x+5,random_y+5],1,1)
    pygame.display.update()
    clock.tick(3)

pygame.quit()
quit()
