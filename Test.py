import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

<<<<<<< HEAD

class Image():
    def __init__(self, FileName, Screen):
        self.Screen = Screen
        self.FileName = FileName
        self.Image = pygame.image.load(FileName)
        self.X = 0
        self.Y = 0
        self.W = self.Image.get_rect().w
        self.H = self.Image.get_rect().h

    def Display(self):
        self.Screen.blit(self.Image, [self.X, self.Y, self.W, self.H])


class Player():
    def __init__(self, X, Y, Speed, FileName, Screen):
        self.Image = Image(FileName, Screen)
        self.X = X
        self.Y = Y
        self.W = self.Image.W
        self.H = self.Image.W
        self.BaseSpeed = Speed
        self.Speed = self.BaseSpeed

    def Update(self, eventsList):
        for event in eventsList:
            self.HandleEvent(event)

        self.Display()

    # Private
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.Move('Up')
            elif event.key == pygame.K_a:
                self.Move('Left')
            elif event.key == pygame.K_s:
                self.Move('Down')
            elif event.key == pygame.K_d:
                self.Move('Right')
            elif event.key == pygame.K_LSHIFT:
                self.Boost()

    # Private
    def Boost(self):
        self.Speed = self.BaseSpeed * 2
    
    # Private
    def Move(self, Direction):
        if Direction == 'Up':
            if PressSinceGround < 2:
                p1Yspeed = -35
            PressSinceGround += 1
        elif Direction == 'Left':
            pressedLeft = True
        elif Direction == 'Right':
            pressedRight = True
            
    # Private
    def Display(self):
        self.Image.X = self.X
        self.Image.Y = self.Y
        self.Image.Display()



class Player1():
    def __init__(self):
        self.player1 = pygame.image.load("mario_sprite.png")
        self.p1rect = self.player1.get_rect()
        self.p1Yspeed = 0

        self.pressedLeft = False
        self.pressedRight = False
        self.pressedLBoost = False
        
        self.p1rect.x = 100
        self.p1rect.y = 600

        self.PressSinceGround = 0

    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.PressSinceGround < 2:
                    self.p1Yspeed = -35
                self.PressSinceGround += 1
            elif event.key == pygame.K_a:
                self.pressedLeft = True
                self.player1 = pygame.image.load("mario_sprite_left.png")
            elif event.key == pygame.K_d:
                self.pressedRight = True
                self.player1 = pygame.image.load("mario_sprite.png")
            elif event.key == pygame.K_LSHIFT:
                self.pressedLBoost = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.pressedLeft = False
            elif event.key == pygame.K_d:
                self.pressedRight = False
            elif event.key == pygame.K_LSHIFT:
                self.pressedLBoost = False

    def CheckBoundary(self):
        if self.p1rect.x < -20:
            self.p1rect.x = 1080
        if self.p1rect.x > 1080:
            self.p1rect.x = 0

    def Movement(self):
        if self.pressedLeft == True:
            self.p1rect.x -= 20
            if self.pressedLBoost == True:
                self.p1rect.x -= 30
        elif self.pressedRight == True:
            self.p1rect.x += 20
            if self.pressedLBoost == True:
                self.p1rect.x += 30

    def CheckPlatforms(self, platrect1, platrect2, platrect3):
        if self.p1rect.x > platrect1.x - 20 and self.p1rect.x + self.p1rect.w < platrect1.x + (platrect1.w + 40) and self.p1rect.y < 150 and self.p1rect.y > 150-self.p1rect.h:
            self.p1rect.y = 149 - self.p1rect.h
            self.p1Yspeed = 0
            self.PressSinceGround = 0
        if self.p1rect.x > platrect2.x - 20 and self.p1rect.x + self.p1rect.w < platrect2.x + (platrect2.w + 40)  and self.p1rect.y < 250 and self.p1rect.y > 250-self.p1rect.h:
            self.p1rect.y = 249 - self.p1rect.h
            self.p1Yspeed = 0
            self.PressSinceGround = 0
        if self.p1rect.x > platrect3.x - 20 and self.p1rect.x + self.p1rect.w < platrect3.x + (platrect3.w + 40)  and self.p1rect.y < 420 and self.p1rect.y > 420-self.p1rect.h:
            self.p1rect.y = 420 - self.p1rect.h
            self.p1Yspeed = 0
            self.PressSinceGround = 0
        else:
            self.p1Yspeed +=2

    def SetPosition(self):
        self.p1rect = self.p1rect.move(0, self.p1Yspeed)

    def StopOnGround(self):
        if self.p1rect.y > 600:
            self.p1rect.y = 600
            self.p1Yspeed = 0
            self.PressSinceGround = 0
        elif self.p1rect.y < 0:
            self.p1Yspeed += 2

    def Display(self, screen):
        screen.blit(self.player1, self.p1rect)


