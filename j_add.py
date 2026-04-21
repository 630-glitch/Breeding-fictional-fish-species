en = []
binds = []
ad = []
ed = []
eggs = []
small = []
mi = []
tanks = []
next_id = 2
ids = {}
hardness = 15
oxy = 100
import f_draw
import fch_draw
import f_int
import random 
import pygame
import math
import my_mod
import j_int
import popups
import json
import os
data = "traits5.json"
with open (data, "w") as file:
    json.dump([] , file)
def updateid():
    global next_id
    next_id += 1
def eggcol(obj, ec):
    with open(data, 'r') as file:
        es = json.load(file)
    modified  = False    
    for e in es:
        if e.get("datatype") == "adult" and e.get("id") == str(obj.id):
            e["eggcolor"] = ec
            with open(data, "w") as file:
                json.dump(es, file, indent=4)       
def addoff(obj, off):
    with open(data, 'r') as file:
        es = json.load(file)
    for e in es:
        if e.get("datatype") == "adult" and e.get("id") == str(obj.id):
            if "offspring" not in e:
                e["offspring"] = []
            e["offspring"].append(off)
            with open(data, "w") as file:
                json.dump(es, file, indent=4)
            break 
def adata(obj):
    ats = j_int.reg(obj)
    new = {"datatype" : "adult", "id" : str(obj.id), 'mf' : str(ats[9]), 'collor' : str(ats[0]), 'fincollor' : str(ats[1]), 'beak' : str(ats[2]), 'tail' : str(ats[3]) , 'tailend' : str(ats[4]), 'fin' : str(ats[5]), 'eyesizse' : str(ats[6]), 'pupilsize' : str(ats[7]), 'pupilcolor' : str(ats[8])}
    if os.path.exists(data) and os.path.getsize(data) > 0:
        with open(data, "r") as this:
            obs = json.load(this)
    else:
        obs = []
    obs.append(new)
    with open(data, "w") as this:
        json.dump(obs, this, indent=4)
        
def iseyes(own):
    eyes = False
    if own.ch2m[4][0] == True and own.ch2p[4][0] == True:
        if own.ch2m[4][1] > 0 and own.ch2p[4][1] > 0:
            if own.ch1m[7] == 'on' or own.ch1p[7] == 'on':
                eyes = True
                return eyes
def cleanup(fish):
    for b in mi:
        if b.h == fish.id:
            mi.remove(b)
def tanksget(men, back):
    try:
        i1 = tanks[0]
    except IndexError:
        i1 = None
    try:
        i2 = tanks[1]
    except IndexError:
        i2 = None
    try:
        i3 = tanks[2]
    except IndexError:
        i3 = None
    popups.tankshow(back, i1, i2, i3)
def nec(fish):
    cause = fish.c
    return cause 
def health_check(fish):
    if fish.status[7] < 1:
        health = "injured"
    else:
        health = "healthy"
    for obj in mi:
        if obj.h == fish.id:
            inf = obj.type
    hardmin = fish.status[8]
    harmax = fish.status[9]
    return health 
class tank:
    def __init__(self, name, type, hardness, oxy):
        self.name = name
        self.type = type
        self.hardness = hardness 
        self.oxy = oxy

class fry:
    def __init__(self, tank, id, px, py, time, act, status, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2, likes, attributes=None):
        self.tank = tank
        self.id = id
        self.px = px
        self.py = py
        self.time = time
        self.act = act
        self.status = status 
        self.mt = mt
        self.ch1m = ch1m
        self.ch1p = ch1p
        self.ch2m = ch2m
        self.ch2p = ch2p
        self.ch3m = ch3m
        self.ch3p = ch3p
        self.ch4m = ch4m
        self.ch4p = ch4p
        self.z1 = z1
        self.z2 = z2
        self.likes = likes
        self.rect = pygame.Rect(self.px, self.py, 100, 100)
    def adult(self):
        mem = [0, '0', '0']
        act = ['down', '', 5, 'l', 'r']
        e = f_int.iseyes(self)
        fin = f_int.isfin(self)
        status = [2, 4, 10, 0, 50, 40, 1, 1, 10, 40, 10, e, fin]
        likes = likes = [0, 0, 10, 10, 10, 0, 10, 10, 10, -6]
        en.append(an(self.tank, self.id, self.px, self.py, mem, act, status, self.mt, self.ch1m, self.ch1p, self.ch2m, self.ch2p, self.ch3m, self.ch3p, self.ch4m, self.ch4p, self.z1, self.z2, likes))
        adata(self)
        small.remove(self)
    def grow(self):
        if self.time > 0:
            self.time -= 1
        else:
            self.adult()
    def draw(self):
        fch_draw.draw_fry(self, screen)
    def dirflip(self):
        if self.act[3] == 'l':
            self.act[3] = 'r'
        else:
            self.act[3] = 'l'
    def move(self):
        if self.likes[1] > 3:
            opt = ['df', 'nf']
            if self.likes[1] == 4:
                weights = [1, 20]
            if self.likes[1] > 4 and self.likes[1] < 7:
                weights = [1, 10]
            if self.likes[1] > 6:
                weights = [1, 5]
            fon = random.choices(opt, weights=weights, k=1)[0]
            if fon == 'df':
                self.dirflip()        
        if self.px == 10 or self.px == 1029:
            self.dirflip()
        opt = ['change', 'nochange']
        if self.likes[2] > 3:
            if self.likes[2] < 5:
                weights = [1, 20]
            if self.likes[2] > 4 and self.likes[2] < 8:
                weights = [2, 10]
            if self.likes[2] > 7:
                weights = [4, 10]
            ud = random.choices(opt, weights=weights, k=1)[0]
            if ud == 'change':
                opt2 = ['up', 'straight', 'down']
                weights  = [1, 1, 1]
                ac = random.choices(opt2, weights=weights, k=1)[0]
                self.act[0] = ac      
        if self.act[0] == 'up':
            self.py -= 1
        if self.act[0] == 'down':
            self.py += 1       
        if self.act[3] == 'l':
            self.px -= 10
        if self.act[3] == 'r':
            self.px += 10
        if obj.status[1] > 0:
            obj.status[1] -= 1
        else:
            obj.status[1] = 2
            if obj.status[0] == 1:
                obj.status[0] = 2
            else:
                obj.status[0] = 1

