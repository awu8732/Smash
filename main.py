import pygame
import time
import random
from Platform import Platform
from Player import Player

pygame.init()

win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("SSB Ripoff")
t = pygame.time.get_ticks()

bg = pygame.image.load('Pictures/bg1.jpg')
arrow = pygame.image.load('Pictures/link/bow/arrow.png')
avatar = pygame.image.load('Pictures/link/charPicture.png')

user = Player(250,0,5)
platforms = [Platform(125, 425, 750, 50), Platform(175,325, 200, 20), Platform(500, 200, 200, 20)] #1st el is main
game = True
tdelta = 0
beganJumping = 0
beganSpin = 0
beganJumpAttack = 0

def drawGameWindow():
    win.blit(bg, (-100,-50))
    user.draw(win)
    #win.blit(arrow, (200, 200))
    user.useBow(win)
    for plat in platforms:
        plat.draw(win)
    #pygame.draw.rect(win, (0,0,0), (125,450,750,100))
    #
    #win.blit(avatar, (100, 300))
    pygame.display.update()

while game:
    pygame.time.delay(45)
    user.protect = False
    user.isWalking = False
    user.isSprinting = False
    user.bowBack = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        user.protect = True
    elif keys[pygame.K_o] and not user.protect:
        user.attack = True

    if keys[pygame.K_UP] and keys[pygame.K_p] and user.y - user.jumpVel > 0 and not user.protect:
        if time.time()-beganSpin > 2.5:
            beganSpin = time.time()
            user.spin = True

    if keys[pygame.K_UP] and keys[pygame.K_o] and user.y - user.jumpVel > 0 and not user.protect:
        if time.time()-beganJumpAttack > 1:
            beganJumpAttack = time.time()
            user.jumpAt = True
    if keys[pygame.K_p] and not user.spin:
        user.bowBack = True

    if keys[pygame.K_RIGHT] and user.x + user.vel < 955 and not user.protect and not user.attack and not user.bowBack:
        if keys[pygame.K_i]:
            user.sprintRight()
        else:
            user.walkRight()
    elif keys[pygame.K_LEFT] and user.x - user.vel > -5 and not user. protect and not user.attack and not user.bowBack:
        if keys[pygame.K_i]:
            user.sprintLeft()
        else:
            user.walkLeft()

    if keys[pygame.K_UP] and user.y - user.jumpVel > 0 and not user.protect:
        if (time.time() - beganJumping > 1):
            beganJumping = time.time()
            user.isJumping = True
            user.isFalling = False
            #user.y-=user.jump

    user.jump()
    user.thrust()
    user.spinAttack()
    user.jumpAttack()
    #user.useBow(win)

    for plat in platforms:
        if plat.inBounds(user.x, user.y + tdelta+80) == False:
            if user.isJumping == False:

                if (user.isFalling==False):
                    beganFalling = time.time()
                    user.isFalling = True
                tdelta = time.time() - beganFalling

                user.y+=9.81 * (tdelta)
        else:
            while(plat.inBounds(user.x, user.y+tdelta + 70) == False and user.isJumping == False):
                user.y+=1
            while (plat.inBounds(user.x, user.y + tdelta + 65) == True and user.isJumping == False):
                user.y -= 1
            user.isFalling = False
            break

    drawGameWindow()

    if user.isWalking == False:
        user.walkCount = 0
    if user.attackCount == 5:
        user.attackCount = 0
        user.attack = False
        user.v = random.randint(1, 2)
    if user.spinCount == 11:
        user.spinCount = 0
        user.spin = False
    if user.jumpCount == 6:
        user.jumpCount = 0
        user.jumpAt = False
    if user.bowState == 10:
        user.bowState = 0
        user.bowPower = 0



pygame.quit()