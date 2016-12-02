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

#List of fired bullets
armory = []

gameDisplay = pygame.display.set_mode((800, 600)) # -> Surface

#background = pygame.image.load(image_name)-> setting a background image

pygame.display.set_caption("Michigan Football Asteroid")

pygame.display.update()

gameDisplay.fill(white)
pygame.display.update()

def updateShip():
    ship = gameDisplay.fill(blue, rect=[x_pos, y_pos, 20, 20])

class bullet():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    # def myMethodToIncreasedx(number):
    #     self.dx = self.dx + number

# bullet1 = bullet(50, 100, 30, 0)
# #bullet1.dx -> 30
# bullet1.myMethodToIncreasedx(5)
# #bullet1.dx -> 35

def fireBullet(direction):
    if direction == pygame.K_w:
        shot = bullet(x_pos, y_pos + 30, 0, -30) 
    elif direction == pygame.K_a: # left
        shot = bullet(x_pos + 30, y_pos, -30, 0) 
    elif direction == pygame.K_s: # down
        shot = bullet(x_pos, y_pos - 30, 0, 30) 
    elif direction == pygame.K_d: # right
        shot = bullet(x_pos - 30, y_pos, 30, 0)
    armory.append(shot)

# shot = bullet(20, 20 + 30, 0, -30)
# shot.x = 20   calling shot.x will return the value 20
# shot.y = 50
# shot.dx = 0
# shot.dy = -30

# bullet1 = bullet(100, 300, 10, 10)
# bullet2 = bullet(400, 200, 10 ,10)
# print(bullet1.x)  -> 100
# print(bullet2.dx) -> 10
# bullet1.x = 77
# bullet2.dx = 42
# print(bullet1.x)  -> 77
# print(bullet2.dx) -> 42

def updateBullets():
    for i in armory: # for now, armory is just [shot] shot is a bullet object
        i.x = i.x + i.dx 
        i.y = i.y + i.dy 
    for i in armory:
        if (i.x < 0 or i.y < 0): 
            armory.remove(i)

        # first time through game while loop
        # i.x += dx   this is i.x = 20 + 0 = 20
        # i.y += dy   this is i.y = 50 - 30 = 20
        # second time through game while loop
        # i.x = 20 + 0
        # i.y = 20 - 30 = -10
        gameDisplay.fill(red, rect =[i.x, i.y, 10, 10])

class Asteroid(pygame.Rect):
    def __init__(self, asteroid_x, asteroid_y, mysize, speed, direction):
        pygame.Rect.__init__(self, asteroid_x, asteroid_y, mysize, mysize)
        self.asteroid_x = asteroid_x
        self.asteroid_y = asteroid_y
        self.mysize = mysize
        self.speed = speed
        self.direction = direction

# asteroid1 = asteroid(x, y, "large", "fast", "NE")
# "large" : 80 square => height = width = 80

#def updateAsteroids():


# def checkCollisions():
#     for asteroid in space:
#         ship.collidelist(space)


gameExit = False
while not gameExit:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_pos -= 10
        if event.key == pygame.K_RIGHT:
            x_pos += 10
        if event.key == pygame.K_UP:
            y_pos -= 10
        if event.key == pygame.K_DOWN:
            y_pos += 10
        if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]: #actually firing down should I just change to -30
            fireBullet(event.key)
    #screen.blit(background, (0,0)) -> in game command for line 21
    asteroid1 = Asteroid(20, 50, 80, 80, 1)

    updateBullets()
    updateShip()
    # updateAsteroids()
    # checkCollisions()
    pygame.display.update()


pygame.quit()
quit()

# something random needs to generate asteroids
#   some random number generation for each parameter (x, y, size, speed, direction)
#       consider random number generation for size: 1, 2, 3 => 40x40, 60x60, 80x80
#   upon asteroid initiliazation store asteroid in space list
# asteroids


