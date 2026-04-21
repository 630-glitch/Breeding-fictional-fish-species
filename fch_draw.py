import random 
import pygame
import math
import my_mod
eggs = []

def drawegg(own, screen):
    if own.col == 'red':
        color = (250, 0, 0)
    if own.col == 'black':
        color = (0, 0, 0)
    if own.col == 'white':
        color = (250, 250, 250)
    pygame.draw.circle(screen, color, (own.px, 1000), 10, 0)
    if own.status == 'dip':
        dot = (0, 0, 0)
        pygame.draw.circle(screen, dot, (own.px, 1000), 4, 0)
    if own.status == 'rot1':
        color = (0, 100, 0)
        pygame.draw.circle(screen, color, (own.px, 1000), 10, 0)
    if own.status == 'rot2':
        color = (0, 250, 0)
        pygame.draw.circle(screen, color, (own.px, 1000), 10, 0)        
def draw_fry(own, screen):
    white = (200, 200, 200)
    bace = (150, 150, 150)
    black = (0, 0, 0)     
    pygame.draw.ellipse( screen, bace, (own.px, own.py, 25, 15)) 
    if own.act[3] == 'l':
        eyex = own.px + 1
    else:
        eyex = own.px + 25
    pygame.draw.circle(screen, white, (eyex, own.py), 4, 0)
    pygame.draw.circle(screen, black, (eyex, own.py), 3, 0)    
    xpoint = own.px + 6
    ypoint = own.py + 6
    if own.act[3] == 'l':
        tx = own.px + 20
    else:
        tx = own.px - 15
    ym = own.py + 3
    pygame.draw.rect(screen, bace, (tx, ym, 20, 5))
    ex = own.px + 20
    if own.status[0] == 2:
        ey = own.py 
    else:
        ey = own.py + 10
    pygame.draw.line(screen, white, (xpoint, ypoint), (ex, ey), 1)
    xt = own.px + 40
    xtend = xt + 7
#    pygame.draw.line(screen, white, (xt, ypoint), (xtend, own.py), 1)
    bty = own.py + 40
#    pygame.draw.line(screen, white, (xt, ypoint), (xtend, bty), 1)
def _draw(own, screen):
    blue = (0, 0, 220)
    lblue = (100, 100, 220)
    pygame.draw.rect(screen, blue, (own.rect_c.x, own.rect_c.y, 30, 20))
    pygame.draw.rect(screen, lblue, (own.rect_a.x, own.rect_a.y, 60, 60))
    owncolor = (250, 250, 250)
    r = 250
    b = 250
    g = 250
    if own.ch3m[3][0] == True:
        i = own.ch3m[3][1]
        r -= 100 * i
        g -= 100 * i
    if own.ch3p[3][0] == True:
         i = own.ch3p[3][1]
         r -= 100 * i
         g -= 100 * i
    if own.ch1m[10][0] == True:
        i = own.ch1m[10][1]
        r -= 100 * i
        b -= 100 * i
        g += 10 * i
    if own.ch1m[3][0] == True:
        i = own.ch1m[3][1]
        b -= 100 * i
        g -= 100 * i
    if own.ch1p[3][0] == True:
        i = own.ch1p[3][1]
        b -= 100 * i
        g -= 100 * i
    if own.ch2m[10][0] == True:
        i = own.ch2m[10][1]
        r -= 100 * i
        b -= 100 * i
        g -= 100 * i
    if own.ch2p[10][0] == True:
        i = own.ch2p[10][1]
        r -= 100 * i
        b -= 100 * i
        g -= 100 * i  
    if r < 0:
        r = 0
    if b < 0:
        b = 0
    if g < 0:
        g = 0
    if r > 250:
        r = 250
    if g > 250:
        g = 250
    if b > 250:
        b = 250    
    if own.ch1m[6] == 'on' or own.ch1p[6] == 'on':
        owncolor = (r, g, b)
    if own.ch3m[4] == 'on' or own.ch3p[4] == 'on':
        t = 100
    else:
        t = 25 
    blue = (0, 0, 250)
