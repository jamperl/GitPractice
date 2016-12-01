from turtle import *
import tkinter.messagebox
import tkinter
import random
import math

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

class PhotonTorpedo(RawTurtle):
    def __init__(self,canvas,x,y,direction,dx,dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x,y)
        self.setheading(direction)
        self.color("Green")
        self.lifespan = 200
        self.dx = math.cos(math.radians(direction)) * 2 + dx
        self.dy = math.sin(math.radians(direction)) * 2 + dy
        self.shape("bullet")
    
    def getLifeSpan(self):
        return self.lifespan

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def move(self):
        self.lifespan = self.lifespan - 1
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()
        x = (self.dx + x - screenMinX) %  \
            (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % \
            (screenMaxY - screenMinY) + screenMinY
   
        self.goto(x,y)




class Asteroid(RawTurtle):
    def __init__(self,canvas,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.goto(x,y)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.shape("rock" + str(size))

    def getSize(self):
        return self.size
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy
    
    def setDX(self,dx):
        self.dx = dx
        
    def setDY(self,dy):
        self.dy = dy
        
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)
   
    def getRadius(self):
        return self.size * 10 - 5

class SpaceShip(RawTurtle):
    def __init__(self,canvas,dx,dy,x,y):
        RawTurtle.__init__(self,canvas)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.shape("ship")

    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()

        x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        
        self.goto(x,y)

    def fireEngine(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        self.dx = self.dx + x
        self.dy = self.dy + y
   
    def getRadius(self):
        return 2
    
    def getDX(self):
        return self.dx
    
    def getDY(self):
        return self.dy

def intersect(object1,object2):
        dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
        
        radius1 = object1.getRadius()
        radius2 = object2.getRadius()
        
        # The following if statement could be written as 
        # return dist <= radius1+radius2
        if dist <= radius1+radius2:
            return True
        else:
            return False

def main():
    
    # Start by creating a RawTurtle object for the window. 
    root = tkinter.Tk()
    root.title("Asteroids!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("rock3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))
    screen.register_shape("rock2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
    screen.register_shape("rock1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
    screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
    screen.register_shape("bullet",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    t.ht()
    

    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    scoreTitle = tkinter.Label(frame,text="Score")
    scoreTitle.pack()
    scoreFrame = tkinter.Frame(frame,height=2, bd=1, \
        relief=tkinter.SUNKEN)
    scoreFrame.pack()
    score = tkinter.Label(scoreFrame,height=2,width=20,\
        textvariable=scoreVal,fg="Yellow",bg="black")
    
    score.pack()

    def quitHandler():
        root.destroy()
        root.quit()

    quitButton = tkinter.Button(frame, text = "Quit", command=quitHandler)
    quitButton.pack()
    
    screen.tracer(10)
    
    ship = SpaceShip(cv,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY)
    
    asteroids = []

    bullets = [] 
    
    for k in range(5):
        dx = random.random() * 6 - 3
        dy = random.random() * 6 - 3
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        asteroid = Asteroid(cv,dx,dy,x,y,3)

        asteroids.append(asteroid)

    def play():
    
        deadbullets = [] 

        for bullet in bullets:
            bullet.move()

            if bullet.getLifeSpan() <= 0:
                deadbullets.append(bullet)

        for bullet in deadbullets:
            try:
                bullets.remove(bullet)
            except:
                print ("didn't find bullet")

            bullet.goto(-screenMinX*2, -screenMinY*2)
            bullet.ht

        ship.move()
        
        hitasteroids = []

        for bullet in bullets:
            for asteroid in asteroids:
                if not asteroid in hitasteroids and \
                             intersect(bullet,asteroid):
                    deadbullets.append(bullet)
                    hitasteroids.append(asteroid)
                    asteroid.setDX(bullet.getDX() + \
                      asteroid.getDX())
                    asteroid.setDY(bullet.getDY() + \
                      asteroid.getDY())

        for asteroid in hitasteroids:
            try:
                asteroids.remove(asteroid)
            except:
                print("didn't find asteroid in list")
               
            asteroid.ht()
            size = asteroid.getSize()
            
            score = int(scoreVal.get())
            
            if size == 3:
                score += 20
            elif size == 2:
                score += 50
            elif size == 1:
                score += 100
                
            scoreVal.set(str(score))
            
            if asteroid.getSize() > 1:
                dx = asteroid.getDX()
                dy = asteroid.getDY()
                dist = math.sqrt(dx ** 2 + dy ** 2)
                normDx = asteroid.getDX() / dist
                normDy = asteroid.getDY() / dist
                
                asteroid1 = Asteroid(cv,-normDy,normDx, \
                  asteroid.xcor(),asteroid.ycor(), \
                  asteroid.getSize()-1)
                asteroid2 = Asteroid(cv,normDy,-normDx, \
                  asteroid.xcor(),asteroid.ycor(), \
                  asteroid.getSize()-1)
                asteroids.append(asteroid1)
                asteroids.append(asteroid2)


        for asteroid in asteroids:
            asteroid.move()

        # Set the timer to go off again in 5 milliseconds
        screen.ontimer(play, 5)

    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play, 5)
    
    
    def turnright():
        ship.setheading(ship.heading()-7)

        screen.onkeypress(turnRight, K_6)

    def turnLeft():
        ship.setheading(ship.heading()+7)
        
        screen.onkeypress(turnLeft, K_4)
    
    def forward():
        ship.fireEngine()
        
        screen.onkeypress(forward, " ")

    def fire():
        bullet = PhotonTorpedo(cv,ship.xcor(),ship.ycor(), \
            ship.heading(),ship.getDX(),ship.getDY())
        bullets.append(bullet)
    
    screen.onkeypress(fire, " ")
    
    screen.listen()
    tkinter.mainloop()
  
if __name__ == "__main__":
    main()
  