import random 
def iseyes(own):
    eyes = False
    if own.ch2m[4][0] == True and own.ch2p[4][0] == True:
        if own.ch2m[4][1] > 0 and own.ch2p[4][1] > 0:
            if own.ch1m[7] == 'on' or own.ch1p[7] == 'on':
                eyes = True
                return eyes
def isfin(own):
    fin = False
    if ch2m[1]  == 'on' or ch2p[1] == 'on':
        if ch2m[6] == 'cir' or 'tri' or ch2p[6] == 'cir' or 'tri':
            if ch2m[2][0] == True or ch2p[2][0] == True:
                if ch2m[2][1] > 0 or ch2p[2][1] > 0:
                    fin = True
class egg:
    def __init__(self, tank, col, px, status, time, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2):
        self.tank = tank
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
def check_la(lst, lenth):
    if isinstance(lst, list, lenth):
        count = len(lst)
        if count > lenth - 1:
            check = True
        else:
            check = False
    else:
        check = False 
def cr(own):
    if own.ch2m[5] == 's' or own.ch2p[5] == 's':
        st = random.choice([own.ch1m, own.ch1p])
        if st == own.ch1m:
            ad = own.ch1p
        else:
            ad = ch1m       
        r = st    
        i = random.randrange(2, 4)
        r[0:i] = ad[0:i] 
        i = random.randrange(7, 9)      
        r[i:] = st[i:]    
        return r
def mei(own):
    if own.ch2m[5] == 's' or own.ch2p[5] == 's':
        st1 = random.choice([own.ch1m, own.ch1p])
        if st1 == own.ch1m:
            ad1 = own.ch1p
        else:
            ad1 = ch1m
        i = random.choices([2, 3, 4])
        
    ch1 = random.choice([own.ch1m, own.ch1p])
    ch2 = random.choice([own.ch2m, own.ch2p])
    ch3 = random.choice([own.ch3m, own.ch3p])
    ch4 = random.choice([own.ch4m, own.ch4p])
    z = random.choice([own.z1, own.z2])
    return ch1, ch2, ch3, ch4, z
def egg_at(own):
    tank = own.tank
    col = 'white'
    if own.ch2m[9] > 0:
        col = 'red'
        if own.ch2m[9] > 1:
            col = 'black'
    px = own.px
    status = 'hap'
    time = 100
    mt = own.mt
    chs = mei(own)
    ch1m = chs[0]
    ch1p = None 
    ch2m = chs[1]
    ch2p = None
    ch3m = chs[2]
    ch3p = None
    ch4m = chs[3]
    ch4p = None
    z1 = chs[4]
    z2 = None
    return tank, col, px, status, time, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2
def getmt(own):
    ltc = own.mt
    ecount = sum(word.count('e') for word in ltc)
    acount = sum(word.count('a') for word in ltc)
    tcount = sum(word.count('t') for word in ltc)
    maxmt = max(ecount, acount, tcount)
    minmt = min(ecount, acount, tcount)
    return ecount, acount, tcount, minmt, maxmt
def cel_h(own):
    pa = 0
    pb = 0
    ma = 0
    mb = 0
    if own.ch2m[10][0] == True:
        ma = own.ch2m[10][1]
    if own.ch2p[10][0] == True:
        mb = own.ch2m[10][1]
    m = ma + mb
    if own.ch1m[10][0] == True:
        pa = own.ch1[10][1]
    if own.ch1p[10][0] == True:
        pb = ch1p[10][1]
    p = pa + pb
    h = p - m
    return hl
def rdf(own):
    pa = 0
    pb = 0
    if own.ch4m[2][0] == True:
        pa = ch4m[2][1]
    if own.ch4p[2][0] == True:
        pb = ch4p[2][1]
    p1 = pa + pb
    if own.ch1m[6] == 'on':
        pa = 1
    if own.ch1p[6] == 'on':
        pb = 1
    p2 = pa + pb
    df = p1 + p2
    return df