class egg:
    def __init__(self, tank, id, col, px, status, time, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2, attributes=None):
        self.tank = tank
        self.id = id
        self.col = col
        self.px = px
        self.status = status 
        self.time = time
        self.mt = mt
        self.ch1m = ch1m
        self.ch1p = ch1p
        self.ch2m = ch2m
        self.ch2p = ch2p
        self.ch3m = ch3m
        self.ch3p = ch3p
        self.ch4m = ch4m
        self.ch4p = ch4p
        self.z1 = z1
        self.z2 = z2
        self.rect = pygame.Rect(self.px, 10, 100, 100)
    def draw(self):
        fch_draw.drawegg(self, screen)
    def hatch(self):
        if self.status == 'dip':
            check = f_int.hatchcheck(self)
            if check == True:
                if self.z1[6] == 'on' or self.z2[6] == 'on':
                    if self.ch1m[11] == 'on' or ch1p[11] == 'on':
                        i = 1
                        h = 50
                        act = ['up', 'u', 'u', 'l', ]
                        status = [2, 4, 3, 15, 30]
                        df = f_int.rdf(self)
                        likes = [3, df, 8]
                        small.append(fry(self.tank, self.id, self.px, 1000, 100, act, status, self.mt, self.ch1m, self.ch1p, self.ch2m, self.ch2p, self.ch3m, self.ch3p, self.ch4m, self.ch4p, self.z1, self.z2, likes))   
                        eggs.remove(self)    
            else:
                self.status = 'rot1'
    def grow(self):
        if self.time > 0:
            self.time -= 1
        else:
            self.hatch()
class b:
    def __init__(self, tank, type, stage, h, timer):
        self.tank = tank        
        self.type = type
        self.stage = stage
        self.h = h
        self.timer = timer
    def oxdep(self):
        for t in tanks:
            if t.name == self.tank:
                if t.oxy > 0:
                    i = self.stage
                    t.oxy -= i
            if t.oxy < 0:
                t.oxy = 0
    def oxymake(self):
        global oxy
        i = self.stage
        oxy += i
    def win(self):
        if self.h != None:
            for obj in en:
                if obj.id == self.h:
                    obj.status[7] -= 1 #* self.stage   
    def dflf(self):
        if self.h != None:
            for obj in en:
                if obj.id == self.h:
                    obj.dirflip()       
                    obj.likes[4] = -40 
                    obj.likes[5] = 40
                    if self.stage > 15:
                        obj.status[3] = 10
                        obj.likes[3] == 0
                        obj.likes[6] == 0
                        obj.likes[4] = 0
    def ininf(self):
        if self.h == None:
            pot_h = [obj for obj in en if obj.status[7] < 1 and obj.tank == self.tank]
            if pot_h:
                hf = random.choice(pot_h)
                self.h = hf.id
    def biteinf(self, nh):
        tank = self.tank
        type = self.type
        stage = 1
        h = nh.id
        timer = 0
        if nh.z1[0] == 'on' and nh.z2[0] == 'on':
            mi.append(b(tank, type, stage, h, timer))
    def freeinf(self):
        if self.h  == None:
            pot_h = [obj for obj in en if obj.tank == self.tank]
            if pot_h:
                hf = random.choice(pot_h)
                self.h = hf.id
    def spread(self):
        if self.h != None:
            tank = self.tank
            type = self.type
            stage = 0
            h = None 
            timer = 0
            mi.append(b(tank, type, stage, h, timer))
    def slowrep(self):
        if self.stage < 20:
            if self.timer < 1:
                self.stage += 1            
    def rep(self):
         if self.stage < 20:
             newstage = self.stage * 2
             self.stage = newstage
    def act(self):
        if self.type == 'dr':
            self.oxdep()       
        if self.type == 'in':
            self.win()
            self.ininf()
        if self.type == 'frin':
            self.win()
            self.freeinf()
        if self.type == 'dir':
            self.dflf()
            self.slowrep()
            if self.timer > 0:
                self.timer -= 1
            else:
                self.timer = 10
        if self.type == 'oxmake':
            self.oxymake()
