import pygame
import time

#Establish the screen
pygame.init()
black=(0,0,0)
white=(255,255,255)
x=800
y=800
dis=pygame.display.set_mode((x,y))
pygame.display.set_caption('Crayz Clock')
clock = pygame.time.Clock()

#Create font object
font=pygame.font.Font('freesansbold.ttf',45)

#Create function for creaing the text
def create_clock_number(number,false,color):
    text=font.render(number,false,color)
    return text

count=0
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           game_over=True
    print(event)
    c_num_pos=[[600,54],[746,200],[775,380],[746,575],[600,746],[400,765],[200,746],[50,550],[10,375],[50,200],[170,68],[380,0]]
    hand_pos=[[400,0],[600,54],[746,200],[800,400],[746,600],[600,746],[400,800],[200,746],[54,600],[0,400],[54,200],[200,54]]
    count+=1
    number='' #This will increment the clock numbers Eg. 1,2,3
    hand_x,hand_y=hand_pos[count]
    dis.fill(white) # Will fill the screen with white
    for i in range (12): # Start the loop for creating the clock's numbers
        num_xy=c_num_pos[i]
        number=i+1
        dis.blit(create_clock_number(str(number),False,black),(num_xy))
        #pygame.draw.circle(dis,black,(400,400),300,2)
    pygame.draw.line(dis,black,(400,400),(hand_x,hand_y))
    pygame.display.update()
    time.sleep(5)
    clock.tick(1)

pygame.quit()
quit