#    pygame.draw.rect(screen, blue, (own.rect_b))
#    pygame.draw.ellipse( screen, owncolor, (own.px, own.py, 100, 60))
    fr = r
    fg = g
    fb = b
    if own.ch1m[8][0] == True or own.ch1p[8][0] == True:
        i = own.ch1m[8][1] + own.ch1p[8][1] - 1
        fr = 100 * i
        fg = 250 * i
        fb = 0
    if own.ch2m[3][0] == True or own.ch2p[3][0] == True:
        i = ch2m[3][1] + ch2p[3][1] - 1
        fb -= 250 * i
        fg -= 100 * i
        fr += 10 * i
    if fb < 0:
        fb = 0
    if fb > 225:
        fb = 225
    if fg < 0:
        fg = 0
    if fg > 225:
        fg = 225
    if fr > 225:
        fr = 225
    if fr < 0:
        fr = 0
    w = 240

    fcolor = (w, w, w, t)
    if own.ch1m[6] == 'on' or own.ch1p[6] == 'on':
        if own.ch1m[7] == 'on' and own.ch1p[7] == 'on':
            fcolor = (fr, fg, fb, t)
#idm        
    bwidth = 60   
    if own.z1[3] == 'on' and own.z2[3] == 'on':
        dfy = own.py - 20
        bwidth = 54
        pygame.draw.arc(screen, fcolor, [own.px, dfy, 100, 100], math.radians(45), math.radians(135),30)   
    pygame.draw.ellipse( screen, owncolor, (own.px, own.py, 100, bwidth))                
#mouth
    i = ch4m[2][1] + ch4p[2][1] - 2 
    mwdth = 10 
    mwdth += i
    if own.ch4m[2][0] == True or own.ch4p[2][0] == True:
        if own.act[3] == 'l':
            mx = own.px - 25
            my = own.py + 25           
            if own.act[0] == 'eat':
                mwdth += 10
                my -= 5
        if own.act[3] == 'r':
            mx = own.px + 90
            my = own.py + 25 
            if own.act[0] == 'eat':
                mwdth += 10
                my -= 5                  
        my -= i / 4
        pygame.draw.rect(screen, owncolor, (mx, my, 30, mwdth))
#tail
    if own.act[3] == 'l':
        tx = own.px + 90
        ty = own.py + 15
        lenth = 25
    if own.act[3] == 'r':
        tx = own.px - 12
        ty = own.py + 15
        lenth = 25
    if own.status[0] == 2:
        lenth -= lenth / 2
        if own.act[3] == 'r':
            tx += lenth / 2
    tail = False        
    if own.ch2m[1] == 'on' or own.ch2p[1] == 'on':        
        pygame.draw.rect(screen, owncolor, (tx, ty, lenth, 30))
        tail = True
    if own.ch2m[6] == 'cir' or own.ch2p[6] == 'cir':
        if own.act[3] == 'l':
            bx = tx + lenth / 2
        if own.act[3] == 'r':
            bx = tx - lenth / 2
        by = ty
        clenth = lenth + (lenth / 5)
#cirtail
        ttopx = bx + clenth
#
        ttopy = ty - 80
#
        tleftx = bx
        tlefty = by
        trightx = bx + clenth
        trighty = by + 15
        if own.act[3] == 'r':
            ttopx -= 13              
            tleftx = bx 
            tlefty = by + 15
            trightx = bx + clenth
            trighty = by            
        tpoints = [(ttopx, ttopy), (tleftx, tlefty), (trightx, trighty)]
        btopx = bx 
        btopy = ty + 30
        bleftx = bx + clenth 
        blefty = ty + 100
        brightx = bx + clenth
        brighty = ty + 15
        if own.act[3] == 'r':
            bleftx -= 100              
            btopx += 0
            bleftx += 90
        bpoints = [(btopx, btopy), (bleftx, blefty), (brightx, brighty)]
        if tail == True:
            pygame.draw.polygon(screen, fcolor, tpoints)
            pygame.draw.polygon(screen, fcolor, bpoints)
            pygame.draw.rect(screen, owncolor, (tx, ty, lenth, 30))
            pygame.draw.ellipse(screen, owncolor, (bx, by, clenth, 30))
    if own.ch2m[6] == 'tri' or own.ch2p[6] == 'tri':
        if own.ch2m[6] != 'cir' and own.ch2p[6] != 'cir':
            if own.act[3] == 'l':
                toptx = tx + lenth
                topty = ty
                botlx = toptx
                botly = ty + 30
                botrx = toptx + 10
                botry = ty + 15
            if own.act[3] == 'r':
                toptx = tx 
                topty = ty
                botlx = toptx
                botly = ty + 30
                botrx = toptx 
                botry = ty + 15
            tip = [(toptx, topty), (botlx, botly), (botrx, botry)]
            utx = toptx
            uty = topty
            ulx = botrx
            uly = botry
            urx = utx + 40 
            ury = uty - 40
            if own.act[3] == 'r':
                urx -=100
            toppoints = [(utx, uty), (ulx, uly), (urx, ury)]
            if tail == True:
                pygame.draw.polygon(screen, fcolor, toppoints)