class dan:
    def __init__(self, tank, id, c, time, px, col1, col2, f1, f2, m1, m2, z1, z2, attributes=None):
        self.tank = tank
        self.id = id
        self.c = c
        self.time = time
        self.px = px
        self.col1 = col1
        self.col2 = col2
        self.f1 = f1
        self.f2 = f2
        self.m1 = m1
        self.m2 = m2
        self.z1 = z1
        self.z2 = z2
        self.rect = pygame.Rect(self.px, 10, 100, 100)
    def bproduce(self, b):
        if self.time < 10:
            tank = self.tank
            type = 'dr'
            stage = 1
            h = None
            timer = 0
            mi.append(b(tank, type, stage, h, timer))
    def draw(self):
        if self.time > 10:
            f_draw.drawd(self, screen)
        else:
            f_draw.rdraw(self, screen)
class f:
    def __init__(self, tank, px, py, col, f_size, attributes=None):
        self.tank = tank
        self.px = px
        self.py = py
        self.col = col
        self.f_size = f_size
        self.rect = pygame.Rect(self.px, self.py, 100, 100)
    def ap(self):
        if self.col == 'yellow':
            cl = (250, 250, 0)
        if self.col == 'white':
            cl = (250, 250, 250)
        if self.col == 'orange':
            cl = (250, 120, 0)
        pygame.draw.rect(screen, cl, (self.px, self.py, self.f_size, self.f_size))
class an:
  def __init__(self, tank, id, px, py, mem, act, status, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2, likes, attributes=None):
    self.tank = tank
    self.id = id
    self.px = px
    self.py = py
    self.mem = mem[:]
    self.act = act[:]
    self.status = status[:] 
    self.mt = mt[:]
    self.ch1m = ch1m[:]
    self.ch1p = ch1p[:]
    self.ch2m = ch2m[:]
    self.ch2p = ch2p[:]
    self.ch3m = ch3m[:]
    self.ch3p = ch3p[:]
    self.ch4m = ch4m[:]
    self.ch4p = ch4p[:]
    self.z1 = z1[:]
    self.z2 = z2[:]
    self.likes = likes[:]
    self.rect_a = pygame.Rect(px, py, 60, 60)
    self.rect_b = pygame.Rect(my_mod.middle(self.px, 900), (my_mod.middle(self.py, 900)), 900, 900)   
    self.rect_c = pygame.Rect(px, py, 30, 20)
  def cfix(self):
      if self.act[3] == 'l':
          self.rect_c.x = self.px - 25
      else:
          self.rect_c.x = self.px + 90
      self.rect_c.y = self.py + 20
  def dirflip(self):
     if self.status[2] > 1:
         if self.act[3] == 'l':
             self.act[3] = 'r'
         else:
             self.act[3] = 'l'
         self.mem.insert(1, 'df')
         self.cfix
  def brupdate(self):
      if self.z1[4] or self.z2[4] == 'f':
          if self.status[10] < 100:
              self.status[10] += 1
  def metupdate(self):
      if self.status[4] > 0:
          if self.status[2] < 1:
              self.status[4] -= 1
              self.status[2] += 200
      if self.status[6] > 0:
          self.status[6] -= 1
      elif self.status[6] < 1 :
          self.status[6] = 40
          self.status[5] -= 1
      if self.status[7] < 1:
           if self.status[6] < 1:
               if self.ch1m[2] == True or self.ch1p[2] == True:
                   self.status[7] +=1
                   self.status[5] -= 1    
#immune  
      if self.ch2m[7][0] == True or self.ch2p[7][0] == True:
          if self.z1[2] == 'on' or self.z2[2] == 'on':
              i = self.ch2m[7][1]  + self.ch2p[7][1]
              for obj in mi:
                  if obj.h == self.id:
                      if obj.type == 'frin' or obj.type == 'in':
                          if i > obj.stage:
                              d = 1
                          obj.stage -= i
                          
  def move(self):
#      if self.act[0] == 'straight':
#          self.col1[6] = 'on'
      if self.status[2] > 0:
           if self.act[1] == 'fast':
               fast = 2
           else:
               fast = 1
           if self.act[3] == 'l' and self.status[12] == True:
               self.px -= 10 * fast
           elif self.status[12] == True:
               self.px += 10 * fast
           if self.act[0] == 'down':
               if self.ch1m[4] == 'on' or self.ch1p[4] == 'on':
                   self.py += fast * fast
           if self.act[0] == 'up' and self.status[12] == True:
               if self.ch1m[4] == 'on' or self.ch1p[4] == 'on':
                   self.py -= fast * fast        
           if self.status[1] > 1:
               self.status[1] -= 1
           else:
                self.status[1] = 4
                if self.status[0] == 1:
                   self.status[0] = 2
                else:
                   self.status[0] = 1
                minus= 5
                if self.ch1m[1] == True or self.ch1p[1] == True:
                   minus -= 2
                if self.ch1m[9][0] == True:
                   minus -= ch1m[9][1]
                if self.ch1p[9][0] == True:
                   minus -= ch1p[9][1]
                if self.act[1] == 'fast':
                    m_ = minus
                    minus = m_ + m_
                    self.act[2] -= 1
                    if self.act[2] < 1:
                        self.act[1] = ''
                    if self.act[1] == '' and self.act[2] < 60:
                        self.act[2] += 2
                        if self.ch3m[5] == 'on' or self.ch3p[5] == 'on':
                            self.act[2] += 2
                if self.ch2m[8] == 'on' or self.ch2p[8] == 'on':
                    if self.status[0] == 2:
