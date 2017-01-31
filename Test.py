import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

ballrect.x = 100
ballrect.y = 600

player1 = pygame.image.load("mario_sprite.png")
player2 = pygame.image.load("luigi_sprite.png")
ground = pygame.image.load("ground.png")

platform1 = pygame.image.load("platform1.png")
platform2 = pygame.image.load("platform2.png")
platform3 = pygame.image.load("platform3.png")

p1rect = player1.get_rect()
p2rect = player2.get_rect()

groundrect = ground.get_rect()
platrect1 = platform1.get_rect()
platrect2 = platform2.get_rect()
platrect3 = platform3.get_rect()

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

groundrect.x = 0
groundrect.y = 600+p1rect.h

p1rect.x = 100
p1rect.y = 600

p2rect.x = 100
p2rect.y = 600

platrect1.x = 0
platrect1.y = 120

platrect2.x = 820
platrect2.y = 220

platrect3.x = 380
platrect3.y = 420
p1SinceGround = 0
p2SinceGround = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
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

    screen.fill(black)
    screen.blit(player1, p1rect)
    screen.blit(player2, p2rect)
    screen.blit(ground, groundrect)
    screen.blit(platform1, platrect1)
    screen.blit(platform2, platrect2)
    screen.blit(platform3, platrect3)
    pygame.display.flip()

    time.sleep(0.05)
