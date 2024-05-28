import pygame
import random
import time
from Projectile import Projectile

idleLeft = pygame.image.load('Pictures/link/linkLeft.png')
idleRight = pygame.image.load('Pictures/link/linkRight.png')
arrow = pygame.image.load('Pictures/link/bow/arrow.png')
#walk
linkUp = [pygame.image.load('Pictures/link/linkUpL.png'), pygame.image.load('Pictures/link/linkUpR.png')]
linkDown = [pygame.image.load('Pictures/link/linkDownL.png'), pygame.image.load('Pictures/link/linkDownR.png')]
linkLeft = [pygame.image.load('Pictures/link/linkL1.png'), pygame.image.load('Pictures/link/linkL2.png'),
            pygame.image.load('Pictures/link/linkL3.png'), pygame.image.load('Pictures/link/linkL4.png')]
linkRight = [pygame.image.load('Pictures/link/linkR1.png'), pygame.image.load('Pictures/link/linkR2.png'),
            pygame.image.load('Pictures/link/linkR3.png'), pygame.image.load('Pictures/link/linkR4.png')]
#sprint
linkLeftS = [pygame.image.load('Pictures/link/sprint/sprint1L.png'), pygame.image.load('Pictures/link/sprint/sprint2L.png'),
            pygame.image.load('Pictures/link/sprint/sprint3L.png'), pygame.image.load('Pictures/link/sprint/sprint4L.png')]
linkRightS = [pygame.image.load('Pictures/link/sprint/sprint1R.png'), pygame.image.load('Pictures/link/sprint/sprint2R.png'),
            pygame.image.load('Pictures/link/sprint/sprint3R.png'), pygame.image.load('Pictures/link/sprint/sprint4R.png')]
#protect
linkProtect = [pygame.image.load('Pictures/link/protect.png'), pygame.image.load('Pictures/link/protect2.png')]
#thrust
linkThrust = [[pygame.image.load('Pictures/link/linkThrustL1.png'), pygame.image.load('Pictures/link/linkThrustL1.png'), pygame.image.load('Pictures/link/linkThrustL2.png'),
               pygame.image.load('Pictures/link/linkThrustL2.png'), pygame.image.load('Pictures/link/linkThrustL3.png'), pygame.image.load('Pictures/link/linkThrustL3.png')],
              [pygame.image.load('Pictures/link/linkThrustR1.png'), pygame.image.load('Pictures/link/linkThrustR1.png'), pygame.image.load('Pictures/link/linkThrustR2.png'),
               pygame.image.load('Pictures/link/linkThrustR2.png'), pygame.image.load('Pictures/link/linkThrustR3.png'), pygame.image.load('Pictures/link/linkThrustR3.png')]]
#attack
linkAttack = [[pygame.image.load('Pictures/link/linkAttackL1.png'), pygame.image.load('Pictures/link/linkAttackL1.png'), pygame.image.load('Pictures/link/linkAttackL2.png'),
               pygame.image.load('Pictures/link/linkAttackL2.png'), pygame.image.load('Pictures/link/linkAttackL3.png'), pygame.image.load('Pictures/link/linkAttackL3.png')],
              [pygame.image.load('Pictures/link/linkAttackR1.png'), pygame.image.load('Pictures/link/linkAttackR1.png'), pygame.image.load('Pictures/link/linkAttackR2.png'),
               pygame.image.load('Pictures/link/linkAttackR2.png'), pygame.image.load('Pictures/link/linkAttackR3.png'), pygame.image.load('Pictures/link/linkAttackR3.png')]]