#                        energy save energy only - at fin condition 
#                        self.col1[1] = 'n'
#                        self.col2[1] = 'n'
                        self.status[2] -= minus
#                    else:
#                        self.col1[1] = 'on'
                else:
                   self.status[2] -= minus
      self.cfix()
      self.rect_a.x = self.px
      self.rect_a.y = self.py
      self.rect_b.x = my_mod.middle(self.px, 900)
      self.rect_b.y = my_mod.middle(self.py, 900)
  def memclear(self):
      newmem = [self.mem[0], self.mem[1], self.mem[2]]
      memnum = len(self.mem)
      if self.ch3m[2][0] == True or self.ch3p[2][0] == True:
          if memnum > 3:
              i = self.ch3m[2][1] + self.ch3p[2][1]
              toindex = i + 2
              if memnum - 1 > toindex:
                  toindex = memnum - 1
              newmem = self.mem[: toindex]
      self.mem = newmem
  def learn(self):
      a = self.ch1m[0] + self.ch1p[0]
      r = self.ch2m[0] + self.ch2p[0]
      if self.mem[0] > 5 or self.mem[0] < -5:
          if self.z1[1] == 'on' or self.z2[1] == 'on' and self.ch3m[1] == 'on' or self.ch3p[1] == 'on':
              if self.mem[0] > 5 :
                  if a > 0:
                      addmin = 'add'
              else:
                  addmin = 'min'
              tap = 'tap'
              if tap in self.mem:
#                  self.col1[0] = ''
#                  self.col2[0] = ''
                  if addmin == 'add':
                      self.likes[9] += a
                  else:
                      self.likes[9] -= r
              if self.py  < 400:
                  if addmin == 'add':
                      self.likes[8] += a
                  else:
                      self.likes[8] -= r
  def react(self, event_pos):
      if not self.rect_a.collidepoint(event.pos):
          if self.rect_b.collidepoint(event.pos):
              self.mem.insert(1, 'tap')
              mx, my = event.pos
              goto_y = self.act[0]
              goto_x = self.act[3]
              if self.likes[9] > 5:
                  if mx > self.px:
                      goto_x = 'r'
                  else:
                      goto_x = 'l'
                  if my > self.py:
                      goto_y = 'down'
                  else:
                      goto_y = 'up'
                  self.act[1] = 'fast'
              if self.likes[9] < -5:
                  if mx > self.px:
                      goto_x = 'l'
                  else:
                      goto_x = 'r'
                  if my > self.py:
                      goto_y = 'up'
                  else:
                      goto_y = 'down'
              self.act[0] = goto_y
              if self.act[3] != goto_x:
                  self.dirflip()
              self.act[1] = 'fast'
  def social(self):
      eye = iseyes(self)
      if self.likes[4] > 4 and eye == True:
          for obj in en:
                          if obj != self and obj.tank == self.tank:
                              yval = self.py - obj.py
                              yfix = abs(yval)
                              if yfix < 600:
                                  if self.act[3] != obj.act[3]:
                                      self.dirflip()
                                  if yfix > 100:
                                      if self.py > obj.py:
                                          self.act[0] = 'up'
                                      else:
                                          self.act[0] = 'down'
      if self.likes[4] < 0 and eye == True:
          for obj in en:
              if obj!= self and obj.tank == self.tank:
                  yval = self.py - obj.py
                  yfix = abs(yval)
                  if yfix < 600:
                      if self.likes[5] > 5:
                          if self.px > obj.px + 10 and self.act[3] == 'r':
                              self.dirflip()
                          if self.px < obj.px and self.act[3] == 'l':
                              self.dirflip()
                          if obj.py > self.py:
                              self.act[0] = 'down'
                          elif self.py > obj.py:
                              self.act[0] = 'up'
