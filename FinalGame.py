from pygame import *
from pygame.sprite import *
import random
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

#Scoring for the game
score = 0
finalScore = 0

# Global variables
clock = pygame.time.Clock()
fire = 0
asteroidsVisible = 10

gameDisplay = pygame.display.set_mode((800, 600)) 



pygame.display.set_caption("Michigan Football Asteroid")

gameDisplay.fill(white)
pygame.display.update()


class Ship(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load("Images/ship.bmp").convert_alpha(), (30,30))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def get_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x = self.x - 10
        if key[pygame.K_RIGHT]:
            self.x = self.x + 10
        if key[pygame.K_UP]:
            self.y = self.y - 10
        if key[pygame.K_DOWN]:
            self.y = self.y + 10

    def update(self):
        self.rect.center = (self.x, self.y)


class bullet(Sprite):
    def __init__(self, x, y, dx, dy): 
        Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("Images/bullet.bmp").convert_alpha(), (10,10))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.rect.center = (self.x, self.y)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x, self.y)

class Asteroid(Sprite): 
    def __init__(self, x, y, mysize, dx, dy):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.size = mysize
        self.image = pygame.transform.scale(pygame.image.load("Images/asteroid.bmp").convert_alpha(), (mysize, mysize))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.center = (self.x, self.y)

    def kill(self):
        global score
        if self.size == 40:
            score += 10
        elif self.size == 60:
            score += 20
        
        Sprite.kill(self)

    def offScreen(self):
        Sprite.kill(self)


def generateAsteroid():
    size = random.randint(1, 2)
    if size == 1:
        ast_size = 40
    elif size == 2:
        ast_size = 60

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

    return Asteroid(ast_x, ast_y, ast_size, ast_dx, ast_dy)

armory = pygame.sprite.Group() #Group of fired bullets
space = pygame.sprite.Group() #Group of created asteroids
Ship = Ship(400, 300)

sound = pygame.mixer.Sound("Sound/gamesound.wav")
sound.play()

gameExit = False
gameOver = False
while not gameExit:
    
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    direction = pygame.key.get_pressed()
    shot_fired = False
    if direction[pygame.K_w]:
        shot = bullet(Ship.x, Ship.y + 30, 0, -30)
        shot_fired = True
    elif direction[pygame.K_a]:
        shot = bullet(Ship.x + 30, Ship.y, -30, 0)
        shot_fired = True
    elif direction[pygame.K_s]:
        shot = bullet(Ship.x, Ship.y - 30, 0, 30)
        shot_fired = True
    elif direction[pygame.K_d]:
        shot = bullet(Ship.x - 30, Ship.y, 30, 0)
        shot_fired = True
    if shot_fired == True:
        armory.add(shot)

    #Collision detection
    if pygame.sprite.spritecollide(Ship, space, False, False):
        gameOver = True
        finalScore =  score

    pygame.sprite.groupcollide(armory, space, True, True)
    
    for asteroid in space.sprites():
        if asteroid.x < -500 or asteroid.x > 1300 or asteroid.y < -400 or asteroid.y > 1000:
            asteroid.offScreen()

    for round in armory.sprites():
        if round.x > 800 or round.x < 0 or round.y > 600 or round.y < 0:
            Sprite.kill(round)

    while (len(space.sprites()) < asteroidsVisible):
        space.add(generateAsteroid())

    Ship.get_input()

    # Draw scoreboard
    if not gameOver:
        text = font.Font(None, 40)
        pygame.draw.rect(gameDisplay,(230, 230, 230),(0, 0, 900, 40))
        scoreboard = text.render("Score: " + str(score), 1, red)
        gameDisplay.blit(scoreboard, (10, 5))
    else:
        text = font.Font(None, 40)
        pygame.draw.rect(gameDisplay,(230, 230, 230),(0, 0, 900, 40))
        scoreboard = text.render("Game Over.  Your score is: " + str(finalScore), 1, black)
        gameDisplay.blit(scoreboard, (10, 5))


    sprites = RenderPlain(armory, space, Ship)
    sprites.update()
    sprites.draw(gameDisplay)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()


