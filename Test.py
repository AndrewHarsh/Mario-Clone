import sys, pygame, time
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
Yspeed = 0
pressedLeft = False
pressedRight = False

ballrect.x = 100
ballrect.y = 600
PressSinceGround = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

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

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    time.sleep(0.05)
