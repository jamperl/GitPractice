import pygame
pygame.init()

#create colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position vars
x_pos = 0
y_pos = 0
fire = 0

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Michigan Football Asteroid")

pygame.display.update()

gameDisplay.fill(white)
pygame.display.update()
	

gameExit = False
while not gameExit:
	gameDisplay.fill(white)
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			gameExit = True
		gameDisplay.fill(blue, rect=[50,50, 20,20]) #xpos ypos width height

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			x_pos -= 10
		if event.key == pygame.K_RIGHT:
			x_pos += 10
		if event.key == pygame.K_UP:
			y_pos -= 10
		if event.key == pygame.K_DOWN:
			y_pos += 10
		if event.key == pygame.K_w:
			fire = 1
			bullet_x = x_pos
			bullet_y = y_pos
			bullet_dx = 0
			bullet_dy = 30
	
	if fire == 1:
		bullet_y += bullet_dy
		gameDisplay.fill(red, rect=[bullet_x, bullet_y, 10, 10])
	gameDisplay.fill(blue, rect=[x_pos, y_pos, 20, 20])
	pygame.display.update()


pygame.quit()
quit()