class Player2():
    def __init__(self):
        self.player2 = pygame.image.load("luigi_sprite.png")
        self.p2rect = self.player2.get_rect()
        self.p2Yspeed = 0

        self.pressedLeftArrow = False
        self.pressedRightArrow = False
        self.pressedRBoost = False
        
        self.p2rect.x = 100
        self.p2rect.y = 600

        self.PressSinceGround = 0
        
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.PressSinceGround < 2:
                    self.p2Yspeed = -35
                self.PressSinceGround += 1
            elif event.key == pygame.K_LEFT:
                self.pressedLeftArrow = True
                self.player2 = pygame.image.load("luigi_sprite_left.png")
            elif event.key == pygame.K_RIGHT:
                self.pressedRightArrow = True
                self.player2 = pygame.image.load("luigi_sprite.png")
            elif event.key == pygame.K_RSHIFT:
                self.pressedRBoost = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.pressedLeftArrow = False
            elif event.key == pygame.K_RIGHT:
                self.pressedRightArrow = False
            elif event.key == pygame.K_RSHIFT:
                self.pressedRBoost = False

    def CheckBoundary(self):
        if self.p2rect.x < -0:
            self.p2rect.x = 1080
        if self.p2rect.x > 1080:
            self.p2rect.x = 0 

    def Movement(self):
        if self.pressedLeftArrow == True:
            self.p2rect.x -= 20
            if self.pressedRBoost == True:
                self.p2rect.x -= 30
        elif self.pressedRightArrow == True:
            self.p2rect.x += 20
            if self.pressedRBoost == True:
                self.p2rect.x += 30

    def CheckPlatforms(self, platrect1, platrect2, platrect3):
        if self.p2rect.x > platrect1.x - 20 and self.p2rect.x + self.p2rect.w < platrect1.x + (platrect1.w + 40) and self.p2rect.y < 150 and self.p2rect.y > 150-self.p2rect.h:
            self.p2rect.y = 150 - self.p2rect.h
            self.p2Yspeed = 0
            self.PressSinceGround = 0
        if self.p2rect.x > platrect2.x - 20 and self.p2rect.x + self.p2rect.w < platrect2.x + (platrect2.w + 40)  and self.p2rect.y < 250 and self.p2rect.y > 250-self.p2rect.h:
            self.p2rect.y = 250 - self.p2rect.h
            self.p2Yspeed = 0
            self.PressSinceGround = 0
        if self.p2rect.x > platrect3.x - 20 and self.p2rect.x + self.p2rect.w < platrect3.x + (platrect3.w + 40)  and self.p2rect.y < 420 and self.p2rect.y > 420-self.p2rect.h:
            self.p2rect.y = 420 - self.p2rect.h
            self.p2Yspeed = 0
            self.PressSinceGround = 0
        else:
            self.p2Yspeed +=2

    def SetPosition(self):
        self.p2rect = self.p2rect.move(0, self.p2Yspeed)

    def StopOnGround(self):
        if self.p2rect.y > 600:
            self.p2rect.y = 600
            self.p2Yspeed = 0
            self.PressSinceGround = 0
        elif self.p2rect.y < 0:
            self.p2Yspeed += 2

    def Display(self, screen):
        screen.blit(self.player2, self.p2rect)

        



screen = pygame.display.set_mode(size)
p1 = Player1()
p2 = Player2()
=======
screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

ballrect.x = 100
ballrect.y = 600

player1 = pygame.image.load("mario_sprite.png")
player2 = pygame.image.load("luigi_sprite.png")
>>>>>>> a33f3442d6a0628c5ff6bd883890bb32cb545c39
ground = pygame.image.load("ground.png")

platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")

groundrect = ground.get_rect()
platrect1 = platform1.get_rect()
platrect2 = platform2.get_rect()
platrect3 = platform3.get_rect()

<<<<<<< HEAD
=======
#Player initial speed
p1Yspeed = 0
p2Yspeed = 0

#Initial Movement presets
pressedLeft = False
pressedRight = False
pressedLBoost = False
pressedLeftArrow = False
pressedRightArrow = False
pressedRBoost = False

>>>>>>> a33f3442d6a0628c5ff6bd883890bb32cb545c39
groundrect.x = 0
groundrect.y = 600+p1.p1rect.h

platrect1.x = 0
platrect1.y = 120

platrect2.x = 820
platrect2.y = 220

platrect3.x = 380
platrect3.y = 420
<<<<<<< HEAD

=======
p1SinceGround = 0
p2SinceGround = 0
>>>>>>> a33f3442d6a0628c5ff6bd883890bb32cb545c39

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
<<<<<<< HEAD
        p1.HandleEvent(event)
        p2.HandleEvent(event)

    p1.CheckBoundary()
    p2.CheckBoundary()
    
    p1.Movement()
    p2.Movement()
    
    p1.CheckPlatforms(platrect1, platrect2, platrect3)
    p2.CheckPlatforms(platrect1, platrect2, platrect3)
    
    p1.SetPosition()
    p2.SetPosition()
    
    p1.StopOnGround()
    p2.StopOnGround()
    