#botom
#botrx = top
#botlx = botl
            btx = botrx
            bty = botry
            blx = btx + 50
            bly = bty + 50
            brx = botlx
            bry = botly
            if own.act[3] == 'r':
                blx -= 100                  
            botpoints = [(btx, bty), (blx, bly), (brx, bry)]
            if tail == True:
                pygame.draw.polygon(screen, fcolor, botpoints)
                pygame.draw.polygon(screen, owncolor, tip)
#draw arc
#    if own.f1[0][0] == True or own.f2[0][0] == True:
#        if own.act[3] == 'l':
#            fx = own.px + 50
#            fy = own.py - 50
#        if own.act[3] == 'r':
#            fx = own.px - 50
#            fy = own.py - 50
#polygon
#        pygame.draw.arc(screen, owncolor, [fx, fy, 100, 100], math.radians(0), math.radians(160),5)
#fin     
        if own.ch2m[2][0] == True or own.ch2p[2][0] == True:
            fi = fcolor 
            thi = 5
            if own.ch1m[9][0] == True:
                i = own.ch1m[9][1]
                thi += 2 * i
            if own.ch1p[9][0] == True:
                i = own.ch1p[9][1]
                thi += 2 * i
            if own.act[3] == 'l':
                xpoint = own.px + 30
                ypoint = own.py + 30
                enx = xpoint + 50
                eny = ypoint + 50
            if own.act[3] == 'r':
                xpoint = own.px + 60
                ypoint = own.py + 30
                enx = xpoint - 50
                eny = ypoint + 50
            if own.status[0] == 2:
                eny -= 100
            pygame.draw.line(screen, fi, (xpoint, ypoint,), (enx, eny), thi)
        if own.ch2m[4][0] == True:
            white = (250, 250, 250)
            i = own.ch2m[4][1] - 1 
            wsize = 2
            if own.ch2m[4][1] > 0:
                wsize = 10 + i
            if own.act[3] == 'l':
                ex = own.px + 10
                ey = own.py + 10
            if own.act[3] == 'r':
                ex = own.px + 90
                ey = own.py + 10
            pygame.draw.circle( screen, white, (ex, ey,), wsize, 0)
            if own.ch2p[4][0] == True:
                bl = (250, 10, 20)             
                i = own.ch2p[4][1] - 1
                bsize = 1
                if own.ch1m[7] == 'on' or own.ch1p[7] == 'on':
                    if own.ch2p[4][1] > 0:
                        bsize = 5 + i
                if bsize > wsize:
                    bsize = wsize
                if own.ch1m[6] == 'on' or own.ch1p[6] == 'on':
                    if own.ch1m[4] == 'on' or own.ch1p[4] == 'on':
                        bl = (0, 0, 0)
                    else:
                        bl = (0, 125, 0)
                blx = ex
                bly = ey
                pygame.draw.circle(screen, bl, (blx, bly,), bsize, 0)
            line = (0, 0, 0)
            if own.z2[1] == 'i':
                line = (250, 0, 0)
            pygame.draw.line(screen, line, (0, own.py), (1000, own.py), 1)
            pygame.draw.line(screen, line, (own.px, 0), (own.px, 1000), 1)
            line2 = (0, 225, 0)
            end = own.py + 25
            pygame.draw.line(screen, line2, (own.px, own.py), (own.px , end))
            if own.status[7] < 0:
                red = (220, 0, 0)
                iy = own.py + 30
                injsize = 10
                if own.status[7] < -10:
                    injsize = 20
                pygame.draw.circle(screen, red, (own.px, iy), injsize, 0)                               
