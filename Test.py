import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

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
    def __init__(self, imageFilename):
        self.image = pygame.image.load(imageFilename)
        self.rect = self.image.get_rect()
        self.Yspeed = 0

        self.pressedLeft = False
        self.pressedRight = False
        self.pressedBoost = False
        
        self.rect.x = 100
        self.rect.y = 600

        self.PressSinceGround = 0

    def CheckBoundary(self):
        if self.rect.x < -20:
            self.rect.x = 1080
        if self.rect.x > 1080:
            self.rect.x = 0

    def Movement(self):
        if self.pressedLeft == True:
            self.rect.x -= 20
            if self.pressedBoost == True:
                self.rect.x -= 30
        elif self.pressedRight == True:
            self.rect.x += 20
            if self.pressedBoost == True:
                self.rect.x += 30

    def CheckPlatforms(self, platrect1, platrect2, platrect3):
        if self.rect.x > platrect1.x - 20 and self.rect.x + self.rect.w < platrect1.x + (platrect1.w + 40) and self.rect.y < 150 and self.rect.y > 150-self.rect.h:
            self.rect.y = 149 - self.rect.h
            self.Yspeed = 0
            self.PressSinceGround = 0
        if self.rect.x > platrect2.x - 20 and self.rect.x + self.rect.w < platrect2.x + (platrect2.w + 40)  and self.rect.y < 250 and self.rect.y > 250-self.rect.h:
            self.rect.y = 249 - self.rect.h
            self.Yspeed = 0
            self.PressSinceGround = 0
        if self.rect.x > platrect3.x - 20 and self.rect.x + self.rect.w < platrect3.x + (platrect3.w + 40)  and self.rect.y < 420 and self.rect.y > 420-self.rect.h:
            self.rect.y = 420 - self.rect.h
            self.Yspeed = 0
            self.PressSinceGround = 0
        else:
            self.Yspeed +=2

    def SetPosition(self):
        self.rect = self.rect.move(0, self.Yspeed)

    def StopOnGround(self):
        if self.rect.y > 600:
            self.rect.y = 600
            self.Yspeed = 0
            self.PressSinceGround = 0
        elif self.rect.y < 0:
            self.Yspeed += 2

    def Display(self, screen):
        screen.blit(self.image, self.rect)
    


class Mario(Player):
    def __init__(self):
         super(Mario, self).__init__("mario_sprite.png")
    
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.PressSinceGround < 2:
                    self.Yspeed = -35
                self.PressSinceGround += 1
            elif event.key == pygame.K_a:
                self.pressedLeft = True
                self.image = pygame.image.load("mario_sprite_left.png")
            elif event.key == pygame.K_d:
                self.pressedRight = True
                self.image = pygame.image.load("mario_sprite.png")
            elif event.key == pygame.K_LSHIFT:
                self.pressedBoost = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.pressedLeft = False
            elif event.key == pygame.K_d:
                self.pressedRight = False
            elif event.key == pygame.K_LSHIFT:
                self.pressedBoost = False

class Luigi(Player):
    def __init__(self):
         super(Luigi, self).__init__("luigi_sprite.png")
         
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.PressSinceGround < 2:
                    self.Yspeed = -35
                self.PressSinceGround += 1
            elif event.key == pygame.K_LEFT:
                self.pressedLeft = True
                self.image = pygame.image.load("luigi_sprite_left.png")
            elif event.key == pygame.K_RIGHT:
                self.pressedRight = True
                self.image = pygame.image.load("luigi_sprite.png")
            elif event.key == pygame.K_RSHIFT:
                self.pressedBoost = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.pressedLeft = False
            elif event.key == pygame.K_RIGHT:
                self.pressedRight = False
            elif event.key == pygame.K_RSHIFT:
                self.pressedBoost = False



screen = pygame.display.set_mode(size)
p1 = Mario()
p2 = Luigi()
ground = pygame.image.load("ground.png")

platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")

groundrect = ground.get_rect()
platrect1 = platform1.get_rect()
platrect2 = platform2.get_rect()
platrect3 = platform3.get_rect()

groundrect.x = 0
groundrect.y = 600+p1.rect.h

platrect1.x = 0
platrect1.y = 120

platrect2.x = 820
platrect2.y = 220

platrect3.x = 380
platrect3.y = 420

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
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
    
    screen.fill(black)
    p1.Display(screen)
    p2.Display(screen)
    screen.blit(ground, groundrect)
    screen.blit(platform1, platrect1)
    screen.blit(platform2, platrect2)
    screen.blit(platform3, platrect3)
    pygame.display.flip()

    time.sleep(0.05)