#                          if self.px == obj.px and self.py :
                          if self.rect_c.colliderect(obj.rect_a):
                              self.act[0] = 'eat'
                              obj.status[7] -= 1
                              obj.likes[4] -= 1
                              obj.mem.insert(1, 'bitten')
                              self.mem.insert(1, 'bite')
                              for o in mi:
                                  if o.type == 'dir' and o.h == self.id:
                                      o.biteinf(obj)
                      else:
                          if self.px > obj.px and self.act[3] == 'l':
                              self.dirflip()
                          if self.px < obj.px and self.act[3] == 'r':
                              self.dirflip
                          if obj.py > self.py:
                              self.act[0] = 'up'
                          elif self.py > obj.py:
                              self.act[0] = 'down'              
      if self.likes[3] > 5:           
          if self.px == 10:                                                 
                                 self.dirflip()
          if self.px == 970:
                                 self.dirflip()                                        
  def br(self):
      if self.z1[3] == 'on' and self.z2[3] == 'on':
          if self.py < 1800:
              self.act[0] = 'down'
          if self.z1[4] == 'm' or self.z2[4] == 'm':
              for obj in eggs:
                  if obj.status == 'hap' and obj.tank == self.tank:
                      if self.z1[5] == 'm' or self.z2[5] == 'm':
                          pats = f_int.mei(self)
                          obj.ch1p = pats[0]
                          obj.ch2p = pats[1]
                          obj.ch3p = pats[2]
                          obj.ch4p = pats[3]
                          obj.z2 = pats[4]
                          obj.time = 100
                          obj.status = 'dip'
                          eid = obj.id
                          addoff(self, eid)
      else:
          if self.z1[4] or self.z2[4] == 'f':
              if self.status[10] > 39:
                  if self.py < 1800:
                      self.act[0] = 'down'
              if self.status[10] < 30:
                  self.act[0] = 'up'
              if self.status[10] > 90 and self.py > 1799:
                  if self.z1[5] == 'e' or self.z2[5] == 'e':
                      self.status[10] = 0
                      ats = f_int.egg_at(self)
                      eid = next_id
                      updateid()
                      eggs.append(egg(ats[0], eid, ats[1], ats[2], ats[3], ats[4], ats[5], ats[6], ats[7], ats[8], ats[9], ats[10], ats[11], ats[12], ats[13], ats[14], ats[15]))
                      addoff(self, eid)
                      eggcol(self, ats[1])
#return tan0k, c1ol, 2px, stat3us, ti4me, 5mt, c6h1m, ch71p, c8h2m, c9h2p, c10h3m, ch311p, ch412m, ch413p, z141, 15z2                      
      if self.likes[3] > 5:
          if self.px == 10:                                                 
                                 self.dirflip()
          if self.px == 970:
                                 self.dirflip()          
          
#      else:
#          f = 2                    
  def dec(self):
      if self.likes[6] > 3:
          opt = ['df', 'nf']
          if self.likes[6] == 4:
              weights = [1, 20]
          if self.likes[6] > 4 and self.likes[6] < 7:
              weights = [1, 10]
          if self.likes[6] > 6:
              weights = [1, 5]
          fon = random.choices(opt, weights=weights, k=1)[0]
          if fon == 'df':
              self.dirflip()
      opt = ['change', 'nochange']
      if self.likes[7] > 3:
          if self.likes[7] < 5:
              weights = [1, 20]
          if self.likes[7] > 4 and self.likes[7] < 8:
              weights = [2, 10]
          if self.likes[7] > 7:
              weights = [4, 10]
          ud = random.choices(opt, weights=weights, k=1)[0]
          if ud == 'change':
              opt2 = ['up', 'straight', 'down']
              weights  = [1, 1, 1]
              ac = random.choices(opt2, weights=weights, k=1)[0]
              self.act[0] = ac
      if self.likes[8] < 0:
          if self.py < 400:
              self.act[0] = 'down'
      if self.likes[8] > 9:
          if self.py > 400:
              self.act[0] = 'up'
#      self.col1[5] = 'o'
#      self.col2[5] = 'o'
      for f in ad:
          if f.py > self.py:
              hy = f.py
              sy = self.py
          else:
              hy = self.py
              sy = f.py
          yd = hy - sy
          if yd < 600:
              if f.px > self.px:
                  hx = f.px
                  lx = self.px
              else:
                  hx = self.px
                  lx = f.px
              xd = hx - lx
              if xd < 600:
                  see = False
                  eye = iseyes(self)
                  if eye == True:
                      if f.col == 'orange':
                          see = True
                      if f.col == 'yellow':
                          if self.ch1m[4] == 'on' or self.ch1p[4] == 'on':
                              see = True
                      if see == True:
                          tofood = 'yes'
                          if self.z1[0] == 'on' or self.z2[0] == 'on':
                              if self.status[3] > 9:
                                  tofood = 'no'
                              if f.col == 'white':
                                  if self.status[3] > 4:
                                      if self.likes[0] < 6:
                                          tofood = 'no'
                              if f.col == 'orange':
                                  if self.status[3] > 6:
                                      if self.likes[1] < 6:
                                          tofood = 'no'
                              if f.col == 'yellow':
                                  if self.status[3] > 4:
                                      if self.likes[2] < 6:
                                          tofood = 'no'
                          if tofood == 'yes':
