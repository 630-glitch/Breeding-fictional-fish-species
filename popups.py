en = []
binds = []
ad = []
ed = []
mi = []
hardness = 15
oxy = 100
import f_draw
import random 
import pygame
import math
import my_mod


time = 10
draged = None
picked = None
status = 'gen'
popup = None
rect1 = pygame.Rect(100, 1, 50, 50)
rect2 = pygame.Rect(500, 1, 50, 50)
back = pygame.Rect(20, 220, 50, 50)
m1rect = pygame.Rect(20, 280, 50, 50)
m2rect = pygame.Rect(20, 340, 50, 50)
m3rect = pygame.Rect(20, 400, 50, 50)
m4rect = pygame.Rect(20, 460, 50, 50)
m5rect = pygame.Rect(20, 520, 50, 50)
pygame.init()
screen_width = 1000
screen_hight = 1000
screen = pygame.display.set_mode((screen_width, screen_hight), 0, 32)
tp = pygame.Surface((screen_width, screen_hight), pygame.SRCALPHA)
black = (0, 0, 0)
white = (225, 225, 225)
blue = (100, 150, 200)
orange = (100, 0, 100)
red = (250, 0, 0)
mes = pygame.font.SysFont(None, 48) 
current_message = "none"
def block(back):
    pygame.draw.rect(screen, white, (20, 200, 790, 800))
    mes1 = mes.render(f"back", True, (0, 0, 0))
    me1_rect = mes1.get_rect(center=(110, 240))
    screen.blit(mes1, me1_rect)
    pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
def main(back, m1rect, m2rect, m3rect):
    block(back)
    message1 = mes.render(f'tanks', True, (0, 0, 0))
    mx1 = m1rect.x + 60
    me1rect = (mx1, m1rect.y)
    screen.blit(message1, me1rect)
    message2 = mes.render(f'shop', True, (0, 0, 0))
    me2rect = (mx1, m2rect.y)
    screen.blit(message2, me2rect)
    message1 = mes.render(f'', True, (0, 0, 0))
    me3rect = (m3rect.x, m3rect.y)
    screen.blit(message1, me3rect)        
    pygame.draw.rect(screen, red, (m1rect.x, m1rect.y, 50, 50))        
    pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m3rect.x, m3rect.y, 50, 50))    
def fishmain(back, m1rect, m2rect, m4rect, m5rect):
    block(back)
    mes2 = mes.render(f"1", True, (0, 0, 0))
    me2_rect = mes2.get_rect(center=(90, 300))
    screen.blit(mes2, me2_rect)
    pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
    pygame.draw.rect(screen, red, (m1rect.x, m1rect.y, 50, 50))        
    pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m3rect.x, m3rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m4rect.x, m4rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))
def m1(back, message):
    block(back)
    message = mes.render(f"{message}", True, (0, 0, 0))
    me_rect = message.get_rect(center=(100, 300))
    screen.blit(message, me_rect)     
def m2(back, m5rect, message):
    block(back)
    message = mes.render(f"{message}", True, (0, 0, 0))
    me_rect = message.get_rect(center=(100, 300))
    screen.blit(message, me_rect)           
    pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))    
def m3(back, m2rect, m5rect):
    block(back)
    message = mes.render(f"mesage3", True, (0, 0, 0))
    me_rect = message.get_rect(center=(100, 300))
    screen.blit(message, me_rect)       
    pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))         
def m4(back, m2rect, m5rect):
    block(back)
    message = mes.render(f"sell for:", True, (0, 0, 0))
    me_rect = message.get_rect(center=(140, 360))
    screen.blit(message, me_rect)  
    message = mes.render(f"cull", True, (0, 0, 0))
    me_rect = message.get_rect(center=(140, 540))
    screen.blit(message, me_rect)         
    pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
    pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))          
def current_mes(current_message):
    block(back)
    message = mes.render(f"{current_message}", True, (0, 0, 0))
    me_rect = message.get_rect(center=(100, 300))
    screen.blit(message, (100, 300))       
def tankshow(back, i1, i2, i3):
    block(back)
    if i1 != None:
        pygame.draw.rect(screen, red, (m1rect.x, m1rect.y, 50, 50))
        message1 = mes.render(f'tank1', True, (0, 0, 0))
        mx1 = m1rect.x + 60
        me1rect = (mx1, m1rect.y)
        screen.blit(message1, me1rect)        
    if i2 != None:         
        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
        message2 = mes.render(f'tank2', True, (0, 0, 0))
        mx2 = m2rect.x + 60
        me2rect = (mx2, m2rect.y)
        screen.blit(message2, me2rect)                
    if i3 != None:
        pygame.draw.rect(screen, red, (m3rect.x, m3rect.y, 50, 50))        
        message1 = mes.render(f'tank3', True, (0, 0, 0))
        mx3 = m1rect.x + 60
        me3rect = (mx3, m3rect.y)
        screen.blit(message3, me3rect)                
       
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
# #    Fill the screen with a background color (e.g., black)
#    screen.fill(blue)
#    red = (200, 0, 0)
#    white = (200, 200, 200)
#    tankshow(back, None, None, None)
#    main(back, m1rect, m2rect, m3rect)
#    m1(back, 'message1')
#    m3(back, m2rect, m5rect)
#    m4(back, m2rect, m5rect)
#    current_mes('this message ')
#    fishmain(back, m1rect, m2rect, m3rect, m4rect,)
#    if popup == 'fishmain':
#        pygame.draw.rect(screen, white, (20, 200, 790, 800))
#        mes1 = mes.render(f"back", True, (0, 0, 0))
#        me1_rect = mes1.get_rect(center=(110, 240))
#        screen.blit(mes1, me1_rect)
#        mes2 = mes.render(f"1", True, (0, 0, 0))
#        me2_rect = mes2.get_rect(center=(90, 300))
#        screen.blit(mes2, me2_rect)
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        pygame.draw.rect(screen, red, (m1rect.x, m1rect.y, 50, 50))        
#        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m3rect.x, m3rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m4rect.x, m4rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))
#    if popup == '1':
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"mesage1", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)     
#    if popup == '2':
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))        
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"mesage2", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)           
#        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))   
#    if popup == '3':        
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))        
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"mesage3", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)       
#        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))                       
#    if popup == '4':
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))        
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"mesage4", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)     
#        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))          
#    if popup  == 'currentmessage':
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))        
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"{current_message}", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)       
#    if popup == 'df':
#        pygame.draw.rect(screen, white, (20, 200, 800, 800))
#        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
#        bacm = mes.render(f"back", True, (0, 0, 0))        
#        bacrect = bacm.get_rect(center=(100, 250))
#        screen.blit(bacm, bacrect)
#        message = mes.render(f"mesage3", True, (0, 0, 0))
#        me_rect = message.get_rect(center=(100, 300))
#        screen.blit(message, me_rect)       
#        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
#        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))                                      
#    screen.blit(tp, (0, 0)) 
#    pygame.display.flip()