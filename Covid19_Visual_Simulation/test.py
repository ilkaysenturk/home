import pygame
import random
import virus as vr

#Establish the screen
pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('Covid19 Spread')
white = (255, 255, 255)

#Screen refresh adjustment
clock = pygame.time.Clock()
game_over=False
count=0
list=[]
#Frame refresh within the loop
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           game_over=True
    dis.fill(white)
    #Create the number of initial people for the first frame as desired
    for p in range(20):  #number of people
        if count==0:   #if first frame playing
            random_x=random.randint(0,800) # put them somewhere randomly in x axis
            random_y=random.randint(0,600) # put them somewhere randomly in y axis
            #Flag the first one as corona infected
            if p==0:
                is_infected=1
            else:
                is_infected=0
            #Add these people to the list
            list.append([random_x+random.randint(-20,20),random_y+random.randint(-20,20),is_infected])
        else:
            random_x,random_y,is_infected=list[p]
            prev_random_x,prev_random_y,is_infected=list[p]#To keep last position before going out of the boundries

            random_inc_x=random.randint(-20,20)
            random_inc_y=random.randint(-20,20)

            for l in range(2):
                for m in range(len(list)):
                    for s in range(m+1, len(list)):
                        if abs(list[m][0]-list[s][0])<20:
                            if abs(list[m][1]-list[s][1])<20:
                                if list[m][2]==1:
                                    list[s]=list[s][0],list[s][1],1
                list.reverse()

            list[p]= (random_x+random_inc_x,random_y+random_inc_y,is_infected)



            if list[p][0]>800 or list[p][1]>600 or list[p][0]<0 or list[p][1]<0:#Screen boundries
                list[p]=prev_random_x,prev_random_y,is_infected

        if is_infected==1:
            color='red'
        else:
            color='green'
        person=vr.person(dis,color)
        person.wander_around(random_x,random_y)
        pygame.display.update()
    print(list)
    clock.tick(5)
    count+=1
pygame.quit()
quit()
