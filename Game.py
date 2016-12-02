import pygame
pygame.init()
import random

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
#List of created asteroids
space = []

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

class Asteroid(pygame.Rect): # Asteroid is a subclass of pygame.Rect class => pygame sees Asteroid objects as pygame Rects (because they ARE Rects, with some extra attributes we tacked on)
    def __init__(self, x, y, mysize, dx, dy):
        pygame.Rect.__init__(self, x, y, mysize, mysize)
        # self.x = x
        # self.y = y
        self.mysize = mysize
        self.dx = dx
        self.dy = dy
        # size is one of three: small, medium, large
        # speed is one of three settings: slow, normal, fast (delta 4, 8, 12)
        # direction is one of 8: N, E, S, W, NE, SW, NW, SE
        # random generation will need to output 1, 2, or 3 for size as well as speed and 1-8 for direction
        # ^ can it do this??

# asteroid1 = asteroid(x, y, "large", "fast", "NE")
# "large" : 80 square => height = width = 80
# stating "slow" would be convenient when instantiating an object but we never manually instantiate -- this random generator makes ALL the asteroids

def generateAsteroid():
    # random.randint(a,b)
    # determine size
    size = random.randint(1, 2)
    if size == 1:
        ast_size = 40
    elif size == 2:
        ast_size = 60

    # determine dx and dy
    velocity = random.randint(1,8)
    if velocity == 1: #NE and slow
        ast_dx = 2
        ast_dy = -2
    elif velocity == 2:  #NE and fast
        ast_dx = 4
        ast_dy = -4
    elif velocity == 3:  #NW and slow
        ast_dx = -2
        ast_dy = -2
    elif velocity == 4:   #NW and fast
        ast_dx = -4
        ast_dy = -4
    elif velocity == 5:   #SE and slow
        ast_dx = 2
        ast_dy = 2
    elif velocity == 6:   #SE and fast
        ast_dx = 4
        ast_dy = 4
    elif velocity == 7:   #SW and slow
        ast_dx = -2 
        ast_dy = 2
    elif velocity == 8:   #SW and fast
        ast_dx = -4
        ast_dy = -4

    if (velocity == 1 or velocity == 2): # "NE":
        # asteroid should start in quadrant 3
        ast_x = random.randint(-400, 0)
        ast_y = random.randint(600, 900)
    elif (velocity == 7 or velocity == 8): # "Sw":
        # asteroid should start in quadrant 2
        ast_x = random.randint(800, 1200)
        ast_y = random.randint(-300, 0)
    elif (velocity == 3 or velocity == 4): # "NW":
        # asteroid should start in quadrant 4
        ast_x = random.randint(800, 1200)
        ast_y = random.randint(600, 900)
    elif (velocity == 5 or velocity == 6): # "SE":
        # asteroid should start in quadrant 1
        ast_x = random.randint(-400, 0)
        ast_y = random.randint(-300, 0)

    this_is_an_asteroid = Asteroid(ast_x, ast_y, ast_size, ast_dx, ast_dy)
    space.append(this_is_an_asteroid)

    # manual instantiation:    nameofasteroidinstance = Asteroid(50, 50, 40, 2, 2)
    # "dynamic" instantiation: nameofasteroidinstance = Asteroid(ast_x, ast_y, ast_size, ast_dx, ast_dy)

def updateAsteroids(): # obligate this function to the drawing of the asteroid onto the display
    for rock in space:
        # update the asteroid's knowledge ("attribute" storing the value) of its own position
        rock.x = rock.x + rock.dx
        rock.y = rock.y + rock.dy
        # check if asteroid is off the screen
        #   if so, remove it from space list
        #   and generateAsteriod will see the length of space is < 6 and thus will generate a new Asteroid
        gameDisplay.fill(black, rock) # rock is an Asteroid, and Asteroids ARE pygame Rects (that have extra traits on them)
    

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
    #asteroid1 = Asteroid(20, 50, 80, 80, 1)

    if len(space) < 6:   # now we need to delete asteroids from the space list once they are destroyed (# MAYBE TODO: or when off screen)
        generateAsteroid() # will create an asteroid and put it into the space list

    updateBullets()
    updateShip()
    updateAsteroids()
    # checkCollisions()
    pygame.display.update()


pygame.quit()
quit()

# something random needs to generate asteroids
#   some random number generation for each parameter (x, y, size, speed, direction)
#       consider random number generation for size: 1, 2, 3 => 40x40, 60x60, 80x80
#   upon asteroid initiliazation store asteroid in space list
# asteroids