#spin attack
linkSP = [pygame.image.load('Pictures/link/spinAttack/sp1.png'), pygame.image.load('Pictures/link/spinAttack/sp2.png'),
          pygame.image.load('Pictures/link/spinAttack/sp3.png'), pygame.image.load('Pictures/link/spinAttack/sp4.png'),
          pygame.image.load('Pictures/link/spinAttack/sp1.png'), pygame.image.load('Pictures/link/spinAttack/sp2.png'),
          pygame.image.load('Pictures/link/spinAttack/sp3.png'), pygame.image.load('Pictures/link/spinAttack/sp4.png'),
          pygame.image.load('Pictures/link/spinAttack/sp1.png'), pygame.image.load('Pictures/link/spinAttack/sp2.png'),
          pygame.image.load('Pictures/link/spinAttack/sp3.png'), pygame.image.load('Pictures/link/spinAttack/sp4.png')
          ]
#jump attack
linkJA = [[pygame.image.load('Pictures/link/jumpAttack/linkJAL1.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAL2.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAL3.png'),
           pygame.image.load('Pictures/link/jumpAttack/linkJAL4.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAL5.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAL6.png'),
           pygame.image.load('Pictures/link/jumpAttack/linkJAL7.png')],
          [pygame.image.load('Pictures/link/jumpAttack/linkJAR1.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAR2.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAR3.png'),
           pygame.image.load('Pictures/link/jumpAttack/linkJAR4.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAR5.png'), pygame.image.load('Pictures/link/jumpAttack/linkJAR6.png'),
           pygame.image.load('Pictures/link/jumpAttack/linkJAR7.png')]]
#bow
linkBow = [[pygame.image.load('Pictures/link/bow/bow1L.png'), pygame.image.load('Pictures/link/bow/bow1L.png'),
            pygame.image.load('Pictures/link/bow/bow2L.png'), pygame.image.load('Pictures/link/bow/bow2L.png'),
            pygame.image.load('Pictures/link/bow/bow2L.png'), pygame.image.load('Pictures/link/bow/bow3L.png'),
            pygame.image.load('Pictures/link/bow/bow5L.png'), pygame.image.load('Pictures/link/bow/bow5L.png'),
            pygame.image.load('Pictures/link/bow/bow5L.png'), pygame.image.load('Pictures/link/bow/bow5L.png'),
            pygame.image.load('Pictures/link/bow/bow5L.png'), pygame.image.load('Pictures/link/bow/bow5L.png')
            ],
           [pygame.image.load('Pictures/link/bow/bow1R.png'), pygame.image.load('Pictures/link/bow/bow1R.png'),
            pygame.image.load('Pictures/link/bow/bow2R.png'), pygame.image.load('Pictures/link/bow/bow2R.png'),
            pygame.image.load('Pictures/link/bow/bow3R.png'), pygame.image.load('Pictures/link/bow/bow3R.png'),
            pygame.image.load('Pictures/link/bow/bow5R.png'), pygame.image.load('Pictures/link/bow/bow5R.png'),
            pygame.image.load('Pictures/link/bow/bow5R.png'), pygame.image.load('Pictures/link/bow/bow5R.png'),
            pygame.image.load('Pictures/link/bow/bow5R.png'), pygame.image.load('Pictures/link/bow/bow5R.png')
           ]]
linkArrow = Projectile(50, arrow)

