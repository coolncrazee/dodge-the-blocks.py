import pygame
import random
import sys


pygame.init()

WIDTH=800
HEIGHT=600		
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
BACKGROUND_COLOR=(128,128,128)
player_size=50

player_pos=[WIDTH/2,HEIGHT-2*player_size]
enemy_size=50
enemy_pos=[random.randint(0, WIDTH-enemy_size),0]
enemy_list=[enemy_pos]
SPEED=10
score=0
enemy_num=10		
checkpoint_score=50

screen= pygame.display.set_mode((WIDTH,HEIGHT))
	

game_over=False
clock = pygame.time.Clock()

myFont= pygame.font.SysFont("monospace",35)

#idea for seperating enemies with a minimum distance = the size of the player
#as bonus levels between levels every time score reaches a 100
#idea to go TO SCHOOL WITH THIS AND CUSTOMISE IT SO THAT IT ASKS THE NAME OF THE PLAYER AND DOESNT ACCEPT THE NAME AGAIN
#TO MAKE SURE SAME PERSON DOESNT PLAY AGAIN
#GO TO SCHOOL AS A WAY TO BUILD AWARENESS AROUND THE FIELD Of coding and encourage this among youth

def set_level1(score,SPEED):
	# if score <20:
	# 	SPEED=10
	# elif score<40:
	# 	SPEED=15
	# elif score <60:wwwwwwwwww     
	# 	SPEED=20
	# else:
	# 	SPEED=25
	SPEED=score/10+10

	#SPEED=50
	return SPEED

def set_level2(score,enemy_num):
	enemy_num=score/10 +10
	return enemy_num\


def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect =text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)  


 
def drop_enemies(enemy_list):
	delay= random.random()
	if len(enemy_list)<enemy_num and delay<0.1 :
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos= 0
		enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen,BLUE,(enemy_pos[0] , enemy_pos[1],enemy_size,enemy_size))

def update_enemy_positions(enemy_list,score):
	for idx,enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] +=SPEED
		else:
			enemy_list.pop(idx)
			score+=1
	return score

def collision_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos,player_pos):
			return True
	return False 



	
def detect_collision(player_pos,enemy_pos):
	p_x=player_pos[0]
	p_y	=player_pos[1]

	e_x=enemy_pos[0]
	e_y=enemy_pos[1]

	if (e_x>=p_x and e_x < (p_x+player_size)) or (p_x>=e_x and p_x < (e_x+enemy_size)):
		if (e_y>=p_y and e_y < (p_y+player_size)) or (p_y>=e_y and p_y < (e_y+enemy_size)):
			return True
	return False
while not game_over:
    for event in pygame.event.get():

    	if event.type == pygame.QUIT:
    		sys.exit()
    	
    	if event.type == pygame.KEYDOWN:
    		x=player_pos[0]
    		y=player_pos[1]
    		if event.key==pygame.K_LEFT:
    			x-=player_size

    		elif event.key==pygame.K_RIGHT:
    			x+=player_size
    		elif event.key == pygame.K_p:
                    pause = True
                    paused()

    		player_pos=[x,y]
    screen.fill((BACKGROUND_COLOR))
    
    		
    drop_enemies(enemy_list)

    score=update_enemy_positions(enemy_list,score)
    SPEED=set_level1(score,SPEED)
    enemy_num=set_level2(score,enemy_num)
    text= "Score:"+ str(score)
    label= myFont.render(text,1,YELLOW)
    #levelcross="Congrats, you have reached checkpoint score:"+str(checkpoint_score)
    #label2=myFont.render(levelcross,1,BLUE)
    screen.blit(label, (WIDTH-200, HEIGHT-40))


    if  collision_check(enemy_list, player_pos):
    	game_over= True
    	break


    draw_enemies(enemy_list)
    pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))

    clock.tick(30)

    pygame.display.update()
 