#                                 self.col1[6] = 'm'
#                                 self.col2[6] = 'm'
                                 self.move()
                                 if self.act[3] == 'l':
                                     if f.px > self.px:
                                         self.dirflip()
                                 else:
                                     if f.px < self.px:
                                         self.dirflip()                                        
                                 if f.py > self.py and f.py - self.py == 25:  
                                     self.act[0] = 'straight'  
                                     if self.px > f.px:
                                         g = self.px
                                         s = f.px                                    
                                     else:
                                         g = f.px
                                         s = self.px
                                     if self.rect_c.colliderect(f.rect):                                      
                                         if f.col == 'yellow':
                                             self.act[0] = 'eat'
                                             self.status[4] += 10
                                             if self.ch4m[3] == 'on':
                                                 self.status[3] += 1
                                             mood = self.mem[0]
                                             mood += 5
                                             self.mem[0] += mood
                                             if self.ch1p[8] == 'on':
                                                 self.status[5] += 10
                                             ad.remove(f)
                                         if f.col == 'orange':
                                             self.status[4] += 40
                                             self.status[5] += 40
                                             self.status[3] += 1
                                             self.mem[0] += 5
                                             ad.remove(f)
                                             if self.likes[1] > self.likes[2]:
                                                 self.mem[0] += 5
                                 if self.py > f.py:
                                                   self.act[0] = 'up'
                                 if f.py > self.py:
                                                   if f.py - self.py > 25:
                                                       self.act[0] = 'down'
                                                   if f.py - self.py < 25:
                                                       self.act[0] = 'up'
      self.social()

  def shape_draw(self):
      fch_draw._draw(self, screen)         
#tank
name = 't1'
type = 'general'
hardness = 15
oxy = 100
tanks.append(tank(name, type, hardness, oxy))      
name = 't2'
type = 'br'
hardness = 15
oxy = 100
tanks.append(tank(name, type, hardness, oxy))   
#make
tank = 't1'
g = [True, 1]
m = [False, 2]
e = 'eat'
px = 200
py = 1800     
mem = [-20, '0', '0']
dir = 'l'
act = ['', '', 5, 'l', 'r']
ie = True
f = True
status = [2, 4, 10, 0, 50, 40, 1, 1, 10, 40, 0, ie, f]    
mt = [e, e]     
ch1m = [1, True, True, g, 'on', 'on', 'on', 'n', g, g, g, 'on']
ch1p = [1, True, True, g, 'on', 'on', 'on', 'n', g, g, g, 'on']
ch2m = [1, 'on', g, m, g, 's', 'cir', g, 'on', 1, g]
ch2p = [1, 'on', g, g, g, 's' , 'tri', g, 'on', 1, g]
ch3m = [1, 'on', g, g, 'on', 'on', 'l', 'l']
ch3p = [1, 'on', g, g, 'on', 'on', 'l', 'l']
ch4m = [1, 't', g, 'on']
ch4p = [1, 't', g, 'on']
z1 = ['on', 'on', 'on', 'on', 'm', 'm', 'on']
z2 = ['on', 'on', 'on', 'on', 'm', 'm', 'on']
likes = [0, 0, 10, 10, 10, 0, 10, 10, 10, -6]
en.append(an(tank, 0, px, py, mem, act, status, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2, likes))
#2
tank = 't1'
g = [True, 1]
m = [True, 2]
n = [False, 0]
N = None
px = 200
py = 1800     
mem = [-20, '0', '0']
dir = 'l'
act = ['', '', 5, 'l', 'r']
ie = True 
f = True
status = [2, 4, 10, 0, 50, 40, 1, 1, 10, 40, 100, ie, f]         
mt = [e, e]
ch1m = [1, True, True, g, 'on', 'on', 'on', 'on', m, g, g, 'on']
ch1p = [1, True, True, g, 'on', 'on', 'on', 'on', m, g, g, 'on']
ch2m = [1, 'on', g, m, g, 's', 'cir', n, 'on', 1, n]
ch2p = [1, 'on', g, m, g, 's', 'tri', n, 'on', 1, n]
ch3m = [1, 'on', g, g, 'on', 'on', 'l', 'l']
ch3p = [1, 'on', g, n, 'on', 'on', 'l', 'l']
ch4m = [1, 't', g, 'on']
ch4p = [1, 't', g, 'on']
m1 = []
m2 = []
z1 = [N, N, N, N, 'f', 'e', N, N]
z2 = ['on', 'on', 'on', 'on', 'on', 'on', 'on']
likes = [0, 0, 10, 10, 10, 0, 10, 10, 10, -6]
en.append(an(tank, 1, px, py, mem, act, status, e, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2, likes))
#df
tank = 't1'
id = 3
c = 'a'
time = 2
px = 200
col1 = ['on', 'on', 'o', 'n', 'on', 'on', 'on']
col2 = ['on', 'on', 'o', 'n', 'on', 'on', 'on']
f1 = ['on', 'on', 'on', 'tri', 'on']
f2 = ['on', 'on', 'on', 'tri', 'on']
m1 = ['n', 'on', 'on', 'on', 'on', 'on', 'on' ]
m2 = ['n', 'on', 'on', 'on', 'on', 'on', 'on' ]
z1 =  ['on', 'on', 'on']
z2 = ['on', 'on', 'o']
#ed.append(dan(tank, id, c, time, px, col1, col2, f1, f2, m1, m2, z1, z2))
#b make
tank = 't1'
type = 'frin'
stage = 1
h = None
timer = 0
mi.append(b(tank, type, stage, h, timer))
def cf():
    global oxy
    for obj in en:
            c = None
            for t in tanks:
                if t.name == obj.tank:
                    if t.oxy < 6:
                        c = {'LO'}
            if obj.status[7] < - 20:
                if c == None:
                    c = {'inj'}
                else:
                    c.add('inj')
            if obj.status[4] < 1:
                if c == None:
                    c = {'enout'}
                else:
                    c.add('enout')
            if obj.status[5] < 1:
                if c is None:
                    c = {'LP'}
                else:
                    c.add('LP')
            if obj.status[3] > 10:
                if c == None:
                    c = {'OE'}
                else:
                    c.add('OE')
            for bo in mi:
                if bo.h == obj.id:
                    ic = bo.type
                    if c != None:
                        c.add(ic)
            if c != None:
                tank = obj.tank
                id = obj.id               
                time = 20
                px = obj.px
                col1 = obj.col1
                col2 = obj.col2
                f1 = obj.f1
                f2 = obj.f2
                m1 = obj.m1
                m2 = obj.m2
                z1 = obj.z1
                z2 = obj.z2
                ed.append(dan(tank, id, c, time, px, col1, col2, f1, f2, m1, m2, z1, z2))
                en.remove(obj)