def drawd(own, screen):
    red = (250, 0, 0)
    dgreen = (0, 50, 0)
    blue = (0, 0, 10)
    yel = (50, 50, 0)
    pur = (100, 0, 100)
    br = (100, 50, 50)
    pygame.draw.circle(screen, red, (own.px, 20), 20, 0)     
    if 'inj' in own.c:
        pygame.draw.circle(screen, red, (own.px, 200), 20, 0)
    if 'enout' in own.c:
        pygame.draw.circle(screen, dgreen, (own.px, 300), 20, 0)
    if 'LO' in own.c:
        pygame.draw.circle(screen, blue, (own.px, 400), 20, 0)
    if 'LP' in own.c:
        pygame.draw.circle(screen, yel, (own.px, 1000), 20, 0)
    if 'OE' in own.c:
        pygame.draw.circle(screen, br, (own.px, 600), 20, 0)
    tx = own.px + 40
    if 'in' in own.c:
        pygame.draw.circle(screen, red, (tx, 600), 20, 0)
def rdraw(own, screen):
    green = (0, 250, 0)
    pygame.draw.circle(screen, green, (own.px, 20), 20, 0)

en = []
binds = []
ad = []

import pygame
import math
class an:
  def __init__(self, px, py, dir, act, status, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, col1, col2, f1, f2, m1, m2, z1, z2, likes, Attributes=None):
    self.px = px
    self.py = py
    self.dir = dir
    self.act = act
    self.status = status 
    self.ch1m = ch1m
    self.ch1p = ch1p    
    self.ch2m = ch2m
    self.ch3m = ch3m
    self.ch3p = ch3p
    self.ch4m = ch4m
    self.ch4p = ch4p
    self.ch2p = ch2p
    self.col1 = col1
    self.col2 = col2
    self.f1 = f1
    self.f2 = f2
    self.m1 = m1
    self.m2 = m2
    self.z1 = z1
    self.z2 = z2
    self.likes = likes
    self.rect_a = pygame.Rect(px, py, 60, 60)
    self.rect_c = pygame.Rect(px, py, 30, 20)
  def drawfry(self, screen):
      draw_fry(self, screen)
  def shapedraw(self, screen):
      _draw(self, screen)    
#make
g = [True, 1]
m = [True, 2]
n = [True, 0]
px = 200
py = 500      
dir = 'l'
act = ['l', 'l', 'l', 'r']
status = [1, 4, 40, 2, 5, 5, 5, 5, 5, 5]
ch1m = [1, True, True, g, 'on', 'on', 'on', 'on', g, g, g]
ch1p = [1, True, True, g, 'on', 'on', 'on', 'on', g, g, g]
ch2m = [1, 'on', g, g, g, g, 'cir']
ch2p = [1, 'on', g, g, n, g, 'tri']
ch3m = [1, 'on', g, g, 'on']
ch3p = [1, 'on', g, g, 'on']
ch4m = [1, 't', g]
ch4p = [1, 't', g]
col1 = [[True, 1, True]]
col1 = [g, g, g, g, g, g, 'on']
col2 = [g, g, g, g, g, g, 'on']
f1 = [g, g, g, 'ir', 'o']
f2 = [g, g, g, 'ti', 'n']
m1 = [g, 'on', g, 'on', 'on', 'on']
m2 = [g, 'on', g, 'on', 'n', 'on']
z1 = ['on', 'on', 'on', 'on']
z2 = ['on', 'on', 'on', 'on']
likes = [0, 0, 0, 0]
en.append(an(px, py, dir, act, status, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, col1, col2, f1, f2, m1, m2, z1, z2, likes))
# second 
class Egg:
    def __init__(self, col, px, stage):
        self.col = col
        self.px = px
        self.status = status 
    def draw(self, screen):
        drawegg(self, screen)
col = 'red'
px = 100
status = 'rot2'
eggs.append(Egg(col, px, status))

#pygame.init()
#screen_width = 1000
#screen_hight = 1000
#screen = pygame.display.set_mode((screen_width, screen_hight), 0, 32)
#tp = pygame.Surface((screen_width, screen_hight), pygame.SRCALPHA)
#black = (0, 0, 0)
#white = (255, 255, 255)
#blue = (100, 150, 200)
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    # Fill the screen with a background color (e.g., black)
#    screen.fill(blue)
#    for obj in eggs:
#        obj.draw(screen)
#    for obj in en:
#        obj.drawfry(screen)
#        obj.shapedraw(screen)
#    screen.blit(tp, (0, 0)) 
#    pygame.display.flip()        