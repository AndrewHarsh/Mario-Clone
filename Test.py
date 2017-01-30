import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

<<<<<<< HEAD
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
Yspeed = 0
pressedLeft = False
pressedRight = False

ballrect.x = 100
ballrect.y = 600
=======
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

p1Yspeed = 0
p2Yspeed = 0

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
platrect1.y = 150

platrect2.x = 820
platrect2.y = 250

platrect3.x = 380
platrect3.y = 420

>>>>>>> 579999076a621e9a1cc3e766cabfe61ec3c8db65
PressSinceGround = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
<<<<<<< HEAD

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if PressSinceGround < 2:
                    Yspeed = -30
                PressSinceGround += 1
#            if event.key == pygame.K_DOWN:
#                ballrect = ballrect.move(0, 20) 
            elif event.key == pygame.K_LEFT:
                pressedLeft = True
            elif event.key == pygame.K_RIGHT:
                pressedRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressedLeft = False
            elif event.key == pygame.K_RIGHT:
                pressedRight = False


    #movement
    if pressedLeft == True:
        ballrect.x -= 20
    elif pressedRight == True:
        ballrect.x += 20
    
        


    ballrect = ballrect.move(0, Yspeed)

    if ballrect.y < 600:
        Yspeed += 2
    elif ballrect.y > 600:
        ballrect.y = 600
        Yspeed = 0
        PressSinceGround = 0

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]
=======
        if event.type == pygame.KEYDOWN:
            #Player1
            if event.key == pygame.K_w:
                if PressSinceGround < 2:
                    p1Yspeed = -35
                PressSinceGround += 1
            elif event.key == pygame.K_a:
                pressedLeft = True
                player1 = pygame.image.load("mario_sprite_left.png")
            elif event.key == pygame.K_d:
                pressedRight = True
                player1 = pygame.image.load("mario_sprite.png")
            elif event.key == pygame.K_LSHIFT:
                pressedLBoost = True
                
            #Player2
            if event.key == pygame.K_UP:
                if PressSinceGround < 2:
                    p2Yspeed = -35
                PressSinceGround += 1
            elif event.key == pygame.K_LEFT:
                pressedLeftArrow = True
                player2 = pygame.image.load("luigi_sprite_left.png")
            elif event.key == pygame.K_RIGHT:
                pressedRightArrow = True
                player2 = pygame.image.load("luigi_sprite.png")
            elif event.key == pygame.K_RSHIFT:
                pressedRBoost = True
                
        elif event.type == pygame.KEYUP:
            #Player1
            if event.key == pygame.K_a:
                pressedLeft = False
            elif event.key == pygame.K_d:
                pressedRight = False
            elif event.key == pygame.K_LSHIFT:
                pressedLBoost = False
                
            #Player2
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
    #player1
    if pressedLeft == True:
        p1rect.x -= 20
        if pressedLBoost == True:
            p1rect.x -= 30
    elif pressedRight == True:
        p1rect.x += 20
        if pressedLBoost == True:
            p1rect.x += 30
    #player2    
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
    if p1rect.x > platrect1.x - 40 and p1rect.x + p1rect.w < platrect1.x + (platrect1.w + 40) and p1rect.y < 150 and p1rect.y > 150-p1rect.h:
        p1rect.y = 150 - p1rect.h
        p1Yspeed = 0
        PressSinceGround = 0
    if p1rect.x > platrect2.x - 40 and p1rect.x + p1rect.w < platrect2.x + (platrect2.w + 40)  and p1rect.y < 250 and p1rect.y > 250-p1rect.h:
        p1rect.y = 250 - p1rect.h
        p1Yspeed = 0
        PressSinceGround = 0
    if p1rect.x > platrect3.x - 40 and p1rect.x + p1rect.w < platrect3.x + (platrect3.w + 40)  and p1rect.y < 420 and p1rect.y > 420-p1rect.h:
        p1rect.y = 420 - p1rect.h
        p1Yspeed = 0
        PressSinceGround = 0
    else:
        p1Yspeed +=2
        
    #Player 2
    if p2rect.x > platrect1.x - 20 and p2rect.x + p2rect.w < platrect1.x + (platrect1.w + 40) and p2rect.y < 150 and p2rect.y > 150-p2rect.h:
        p2rect.y = 150 - p2rect.h
        p2Yspeed = 0
        PressSinceGround = 0
    if p2rect.x > platrect2.x - 20 and p2rect.x + p2rect.w < platrect2.x + (platrect2.w + 40)  and p2rect.y < 250 and p2rect.y > 250-p2rect.h:
        p2rect.y = 250 - p2rect.h
        p2Yspeed = 0
        PressSinceGround = 0
    if p2rect.x > platrect3.x - 20 and p2rect.x + p2rect.w < platrect3.x + (platrect3.w + 40)  and p2rect.y < 420 and p2rect.y > 420-p2rect.h:
        p2rect.y = 420 - p2rect.h
        p2Yspeed = 0
        PressSinceGround = 0
    else:
        p2Yspeed +=2
        
    p1rect = p1rect.move(0, p1Yspeed)
    p2rect = p2rect.move(0, p2Yspeed)

    if p1rect.y > 600:
        p1rect.y = 600
        p1Yspeed = 0
        PressSinceGround = 0
    elif p1rect.y < 0:
        p1Yspeed += 2
        
    if p2rect.y > 600:
        p2rect.y = 600
        p2Yspeed = 0
        PressSinceGround = 0
    elif p2rect.y < 0:
        p2Yspeed += 2

    
    
>>>>>>> 579999076a621e9a1cc3e766cabfe61ec3c8db65

    screen.fill(black)
    screen.blit(player1, p1rect)
    screen.blit(player2, p2rect)
    screen.blit(ground, groundrect)
    screen.blit(platform1, platrect1)
    screen.blit(platform2, platrect2)
    screen.blit(platform3, platrect3)
    pygame.display.flip()

    time.sleep(0.05)