=======
        if event.type == pygame.KEYDOWN:
            #_____Player1________________________________________________
            if event.key == pygame.K_w:
                if p1SinceGround < 2:
                    p1Yspeed = -35
                p1SinceGround += 1
            elif event.key == pygame.K_a:
                pressedLeft = True
                player1 = pygame.image.load("mario_sprite_left.png")
            elif event.key == pygame.K_d:
                pressedRight = True
                player1 = pygame.image.load("mario_sprite.png")
            elif event.key == pygame.K_LSHIFT:
                pressedLBoost = True     
            #_____Player2________________________________________________
            if event.key == pygame.K_UP:
                if p2SinceGround < 2:
                    p2Yspeed = -35
                p2SinceGround += 1
            elif event.key == pygame.K_LEFT:
                pressedLeftArrow = True
                player2 = pygame.image.load("luigi_sprite_left.png")
            elif event.key == pygame.K_RIGHT:
                pressedRightArrow = True
                player2 = pygame.image.load("luigi_sprite.png")
            elif event.key == pygame.K_RSHIFT:
                pressedRBoost = True
                
        elif event.type == pygame.KEYUP:
            #_____Player1________________________________________________
            if event.key == pygame.K_a:
                pressedLeft = False
            elif event.key == pygame.K_d:
                pressedRight = False
            elif event.key == pygame.K_LSHIFT:
                pressedLBoost = False
            #_____Player2________________________________________________
            if event.key == pygame.K_LEFT:
                pressedLeftArrow = False
            elif event.key == pygame.K_RIGHT:
                pressedRightArrow = False
            elif event.key == pygame.K_RSHIFT:
                pressedRBoost = False
                
    #boundaries
    if p1rect.x < -20:
        p1rect.x = 1080
    if p1rect.x > 1080:
        p1rect.x = 0
        
    if p2rect.x < -0:
        p2rect.x = 1080
    if p2rect.x > 1080:
        p2rect.x = 0 

    #movement
    #_____Player1________________________________________________
    if pressedLeft == True:
        p1rect.x -= 20
        if pressedLBoost == True:
            p1rect.x -= 30
    elif pressedRight == True:
        p1rect.x += 20
        if pressedLBoost == True:
            p1rect.x += 30
    #_____Player2________________________________________________    
    if pressedLeftArrow == True:
        p2rect.x -= 20
        if pressedRBoost == True:
            p2rect.x -= 30
    elif pressedRightArrow == True:
        p2rect.x += 20
        if pressedRBoost == True:
            p2rect.x += 30
            
    #platorm ranges so he cand stand above the ledges
    #Player 1
    if p1rect.x > platrect1.x - 40 and p1rect.x + p1rect.w < platrect1.x + (platrect1.w + 40) and p1rect.y < 120 and p1rect.y > 120-p1rect.h:
        p1rect.y = 120 - p1rect.h
        p1Yspeed = 0
        p1SinceGround = 0
    if p1rect.x > platrect2.x - 40 and p1rect.x + p1rect.w < platrect2.x + (platrect2.w + 40)  and p1rect.y < 220 and p1rect.y > 220-p1rect.h:
        p1rect.y = 220 - p1rect.h
        p1Yspeed = 0
        p1SinceGround = 0
    if p1rect.x > platrect3.x - 40 and p1rect.x + p1rect.w < platrect3.x + (platrect3.w + 40)  and p1rect.y < 420 and p1rect.y > 420-p1rect.h:
        p1rect.y = 420 - p1rect.h
        p1Yspeed = 0
        p1SinceGround = 0
    else:
        p1Yspeed +=2
        
    #Player 2
    if p2rect.x > platrect1.x - 20 and p2rect.x + p2rect.w < platrect1.x + (platrect1.w + 40) and p2rect.y < 120 and p2rect.y > 120-p2rect.h:
        p2rect.y = 120 - p2rect.h
        p2Yspeed = 0
        p2inceGround = 0
    if p2rect.x > platrect2.x - 20 and p2rect.x + p2rect.w < platrect2.x + (platrect2.w + 40)  and p2rect.y < 220 and p2rect.y > 220-p2rect.h:
        p2rect.y = 220 - p2rect.h
        p2Yspeed = 0
        p2SinceGround = 0
    if p2rect.x > platrect3.x - 20 and p2rect.x + p2rect.w < platrect3.x + (platrect3.w + 40)  and p2rect.y < 420 and p2rect.y > 420-p2rect.h:
        p2rect.y = 420 - p2rect.h
        p2Yspeed = 0
        p2SinceGround = 0
    else:
        p2Yspeed +=2
        
    p1rect = p1rect.move(0, p1Yspeed)
    p2rect = p2rect.move(0, p2Yspeed)

    if p1rect.y > 600:
        p1rect.y = 600
        p1Yspeed = 0
        p1SinceGround = 0
    elif p1rect.y < 0:
        p1Yspeed += 2
        
    if p2rect.y > 600:
        p2rect.y = 600
        p2Yspeed = 0
        p2SinceGround = 0
    elif p2rect.y < 0:
        p2Yspeed += 2

>>>>>>> a33f3442d6a0628c5ff6bd883890bb32cb545c39
    screen.fill(black)
    p1.Display(screen)
    p2.Display(screen)
    screen.blit(ground, groundrect)
    screen.blit(platform1, platrect1)
    screen.blit(platform2, platrect2)
    screen.blit(platform3, platrect3)
    pygame.display.flip()

    time.sleep(0.05)