class Player:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        #vel
        self.v = random.randint(1,2)
        self.vel = vel
        self.jumpVel = 17
        #bow
        self.arrowCreated = False
        self.bowPower = 0
        self.bowState = 0
        self.bowBack = False
        #walking
        self.orientation = 1
        self.walkCount = 0
        self.attackCount = 0
        self.spinCount = 0
        self.jumpCount = 0
        #states
        self.isStanding = False
        self.isFalling = False
        self.isJumping = False
        self.isWalking = False
        self.isSprinting = False
        self.lastJump = 0
        self.doubleJump = False
        self.jumpAt = False
        self.protect = False
        self.attack = False
        self.spin = False
        #damaged
        self.damagePercent = 0

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getVel(self):
        return self.vel
    def draw(self, win):
        state = linkRight[0]
        if self.bowBack or self.bowPower>0:
            if self.orientation == -1:
                state = linkBow[0][self.bowState]
            else:
                state = linkBow[1][self.bowState]
        elif self.spin:
            state = linkSP[self.spinCount]
        elif self.jumpAt and self.orientation==-1:
            state = linkJA[0][self.jumpCount]
            self.x += 10 * self.orientation
        elif self.jumpAt and self.orientation==1:
            state = linkJA[1][self.jumpCount]
        elif self.orientation == -1:
            if self.protect:
                state = linkProtect[0]
            elif self.isJumping:
                state = linkUp[0]
            elif self.isFalling:
                state = linkDown[0]
            elif self.attack:
                if self.v==1:
                    state = linkThrust[0][self.attackCount]
                else:
                    state = linkAttack[0][self.attackCount]
            elif self.isSprinting:
                if self.walkCount % 2 == 1:
                    state = linkLeftS[int((self.walkCount-1)/2)]
                else:
                    state = linkLeftS[int((self.walkCount/2))]
            elif self.isWalking:
                if self.walkCount % 2 == 1:
                    state = linkLeft[int((self.walkCount-1)/2)]
                else:
                    state = linkLeft[int((self.walkCount/2))]
            else:
                state = idleLeft
        else:
            if self.protect:
                state = linkProtect[1]
            elif self.isFalling:
                state = linkDown[1]
            elif self.isJumping:
                state = linkUp[1]
            elif self.attack:
                if self.v == 1:
                    state = linkThrust[1][self.attackCount]
                else:
                    state = linkAttack[1][self.attackCount]
            elif self.isSprinting:
                if self.walkCount % 2 == 1:
                    state = linkRightS[int((self.walkCount-1)/2)]
                else:
                    state = linkRightS[int((self.walkCount/2))]
            elif self.isWalking:
                if self.walkCount % 2 == 1:
                    state = linkRight[int((self.walkCount-1)/2)]
                else:
                    state = linkRight[int(self.walkCount/2)]
            else:
                state = idleRight
        win.blit(state, (self.x, self.y))
    def jump(self):
        if (self.isJumping == True):
            self.y -= self.jumpVel
            self.jumpVel -= 1
        if self.jumpVel <= 0:
            self.isJumping = False
            self.jumpVel = 17
    def walkLeft(self):
        self.isWalking = True
        self.x -= self.vel
        self.orientation = -1
        self.walkCount = (self.walkCount + 1) % 8
    def walkRight(self):
        self.isWalking = True
        self.x += self.vel
        self.orientation = 1
        self.walkCount = (self.walkCount + 1) % 8
    def sprintLeft(self):
        self.isWalking = True
        self.isSprinting = True
        self.x -= self.vel*2.5
        self.orientation = -1
        self.walkCount = (self.walkCount + 1) % 8
    def sprintRight(self):
        self.isWalking = True
        self.isSprinting = True
        self.x += self.vel*2.5
        self.orientation = 1
        self.walkCount = (self.walkCount + 1) % 8
    def thrust(self):
        if self.attack:
            self.attackCount = (self.attackCount+1)
            #self.x += 5 * self.orientation
    def spinAttack(self):
        if self.spin:
            self.spinCount+=1
            self.y -= 5
    def jumpAttack(self):
        if self.jumpAt:
            self.jumpCount+=1
            self.x += 5 * self.orientation
    def useBow(self, win):
        if self.bowBack:
            if self.bowPower <= 40:
                self.bowPower+=10
                self.bowState+=1
                self.arrowCreated = False
                linkArrow.x = self.x + 15
                linkArrow.y = self.y + 15
        elif self.bowPower>0:
            if not self.arrowCreated:
                self.arrowCreated = True
                linkArrow.vel = self.bowPower*1.5
            #release
            self.bowState+=1
            self.bowPower-=16

        if self.arrowCreated:
            if linkArrow.vel > 30:
                linkArrow.draw(win, linkArrow.x, linkArrow.y)
                linkArrow.x += linkArrow.vel * self.orientation
                linkArrow.vel-=3
