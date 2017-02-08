import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
black = 0, 0, 0


class Player():
    fallSpeed = 2
    moveSpeed = 20
    boostMoveSpeed = 30
    
    def __init__(self, x, y, imageFilename):
        self.image = pygame.image.load(imageFilename)
        self.rect = self.image.get_rect()
        self.Yspeed = 0

        self.pressedLeft = False
        self.pressedRight = False
        self.pressedBoost = False
        
        self.rect.x = x
        self.rect.y = y

        self.PressSinceGround = 0

    def CheckBoundary(self):
        if self.rect.x < -20:
            self.rect.x = 1080
        if self.rect.x > 1080:
            self.rect.x = 0

    def Movement(self):
        if self.pressedLeft == True:
            self.rect.x -= Player.moveSpeed
            if self.pressedBoost == True:
                self.rect.x -= Player.boostMoveSpeed
        elif self.pressedRight == True:
            self.rect.x += Player.moveSpeed
            if self.pressedBoost == True:
                self.rect.x += Player.boostMoveSpeed

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
            self.Yspeed += Player.fallSpeed

    def SetPosition(self):
        self.rect = self.rect.move(0, self.Yspeed)

    def StopOnGround(self):
        if self.rect.y > 600:
            self.rect.y = 600
            self.Yspeed = 0
            self.PressSinceGround = 0
        elif self.rect.y < 0:
            self.Yspeed += Player.fallSpeed

    def Display(self, screen):
        screen.blit(self.image, self.rect)
    


class Mario(Player):
    allowedDoubleJumps = 2
    jumpSpeed = 35
    
    def __init__(self, x, y):
         super(Mario, self).__init__(x, y, "mario_sprite.png")
    
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.PressSinceGround < Mario.allowedDoubleJumps:
                    self.Yspeed = -Mario.jumpSpeed
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
    allowedDoubleJumps = 2
    jumpSpeed = 35
    
    def __init__(self, x, y):
         super(Luigi, self).__init__(x, y, "luigi_sprite.png")
        
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.PressSinceGround < Luigi.allowedDoubleJumps:
                    self.Yspeed = -Luigi.jumpSpeed
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

class Platform():
    def __init__(self, filename, x, y):
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Display(self, screen):
        screen.blit(self.image, self.rect)
        


screen = pygame.display.set_mode(size)
p1 = Mario(100, 600)
p2 = Luigi(100, 600)

ground = Platform("ground.png", 0, 600+p1.rect.h) 
platform1 = Platform("platform1.png", 0, 120) 
platform2 = Platform("platform2.png", 820, 220) 
platform3 = Platform("platform3.png", 380, 420) 

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
    
    p1.CheckPlatforms(platform1.rect, platform2.rect, platform3.rect)
    p2.CheckPlatforms(platform1.rect, platform2.rect, platform3.rect)
    
    p1.SetPosition()
    p2.SetPosition()
    
    p1.StopOnGround()
    p2.StopOnGround()
    
    screen.fill(black)
    p1.Display(screen)
    p2.Display(screen)
    ground.Display(screen)
    platform1.Display(screen)
    platform2.Display(screen)
    platform3.Display(screen)
    pygame.display.flip()

    time.sleep(0.05)
