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
    c_num_pos=[[575,50],[725,200],[760,375],[725,550],[600,700],[400,750],[200,700],[50,550],[10,375],[50,200],[170,68],[350,0]]
    count+=1
    number='' #This will increment the clock numbers Eg. 1,2,3
    dis.fill(white) # Will fill the screen with white
    for i in range (12): # Start the loop for creating the clock's numbers
        xy=c_num_pos[i]
        number=i+1
        dis.blit(create_clock_number(str(number),False,black),(xy))
    #xy=c_num_pos[count]
    #pygame.draw.line(dis,black,(400,400),(xy))
    pygame.draw.circle(dis,black,(400,400),300,2)
    pygame.display.update()
    clock.tick(1)
pygame.quit()
quit