#                en = [o for o in en if o is not obj]           
hardness_mesure = 'yes' 
oxmesure = 'yes'
time = 10
currenttank = 't1'
draged = None
picked = None
status = 'gen'
popup = None
rect1 = pygame.Rect(100, 1, 50, 50)
rect2 = pygame.Rect(500, 1, 50, 50)
rect3 = pygame.Rect(1000, 1, 50, 50)
back = pygame.Rect(20, 220, 50, 50)
m1rect = pygame.Rect(20, 280, 50, 50)
m2rect = pygame.Rect(20, 340, 50, 50)
m3rect = pygame.Rect(20, 400, 50, 50)
m4rect = pygame.Rect(20, 460, 50, 50)
m5rect = pygame.Rect(20, 520, 50, 50)
def tankchoice(e):
    ct = None
    ra = None
    if m1rect.collidepoint(e):
        ra = 0
    elif m2rect.collidepoint(e):
        ra = 1
    elif m3rect.collidepoint(e):
        ra = 3
    if ra != None:
        CTo = tanks[ra]
        ct = CTo.name
    return ct
for obj in en:
    adata(obj)   
pygame.init()
screen_width = 1000
screen_hight = 1000
screen = pygame.display.set_mode((screen_width, screen_hight), 0, 32)
tp = pygame.Surface((screen_width, screen_hight), pygame.SRCALPHA)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (100, 150, 200)
pink = (120, 255, 255)
orange = (100, 0, 100)
tankcollor = blue
mes = pygame.font.SysFont(None, 48) 
current_message = "none"
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if status == 'yellow':
                plx, pl = event.pos
                ad.append(f(currenttank, plx, 100, 'yellow', 10))
            if status == 'white':
                plx, pl = event.pos
                ad.append(f(currenttank, plx, 100, 'white', 40))
            if rect1.collidepoint(event.pos):
                status = 'yellow'
            if rect2.collidepoint(event.pos):
                status = 'white'
            if rect3.collidepoint(event.pos):
                popup = 'mainmenu'
                status = 'n'
            if popup == 'credit':
                if back.collidepoint(event.pos):
                    popup = 'None'
            if popup == 'tanks':
                if back.collidepoint(event.pos):
                    popup = 'mainmenu'
                ct = tankchoice(event.pos)
                if ct != None:
                    currenttank = ct
                    for t in tanks:
                        if t.name == currenttank:
                            ttype = t.type
                    if ttype == 'br':
                        tankcollor = pink
                    else:
                        tankcollor = blue
                    popup = None
            if popup == 'mainmenu':
                if back.collidepoint(event.pos):
                    popup = None 
                elif m1rect.collidepoint(event.pos):
                    popup = 'tanks'             
                elif m3rect.collidepoint(event.pos):
                    popup = 'credit'
            if popup == 'fishmain':
                if back.collidepoint(event.pos):
                    popup = None
                elif m1rect.collidepoint(event.pos):
                    popup = '1'
                elif m2rect.collidepoint(event.pos):
                    popup = '2'
                elif m3rect.collidepoint(event.pos):
                    popup = '3'
                elif m4rect.collidepoint(event.pos):
                    popup = '4'
                elif m5rect.collidepoint(event.pos):
                    popup = '5'
            if popup == '1' or popup == '2' or popup == '3' or popup == '4' or popup == '5':
                if back.collidepoint(event.pos):
                    popup = 'fishmain'
            if popup == 'currentmessage' and back.collidepoint(event.pos):
                popup = None
            if popup == '2':
                if m5rect.collidepoint(event.pos):
                    current_message = health_check(picked)
                    popup = 'currentmessage'
            if popup == '4':
                if m2rect.collidepoint(event.pos):
                    for obj in en:
                        if obj == picked:
                            en.remove(obj)
                            picked = None
                            popup = None
            if popup == '5':
                ct = tankchoice(event.pos)
                if ct != None and picked != None:
                    picked.tank = ct
                    for b in mi:
                        if b.h == picked.id:
                            b.tank = picked.tank
                    popup = None
            if popup == 'df':
                if m2rect.collidepoint(event.pos):                    
                    current_message = nec(picked)
                    popup = 'currentmessage'
            if popup == 'df':
                if m5rect.collidepoint(event.pos):
                    popup = None
                    ed.remove(picked)
            for obj in en:
                if obj.tank == currenttank:
                    obj.react(event.pos)
                    if obj.rect_a.collidepoint(event.pos):
                        draged = obj.id
                        picked = obj
                        popup = 'fishmain'
            for obj in small:
                if obj.rect.collidepoint(event.pos):
                    popup = 'df'
                    picked = obj         
            for obj in ed:
                if obj.rect.collidepoint(event.pos):
                    popup = 'df'
                    picked = obj         
        elif event.type == pygame.MOUSEMOTION:                    
                    mouse_x, mouse_y = event.pos
                    for obj in en:
                        if draged == obj.id:
                            obj.px = mouse_x
                            obj.py = mouse_y
                            obj.rect_a.x = obj.px
                            obj.rect_a.y = obj.py
        elif event.type == pygame.MOUSEBUTTONUP:
                   draged = None 
    # Fill the screen with a background color (e.g., black)
    screen.fill(tankcollor)
    for obj in mi:
        obj.act()
    if time > 0:
        time -= 1
    else:
        time = 10
        for obj in mi:
            obj.act()
        for obj in ed:
            obj.time -= 1
    for obj in mi:
        if obj.stage < 1:
            mi.remove(obj)
        if obj.type == 'dir':
            if obj.stage > 16:
                obj.act()
    for obj in ed:
        obj.draw()
        obj.bproduce(b)
    for obj in eggs:
        obj.draw()
        obj.grow()
    for obj in small:
        obj.draw()
        obj.move()
        obj.grow()
        if obj.px < 10:
            obj.px = 10
        if obj.px > 1030:
            obj.px = 1029
        if obj.py > 2039:
               obj.py = 2000
        if obj.py < 0:
               obj.py = 0        
    for obj in en:
        obj.shape_draw()