#        act = ['down', '', 5, 'l', 'r']
#        status = [2, 4, 10, 0, 50, 40, 1, 1, 10, 40]
#        likes = likes = [0, 0, 10, 10, 10, 0, 10, 10, 10, -6]    
def gettempc(own):
    w = 0
    if own.ch1m[6] == 'on':
        w += 1
    if own.ch1p[6] == 'on':
        w += 1
    if own.ch1m[7] == 'on' or own.ch1p[7] == 'on':
        w += 1
    if own.ch1m[8][0] == True or own.ch1p[8][0] == True:
        i = own.ch1m[8][1] + own.ch1p[8][1]
        w += i
    if own.ch1m[10][0] == True or own.ch1p == True:
        i = own.ch1m[10][1] + own.ch1p[10][1]
        w += i * 2
    return w
def getact(own):
    lst = [own.act[0]]
    lst.append('n')
    lst.append(5)
    lst.append(own.act[3])
    return lst
def getstatus(own):
    lst = [1]    
    lst.append(1)
    lst.append(10)
    lst.append(1)
    lst.append(2)
    lst.append(2)
    lst.append(1)
#    inj
    lst.append(1)
#    h
    lst.append(own.status[3])
    lst.append(own.status[4])
    ie = iseyes(own)
    lst.append(ie)
    f = isfin
    lst.append(f)
    return lst
def getlikes(own):
    mit = getmt(own)
    lst = [0]
    o = 7
    lst.append(o)
    y = 10
    if own.ch2p[10][0] == True:
        i = ch2p[10][1]
        y -= 4 + i
    lst.append(y)
    lst.append(own.likes[3])
    lof = 0
    if own.ch4m[3] == 'on':
        lof += 1
    if own.ch4p[3] == 'on':
        lof += 1
    if own.ch1m[3][0] == True and ch1m[3][1] > 0:
        lof -= 2
    if own.ch1p[3][0] == True and ch1p[3][1] > 0:
        lof -= 2
    if mit[3] > 8:
        lof += 3
    lst.append(lof)
    t = gettempc(own)
    d = t
    lst.append(d)
    lst.append(own.likes[1])
    lst.append(own.likes[2])
    tos = 0
    lst.append(tos)
    t =  gettempc(own)
    user = 0
    if own.ch3m[1] == 'on' or own.ch3p[1] == 'on':
        i = 0
        if own.ch1m[2] == 'on':
            i += 1 
        if own.ch1p[2] == 'on':
            i +=1
        user -= t + i
        if mit[3] > 8:
            user += 2
    lst.append(user)
    return list 
en = []    
class fry:
    def __init__(self, act, status, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2,  likes):
        self.act = act
        self.status = status 
        self.likes = likes    
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
act = ['down', '', 5, 'l', 'r']
status = [2, 4, 10, 0, 50, 40, 1, 1, 10, 40]         
likes = [0, 0, 10, 10, 10, 0, 10, 10, 10, -6]
g = [True, 1]
N = None
e = 'eat'
mt = [e, e, e, e, e, e, e, e, e]
ch1m = [1, True, True, g, 'on', 'on', 'on', 'on', g, g, g, 'on']
ch1p = [1, True, True, g, 'on', 'on', 'on', 'on', g, g, g, 'on']
ch2m = [1, 'on', g, g, g, 's', 'cir', g, 'on', 1, g]
ch2p = [1, 'on', g, g, g, 's', 'tri', g, 'on', 1, g]
ch3m = [1, 'on', g, g, 'on', 'on', 'l']
ch3p = [1, 'on', g, g, 'on', 'on', 'l']
ch4m = [1, 't', g, 'on']
ch4p = [1, 't', g, 'on']
z1 = [N, N, N, N, 'f', 'e', N, N]
z2 = ['on', 'on', 'on', 'on', 'on', 'on', 'on']
en.append(fry( act, status, mt, ch1m, ch1p, ch2m, ch2p, ch3m, ch3p, ch4m, ch4p, z1, z2,  likes))
#                        act = ['up', 'u', 'u', 'l', ]
#                        status = [2, 4]
#                        likes = [3, 7, 8] 
for obj in en:    
    secondlist = getact(obj)
    wn = gettempc(obj)
    thirdlist = getlikes(obj)
    mit = getmt(obj)
    ch = mei(obj)
    r = cr(obj)
#print(secondlist)
print(r)
