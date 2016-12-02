class ship(RawTurtle):
	def __init__(self, surface, dx, dy, x, y):
		RawTurtle.__init__(self, canvas)


while True:
	e = event.wait()
	if e.type == QUIT:
		pygame.quit()
	
	screen.fill((blue)
	display.update()



class Asteroid(RawTurtle):
	def __init__(self, dx, dy,) 

while True:
	e = event.wait #wait for an event
	if e.type == QUIT:
		PyGame.quit() #exit the game
		break
	elif e.type == type:
		#code to handle some other type of events
	elif ...

class name(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("filename").convert()
			self.rect = self.image.get_rect().move(X,Y) #Use the image size to define the rect field

#Collisions
	if sprite.rect.collidetect(sprite2.rect): #they collide

	groupcollide(group1, group2, kill1, kill2) #returns list of all sprites in group1 that collide with group2

#Drawing text:font
	name.render("text", True, (red, green, blue))
	#example
	my_font = Font(None, 16)
	text = my_font.render("Hello", True, (0,0,0))

#Key Presses
	key.get_pressed() #returns array of keys held down 
	#example
	keys_down = key.get_pressed()
	if keys_down[K_LEFT]: #left arrow is being held down