#        obj.dec()
        obj.br()
        obj.move()
        obj.brupdate()
        obj.metupdate()
        obj.learn()
        obj.memclear()
        for t in tanks:
            if t.name == obj.tank:
                wq = t.hardness
        if wq < obj.status[8]:
            obj.status[7] -= 1
        if wq > obj.status[9]:
            obj.status[7] -= 1
        if obj.px < 10:
            obj.px = 10
        if obj.px > 970:
            obj.px = 970
        if obj.py > 2000:
               obj.py = 2000
        if obj.py < 0:
               obj.py = 0
    for obj in ad:
        obj.ap()
        obj.py += 1
        if obj.col == 'white':
            obj.f_size -= 4
            for t in tanks:
                if t.name == obj.tank:
                    t.hardness += 1
            if obj.f_size < 1:
                ad.remove(obj)
 #   cf()
    red = (200, 0, 0)
    white = (200, 200, 200)
    pygame.draw.rect(screen, red, (100, 1, 50, 50))
    pygame.draw.rect(screen, orange, (500, 1, 50, 50))    
    pygame.draw.rect(screen, orange, (1000, 1, 50, 50))
#    if oxy < 10:
#        pygame.draw.rect(screen, red, (1060, 1, 500, 500))
    if hardness_mesure == 'yes':
        for t in tanks:
            if t.name == currenttank:
                hardness = t.hardness
        hard = mes.render(f"hard {hardness}", True, (0, 0, 0))
        hard_rect = hard.get_rect(center=(250, 250))
        screen.blit(hard, hard_rect)
    if oxmesure == 'yes':
        for t in tanks:
            if t.name == currenttank:
                oxy = t.oxy
        oxm = mes.render(f"oxygen {oxy}", True, (0, 0, 0))
        ox_rect = oxm.get_rect(center=(250, 300))
        screen.blit(oxm, ox_rect)
    if popup == 'mainmenu':
       popups.main(back, m1rect, m2rect, m3rect)
    if popup == 'fishmain':
        popups.fishmain(back, m1rect, m2rect, m4rect, m5rect)
    if popup == '1':
        popups.m1(back, 'mes1')   
    if popup == '2':
        popups.m2(back, m5rect, 'mes2')
    if popup == '3':
        popups.m3(back, m2rect, m5rect)                     
    if popup == '4':
        popups.m4(back, m2rect, m5rect)  
    if popup == '5':
        tanksget('none', back)
    if popup == 'tanks':
        tanksget('none', back)
    if popup  == 'currentmessage':
        popups.current_mes(current_message)   
    if popup == 'credit':
        popups.credits(back, m1rect)
    if popup == 'df':
        pygame.draw.rect(screen, white, (20, 200, 800, 800))
        pygame.draw.rect(screen, red, (back.x, back.y, 50, 50))
        bacm = mes.render(f"back", True, (0, 0, 0))        
        bacrect = bacm.get_rect(center=(100, 250))
        screen.blit(bacm, bacrect)
        message = mes.render(f"mesage3", True, (0, 0, 0))
        me_rect = message.get_rect(center=(100, 300))
        screen.blit(message, me_rect)       
        pygame.draw.rect(screen, red, (m2rect.x, m2rect.y, 50, 50))
        pygame.draw.rect(screen, red, (m5rect.x, m5rect.y, 50, 50))                                      
    screen.blit(tp, (0, 0)) 
    pygame.display.flip()