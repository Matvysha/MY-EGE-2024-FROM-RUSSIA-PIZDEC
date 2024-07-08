print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (((x <= y) <= z) or not(w)) == 0:
                    print(w, x, y, z)

print ('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x == z) or (x <= (y and z))):
                print(x, y, z)

print ('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not((x == y) or ((y or z) <= x)):
                print(x, y, z) 
            
print ('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x and not(y)) or (y == z) or not(w)):
                    print(x, y, z, w)

print ('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((x <= y) and (y <= w) or (z == (x or y)))):
                    print(x, y, z, w)

print ('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x == (w or y)) or ((w <= z) and (y <= w))):
                    print(x, y, z, w)


print ('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((w or not(y)) and x) or (y == z)):
                    print(x, y, z, w)


def f(x, y, h):
    if h == 3 and x + y >= 47:
        return 1
    elif h == 3 and x + y < 47:
        return 0
    elif x + y >= 47 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x + 5, y, h + 1) or f(x, y + 5, h + 1)   # стратегия победителя
        else:
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x + 2, y, h + 1) or f(x, y + 2, h + 1)  # стратегия проигравшего(неудачный ход)
 
for x in range(1, 70):
    if f(x, 7, 1) == 1:
        print("Задача 19:", x)
        break


        
print ('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not ((x and not y) or (x == z) or not w):
                    print(x, y, z, w)

print ('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((y >= x) or (y == w) or z):
                    print(x, y, z, w)
                    
print ('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((not x or y) or (not w or not z) or w):
                    print(x, y, z, w)


def f4(n):
    s = ''
    while n > 0:
        s = str(n %4 ) + s
        n = n // 4
    return s

for n in range(1, 260):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[ -2: ]
    else:
        ost = f4( (n%4) * 2 )
        n4 = n4 + ost
    r = int(n4, 4)
    if r < 261:
        print(n)

def f4(n):
    s = ''
    while n > 0:
        s = str(n %4) + s
        n = n // 4
    return s 

for n in range(1, 368):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[ -2: ]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4, 4)
    if r < 369:
        print(n)


def f4(n):
    s = ''
    while n > 0:
        s = str(n %4) + s 
        n = n // 4
    return s 

for n in range(1,1024):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4 [ -2: ]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4,4)
    if r >= 1025:
        print(n)
        break


def f4(n):
    s = ''
    while n > 0:
        s = str(n %4) + s 
        n = n // 4
    return s 

for n in range(1,1087):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4 [ -2: ]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4,4)
    if r >= 1088:
        print(n)
        break

x = '1' * 2022
while '11' in x or '555' in x:
    if '11' in x:
        x = x.replace('11', '555', 1)
    else:
        x = x.replace('555', '5', 1)
print(x)

mx = 0
for n in range(4, 10000):
    s = '1' + '2' * n
    while '12' in s or  '3322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)
    sm = 0
    for i in s:
        sm += int(i)
    mx = max(mx, sm) == 218
print(mx)

for n in range(10001, 3, -1):
    s = '1' + '2' * n
    while '12' in s or '5522' in s or '2222' in s:
        if '12' in s: s = s.replace('12', '55', 1)
        if '2222' in s: s = s.replace('2222', '1', 1)
        if '5522' in s: s = s.replace('5522', '21', 1)
    x = str(sum ([int(x) for x in s]) ** 0.5)
    a = x.split('.')
    if len(set(s)) == 1 and list(s)[0] == '142':
        print(n)
        break

for n in range(10001, 3, -1):
    s ='4' + '1' * n
    while '31' in s or '411' in s or '1111' in s:
        if '31' in s: s = s.replace('31', '1', 1)
        if '411' in s: s = s.replace('411', '13', 1)
        if '1111' in s: s = s.replace('1111', '13', 1)
    if len(set(s)) == 1 and list(s)[0] == '36':
        print(n)
        break

for n in range(4, 10000):    
    s = '4' + '1' * n 
    while ('31' in s) or ('411' in s) or ('1111' in s):
        s = s.replace('31', '31', 1)
        s = s.replace('355', '52', 1)
        s = s.replace('555', '3', 1)
    if 2*s.count("2")+3*s.count("3")+5*s.count("5") == 17:
        print(n)
        break

x = '1' * 2023
while '211' in x or '112' in x:
    x = x.replace('11', '1', 1)
    if '21' in x:
        x = x.replace('21', '12', 1)
    if '12' in x:
        x = x.replace('12', '1', 1)
print(x)


from itertools import product
count = 0
k = 0
for i in product('АВИОРТФ', repeat=6):
    a = ''.join(i)
    count += 1
    if a.count('Р')==2 and a[0]!='О' and (count % 2 == 0):
        k += 1
print(k)

for x in '0123456789abcdefghijkl':
    x1 = '1' + x  + '1' + x  + '1' + x + '1' + x + '1' + x 
    x2 = '20' + x + '24'
    x3 = '1' + x + '235'
    res = int(x1, 23) + int(x2, 23) + int(x3, 23)
    if res % 22 == 0:
        res = res / 22
        print(res)

    import sys
    sys.setrecursionlimit(10**6)
    def F(n):
        if n == 5:
            return 1
        else:
            return 2 * n + 1 + F(n - 1)
    print(F(2024) - F(2022))


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):       
                if not(not((x <= y) >= w) and z):
                    print(w, x, y, z)
    

x = '1' * 2022
while '11111' in x or '555' in x:
    if '11111' in x:
        x = x.replace('11111', '55', 1)
    else:
        x = x.replace('555', '5', 1)
print(x)

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not((z <= y) <= x) or not(w):
                    print(w, x, y, z)

"""  черепаха """

from turtle import *

tracer(0)
r = 25

for i in range(10):
    fd(7)
    rt(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*r, y*r)
        dot(3, 'blue')

update()

count = 0
for x in range(1, 7):
    for y in range(1, 7):
        if -x / 3 ** 0.5 + 7 > y > x / 3 ** 0.5:
            count += 1
print(count)

print(81920/17920)

from itertools import product
cnt = 0
for x in product('АВОПР', repeat = 4):
    q = ''.join(x)
    cnt += 1
    if q[0] == 'П':
        print(cnt)
        break

x = '1' * 2022
while '11' in x or '555' in x:
    if '11' in x:
        x = x.replace('11', '555', 1)
    else:
        x = x.replace('555', '5', 1)
print(x)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not( ( (x <= y) <= w ) or (z <= (y and w ) ) ):
                    print(w, x, y, z)


import turtle 

turtle.color('black', 'red')

scale = 20
turtle.left(90)
turtle.begin_fill()
for _ in range(6):
    turtle.fd(scale * 19)
    turtle.right(60)
turtle.end_fill()
canvas = turtle.getcanvas()
dots = 0
for x in range(-200 * scale, 200 * scale, scale):
    for y in range(-200 * scale, 200 * scale, scale):
        i = canvas.find_overlapping(x, y, x, y)
        if len(i) == 1 and i[0] == 5:
            dots += 1

print(dots)

print(112*240)
print(35 * 2 ** 13)
i = 286720
k = 26880
print(i/k)
print(2**10)


from itertools import product

n = 1
for x in product('АВИКЛ', repeat = 6):
    s = ''.join(x)
    if s.count('А') <= 2 and s.count('В') == 2 and s.count('И') == 0:
        print(n)
        break
    n += 1

x = '1' * 65
while '11111' in x or '15' in x:
    if '11111' in x:
        x = x.replace('11111', '15', 1)
    else:
        x = x.replace('15', '1', 1)
print(x)

x = '1' * 2023
while ('211' in x) or ('112' in x, x.replace('11', '1', 1)):
    if('21' in x):
        x = x.replace('21', '12', 1)
    else:
        x = x.replace('12', '1', 1)
print(x)

import ipaddress

def ok(net):
    for ip in net:
        lt_sm = bin(int(ip))[2:18].count('1')
        rt_sm = bin(int(ip))[18:].count('1')
        if lt_sm > rt_sm:
            return False
    return True


for a in range(256):
    net = ipaddress.ip_network(f'64.129.{a}.10/255.255.252.0', False)
    if ok(net):
        print(a)


a = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1
cnt = 0
while a > 0:
    if a % 9 == 0:
        cnt += 1
    a //= 9

print(cnt)

b = [i / 10 for i in range(40, 180 + 1)]
c = [i / 10 for i in range(120, 400 + 1)]

def f(x):
    return (x not in a) <= ((x in b) == (x in c))

a = set()
for x in [i / 10 for i in range(10000)]:
    if not f(x):
        a.add(x)
print(sorted(a))


from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(6000)

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return n * (n - 1) + f(n - 1) + f(n - 2)

for i in range(2000):
    f(i)

print(f(2023) - f(2021) - 2 * f(2020) - f(2019))


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(((x <= y )<= z) or (w <= (y and z))):
                    print(w, x, y, z)


import turtle 

turtle.color('black', 'red')

scale = 20
turtle.left(90)
turtle.begin_fill()
for _ in range(21):
    turtle.fd(scale * 31)
    turtle.right(60)
turtle.end_fill()
canvas = turtle.getcanvas()
dots = 0
for x in range(-200 * scale, 200 * scale, scale):
    for y in range(-200 * scale, 200 * scale, scale):
        i = canvas.find_overlapping(x, y, x, y)
        if len(i) == 1 and i[0] == 20:
            dots += 1

print(dots)

from itertools import product
n = 1
for x in product('АЛМОС', repeat = 5):
    s = ''.join(x)
    if s.count('А') == 1 and s.count('М') == 2 and s.count('Л') == 0:
        print(n)
        break
    n += 1


x = '1' * 50
while '11111' in x or '15' in x:
    if '11111':
        x = x.replace('11111', '15', 1)
        x = x.replace('15', '1', 1)
print(x)

import ipaddress

def ok(net):
    for ip in net:
        lt_sm = bin(int(ip))[2:18].count('1')
        rt_sm = bin(int(ip))[18:].count('1')
        if lt_sm > rt_sm:
            return False
    return True


for a in range(256):
    net = ipaddress.ip_network(f'32.0.{a}.5/255.255.240.0', False)
    if ok(net):
        print(a)


n = 2897 // 10 % 10
print(n)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not((x == z) and not(w <= (y and z)))):
                    print(w, x, y, z)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(( (x <= y ) and (y <= w) ) or (z == (x or y) )):
                    print(w, x, y, z)


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((not(z) == y) <= ((w and not(x)) == (y and x))):
                    print(w, x, y, z)


from itertools import product
words = list(product('НРТУ', repeat=4))
print(words[214])

a = 'ABCD'
c = 1
for l1 in a:
    for l2 in a:
        for l3 in a:
            for l4 in a:
                w = l1 + l2 + l3 + l4
                if c == 98:
                    print(w)
                c += 1


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not((x == y) or (x == w)) or z or not(y <= w)):
                    print(w, x, y, z)


print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not((x ==y) or (x == z))) or w or (not( y <= z))
                if f == 0:
                    print(w, x, y, z)


all_r = []
for n in range(1, 1000):
    r = bin(n)[2:]
    s = ''
    for i in r:
        s += i + i
    r = int(s, 2)
    if r > 32:
        all_r.append(r)
print(min(all_r))




from turtle import *

left(90)
pendown()
speed(0)
k = 10000

begin_fill()
right(180)
forward(2 * k)
right(90)
forward(80 * k)
right(90)
forward(2 * k)
for i in range(8):
    circle(-5 * k, 180)
    right(180)

end_fill()
cnt = 0
c = getcanvas()
for x in range(-200, 200):
    for y in range(-200, 200):
        if c.find_overlapping(x * k, y * k, x * k, y * k) == (5, ):
            cnt += 1
print(cnt)


a = 240 * 1024 * 8
b = 360 * 512
print(a/b)


s = '1' + 70 * '2'
while '12' in s or '1' in s:
    if '12' in s:
        s = s.replace('12', '221', 1)
    else:
        if '1' in s:
            s = s.replace('1', '2', 1)
print(s.count('2'))


from ipaddress import *
for mask in range(0,  32 + 1):
    net = ip_network(f'42.118.219.133/{mask}', 0)
    if net[0] == ip_address('42.118.216.0'):
        print(mask)



for x in '0123456789ABCDEFGHIJK':
    x_podoshel = True
    for y in '0123456789ABCDEFGHIJK':
        a = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        if a % 18 != 0:
            x_podoshel = False
            break
    if x_podoshel == True:
        y = 5
        a = int(f'12{y}{x}9', 21) + int(f'36{y}99', 21)
        print(x , a // 18)



for a in range(0, 1000):
    if all(((x < a) and (y < a) and (x * y > 601)) == False for x in range(1, 1000) for y in range(1, 1000)):
        print(a)


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2 and n % 2 == 0:
        return 2 + f(n - 1)
    if n > 2 and n % 2 != 0:
        return 3 * n + f(n - 2)
print(f(43))

data = [int(line)for line in open('17.txt')]
pari = []
for i in range(len(data) - 1):
    if data[i] > 700 or data [i + 1] > 700:
        pari.append(data(i) ** 2 + data[i + 1]**2)
print(len(pari), max(pari))


print('w x y z')
for w in range(2):
 for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x and not(y) or (y == z) or not(w)):
                print(w, x, y, z)

     


def f(N):
    bN = bin(N)[2:]
    if N % 3 == 0:
        bN += bN [-3:]
    else:
        r = bin((N % 3) * 3)[2:]
        bN += r
    return int(bN, 2)

for N in range(1 ,300):
    R = f(N)
    if R > 151:
        print(R)


print('x y')
for x in range(2):
    for y in range(2):
        if not(not(x) or y):
            print(x, y)

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not(y <= (x == w)) and (z <= x))
                print(w, x, y, z)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(x and not(y) or (y == z) or not(w)):
                    print(w, x, y, z)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((w == z) or (x and not(y)) or w):
                    print(w, x, y, z)
                    
print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not( ( (x <= y) and (z or w) ) <= ( (x ==  w) or (y and not(z)) ) ):
                    print(w, x, y, z)
        
n = []
for i in range(0 , 100):
    chislo = int(bin(i)[2:])
    if chislo % 2 == 0:
        new_chislo = int('11' + str(chislo) + '0', 2)
    else:
        new_chislo = int('11' + str(chislo) + '11', 2)
    if new_chislo > 52:
        n.append(new_chislo)
n.sort()
print(n[0])


mass = []
for i in range(0, 100):
    chislo = str(bin(i)[2:])
    promezutoc1 = chislo + str(sum([int(i) for i in chislo]) % 2)
    new_chislo = int(promezutoc1 + str(sum([int(i) for i in promezutoc1]) % 2), 2)
    if new_chislo > 77:
        mass.append(i)
mass.sort()
print(mass[0])

x = 1024 * 1536
c = 2 * 2 ** 23
print(c/x)
print(2**4)

import itertools,sys
k = 0
for i in itertools.product('ГЕПАРД', repeat = 5):
    n = ''.join(i)
    if n.count('Г') == 1 and n[0] != 'А' and n[4] != 'E':
        k += 1
    print(i, k)


import itertools, sys
k = 0
for i in itertools.product('ГЕПАРД',  repeat = 5):
    n = ''.join(i)
    if n.count('Г') == 1 and n[0] != 'А' and n[4] != 'Е':
        k += 1
    print(i, k)

import itertools
s = 'ЕЛМУР'
n = 0
for i1, i2, i3, i4 in itertools.product(s, repeat = 4):
    n = n + 1
    if i1 == 'Л':
        print(n,i1,i2,i3,i4)
        break



import itertools
k = 0
for i1,i2,i3,i4,i5,i6,i7,i8 in itertools.permutations('Светлана', r = 8):
    t = i1+i2+i3+i4+i5+i6+i7+i8
    if ('аа' in t) == 0:
        k += 1
print(k/2)

import itertools,sys
k = 0
for i in itertools.product('АПРСУ', repeat =5):
    k += 1
    if i1 == 'У' and ('аа' in i):
        print(k)



for n in range(1, 1000000):
    r = bin(n)[2:]
    c = r.count('1')
    c1 = r.count('0')
    c2 = c + c1
    r1 = bin(c2)[2:]
    if n % 2 == 0:
        f = r + r1
    else:
        f = '1' + r + '00'
    r = int(f, 2)
    if  r > 215:
        print(n)
        break

for n in range(1, 1000000):
    r = bin(n)[2:]
    c = r.count('1')
    c1 = r.count('0')
    c2 = c + c1
    r1 = bin(c2)[2:]
    if n % 2 == 0:
        f =  '' + r + '10'
    else:
        f = '1' + r + '01'
    r = int(f, 2)
    if r > 516:
        print(n)
        break

for n in range(1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '10'
    else:
        r = '1' + r + '01'
    if int(r, 2) > 516:
        print(n)
        break


a = []
for n in range(10000):
    r = bin(n)[2:]
    r = str(r)
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else: 
        r = '11' + r[2:] + '1'
    r = int(r, 2)
    if r > 16:
       a.append(n)
print(min(a))

a = []
for n in range(1, 10000):
    r = bin(n)[2:]
    r = str(r)
    if n % 2 == 0:
        r = r + '00'
    else:
        r = r + '11'
    r = int(r, 2)
    if r < 134:
        a.append(n)
print(max(a))




for n in range(1, 10000000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '00'
    else:
        r += '01'
    s = int(r, 2)
    if s > 77:
        print(s)
        break


for n in range(100000, 1, -1):
    r = bin(n)[2:]
    if n % 5 == 0:
        r += bin(5)[2:]
    else:
        r += '1'
    if int(r, 2) % 7 == 0:
        r += bin(7)[2:]
    else: 
        r += '1'
    if int(r, 2) < 1855663:
        print(n)
        break

print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not ((x <= y) or not(w <= z)):
                    print(w, x, y, z)

print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if not (((a == b) or not(c == d)) or (not(c) >= b)):
                    print(a, b, c, d)



print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = not(y <= (x == w)) and (z <= x) == 1
                print(w, x, y, z)
                    

x = '8' * 70
while ('2222' in x) or ('8888' in x):
    if ('2222' in x):
        x = x.replace('2222', '88', 1)
    else:
        x = x.replace('8888', '22', 1)
print(x)

oc = '192.168.32.160' 
if oc > 256:
    print("Only 256 or less")
else:
    binary = bin(oc)[2:]

oc = int(input("Enter oc1: "))
if oc > 256:
    print("Only 256 or less")
else:
    binary = bin(oc)[2:]

print(bin(215)[2:])


for x in range(0, 23):
    a = 1*23**0 + x*23**1 + 1*23**2 + x*23**3 + 1*23**4 + x*23**5 + 1*23**6 + x*23**7 + 1*23**8
    b = 4*23**0 + 2*23**1 + x*23**2 + 0*23**3 + 2*23**4
    c = 5*23**0 + 3*23**1 + 2*23**2 + x*23**3 + 1*23**4
    if(a+b+c)% 22 == 0:
        print(x, (a+b+c)//22)

for x in range(0, 23):
    a = 1*23**0+1*23**1+0*23**2+1*23**3+4*23**4+3*23**5+x*23**6+x*23**7+2*23**8
    b = 4*23**0+x*23**1+0*23**2+2*23**3+2*23**4
    c = 6*23**0+x*23**1+0*23**2+1*23**3+1*23**4
    if(a+b+c)%22 == 0:
        print(x, (a+b+c)//22)

for x in range(0, 25):
    a = 5*25**0 + x*25**1 + 4*25**2 + x*25**3 + 3*25**4 + x*25**5 + 2*25**6 + x*25**7 + 1*25**8
    b = 4*25**0 + 2*25**1 + 0*25**2 + x*25**3 + 2*25**4
    c = 9*25**0 + 9*25**1 + 0*25**2 + x*25**3 + 1*25**4
    if(a+b+c)%24 == 0:
        print(x, (a+b+c)//24)

for x in range(0, 19):
    a = 1*19**0 + x*19**1 + 0*19**2 + x*19**3 + 1*19**4 + x*19**5 + 2*19**6 + x*19**7 + 3*19**8
    b = 4*19**0 + 2*19**1 + 0*19**2 + 2*19**3 + x*19**4
    c = 7*19**0 + 7*19**1 + 0*19**2 + x*19**3 + 1*19**4
    if(a+b+c)%18 == 0:
        print(x, (a+b+c)//18)


for x in range(0, 17):
    a = 9*17**0 + x*17**1 + 5*17**2 + 3*17**3 + 1*17**4
    b = 1*17**0 + 3*17**1 + 5*17**2 + x*17**3 + 9*17**4
    if(a+b)%9 == 0:
        print(x, (a+b)//9)


for x in range(0, 15):
    a = 7*15**0+x*15**1+5*15**2+3*15**3+1*15**4
    b = 1*15**0+3*15**1+5*15**2+x*15**3+7*15**4
    if(a+b)%14 == 0:
        print(x, (a+b)//14)



x = 4 * 25**20222 - 2 * 5**2000 + 125 ** 1011 - 3 * 5**100 - 600
s = ''
while x > 0:
    s = s +str(x%5)
    x = x // 5
print(s.count('4'))

x = 4**2022 - 6*4**522 + 5*64**510 - 3*2**330 - 100
s = ''
while x > 0:
    s = s + str(x%8)
    x = x // 8
print(s.count('7'))


x = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210 - 255
s = ''
while x > 0:
    s = s + str(x%8)
    x = x // 8
print(s.count('0'))

x = 243**540 - 6*9**530 + 21*3**511 - 3*3**70 - 200
s = ''
while x > 0:
    s = s + str(x%9)
    x = x // 9
print(s.count('А'))

x = 1331 ** 650 - 55 * 121 **610 + 77 * 11 ** 510 - 3 * 11 **100 - 221
s = 0
while x:
    if x % 11 == 10:
        s += 1
    x //= 11
print(s) 


x = 4 ** 2022 - 2 * 4 **1111 + 16 ** 600 + 192
s = ''
while x > 0:
    s = s + str(x%4)
    x = x // 4
print(s.count('3'))

x = 2 * 3**2022 + 5 * 3 **1800 + 3 ** 1001 + 4 * 3 ** 1000 + 3
s = ''
while x > 0:
    s = s + str(x%9)
    x = x // 9
s = s[::-1]
print(s.count('0'))

x = 3 ** 2020 - 3**1020 + 9 ** 800 - 81
s = ''
while x > 0:
    s = s + str(x%3)
    x = x // 3
print(s.count('2'))

x = 4**700 + 4 ** 100 - 16 **100 -64
s = ''
while x > 0:
    s = s + str(x%4)
    x = x // 4
print(s.count('3'))

x = 49 ** 6 * 7 ** 19 - 7 ** 9 - 21
s = ''
while x > 0:
    s = s + str(x%7)
    x = x // 7
print(s.count('6'))

x = 3**333+3**22-9**111-8
s = ''
while x > 0:
    s = s + str(x%3)
    x = x // 3
print(s.count('2'))

for n in range(4, 10000):
    s = '1' + '2' * n
    while ('12' in s) or ('2222' in s) or ('2222' in s):
        if ('12' in s):
            s = s.replace('12', '33', 1)
        if ('2222' in s):
            s = s.replace('2222', '1', 1)
        if ('3322' in s):
            s = s.replace('3322', '21', 1)
    summ = sum(list(map(int, s)))
    if summ == 218:
        print(n)
        break

for n in range(4, 10000):
    s = '1' + '2' * n
    while ('12' in s) or ('5522' in s) or ('2222' in s):
        if('12' in s):
            s = s.replace('12', '55', 1)
        if('2222' in s):
            s = s.replace('2222', '1', 1)
        if('5522' in s):
            s = s.replace('5522', '21', 1)
        summ = sum(list(map(int, s)))
        if summ == 142:
            print(n)
            break

for n in range(5, 10000):
    s = '4' + '1' * n
    while ('31' in s) or ('411' in s) or ('1111' in s):
        if('31' in s):
            s = s.replace('31', '1', 1)
        if('411' in s):
            s = s.replace('411', '13', 1)
        if('1111' in s):
            s = s.replace('1111', '4', 1)
        summ = sum(list(map(int, s)))
        if summ == 36:
            print(n)
            break

x = '22' + '1' * 2023 + '22'
while ('211' in x) or ('112' in x):
    x = x.replace('11', '1', 1)
    if('21' in x):
        x = x.replace('21', '12', 1)
    else:
        x = x.replace('12', '1', 1)
print(x)

x = '22' + '1' * 2050 + '22'
while('211' in x) or ('112' in x):
    x = x.replace('11', '1', 1)
    if('12' in x):
        x = x.replace('21', '12', 1)
    else:
        x = x.replace('12', '1', 1)
print(x)

x = '22' + '1' * 2024 + '22'
while('2111' in x) or ('1112' in x):
    x = x.replace('111', '1', 1)
    if('21' in x):
        x = x.replace('21', '12', 1)
    else:
        x = x.replace('12', '1', 1)
print(x)

x = '22' + '1' * 2023
while('2111' in x) or ('1112' in x):
    x = x.replace('111', '1', 1)
    if('21' in x):
        x = x.replace('21', '12', 1)
    else:
        x = x.replace('12', '1', 1)
print(x)

x = '1' * 91
while('2222' in x) or ('1111' in x):
    if('2222' in x):
        x = x.replace('2222', '11', 1)
    else:
        x = x.replace('1111', '22', 1)
print(x)


def simple(x):
    for i in range(2, int(x ** 0.5)+ 1):
        if x%i == 0:
            return 0
    return 1
for n in range(50):
    a = '>' + '0' * 15 + '1'*n + '2' * 15
    while ('>0' in a) or ('>1' in a) or ('>2' in a):
        if('>0' in a):
            a = a.replace('>0', '22>', 1)
        if('>1' in a):
            a = a.replace('>1', '2>', 1)
        if('>2' in a):
            a = a.replace('>2', '1>', 1)
    x = sum(int(i) for i in a[:-1])
    if simple(x) == 1:
        print(n)
        break

def simple(x):
    for i in range(2, int(x*0,5)+1):
        if x%i == 0:
            return 0
        return 1
for n in range(50):
    a = '>' + '0' * 15 + '1' * n + '2' * 15
    while ('>0' in a) or ('>1' in a) or ('>2' in a):
        if ('>0' in a):
            a = a.replace('>0', '22>', 1)
        if ('>1' in a):
            a = a.replace('>1', '2>', 1)
        if ('>2' in a): 
            a = a.replace('>2', '1>', 1)
        x = sum(int(i) for i in a[:-1])
        if simple(x) == 1:
            print(n)
            break

def simple(x):
    for i in range(2, int(x ** 0.5)+1):
        if x%i == 0:
            return 0
    return 1
for n in range(50):
    a = '>' + '1' * 11 + '2' * n + '3' * 11
    while('>1' in a) or ('>2' in a) or ('>3' in a):
        if ('>1' in a):
            a = a.replace('>1', '222>', 1)
        if('>2' in a):
            a = a.replace('>2', '3>', 1)
        if('>3' in a):
            a = a.replace('>3', '1>', 1)
    x = sum(int(i) for i in a[:-1])
    if simple(x) == 1:
        print(n)
        break


def simple(x):
    for i in range(2, int(x ** 0.5)+1):
        if x%i == 0:
            return 0
    return 1
for n in range(50):
    a = '>' + '1' * 16 + '2' * n + '3' * 16
    while('>1' in a) or ('>2' in a) or ('>3' in a):
        if('>1' in a):
            a = a.replace('>1', '1>', 1)
        if('>2' in a):
            a = a.replace('>2', '>3', 1)
        if('>3' in a):
            a = a.replace('>3', '>1', 1)
    x = sum(int(i) for i in a[:-1])
    if simple(x) == 1:
        print(n)
        break


def simple(x):
    for i in range(2, int(x ** 0.5)+1):
        if x%i == 0:
            return 0 
    return 1
for n in range(100):
    a = '>' + '1' * 23 + '2' * n + '3' * 25
    while('>1' in a) or ('>2' in a) or ('>3' in a):
        if('>1' in a):
            a = a.replace('>1', '1>', 1)
        if('>2' in a):
            a = a.replace('>2', '>3', 1)
        if('>3' in a):
            a = a.replace('>3', '>11', 1)
    x = sum(int(i) for i in a[:-1])
    if simple(x) == 1:
        print(n)
        break


x = '1' + '5' * 25
while('15' in x) or ('1' in x):
    if ('15' in x):
        x = x.replace('15', '5551', 1)
    else:
        x = x.replace('1', '5', 1)
print(x.count('5'))


for n in range(1000):
    x = '4' + '1' * n
    while('31' in x) or ('411' in x) or ('1111' in x):
        if('31' in x):
            x = x.replace('31', '1', 1)
        if('411' in x):
            x = x.replace('411', '13', 1)
        if('1111' in x):
            x = x.replace('1111', '4', 1)
    summ = 0
    for i in x:
        summ += int(i)
        if summ == 34:
            print(n)

for n in range(1000):
    x = '4' + '1' * n
    while ('31' in x) or ('411' in x) or ('1111' in x):
        if('31' in x):
            x = x.replace('31', '1', 1)
        if('411' in x):
            x = x.replace('411', '13', 1)
        if('1111' in x):
            x = x.replace('1111', '4', 1)
    summ = 0
    for i in x:
        summ += int(i)
        if summ == 36:
            print(n)

x = '0' + '1' * 12 + '2' * 15 + '3' * 17
while ('01' in x) or ('02' in x) or ('03' in x):
    x = x.replace('01', '20', 1)
    x = x.replace('02', '120', 1)
    x = x.replace('03', '302', 1)
print(x.count('1'))

from ipaddress import ip_network
network = ip_network('142.108.56.118/255.255.255.240', False)
count = 0
for ip in network:
    ip_bin = bin(int(ip))[2:]
    if ip_bin[:16].count('1') < ip_bin[16:].count('1'):
        count += 1
print(count)

from ipaddress import ip_network
network = ip_network('116.29.170.89/255.255.255.224', False)
count = 0
for ip in network:
    ip_bin = bin(int(ip))[2:]
    if ip_bin[:15].count('1') > ip_bin[16:].count('1'):
        count += 1
print(count)

from ipaddress import ip_network
network = ip_network('23.140.159.160/255.255.252.0', False)
count = 0
for ip in network:
    ip_bin = bin(int(ip))[2:]
    if ip_bin[:16].count('1') > ip_bin[13:].count('1'):
        count += 1
print(count)

from ipaddress import ip_network
network = ip_network('253.112.169.12/255.255.254.0', False)
count = 0
for ip in network:
    ip_bin = bin(int(ip))[2:]
    if ip_bin[:15].count('1') <= ip_bin[16:].count('1'):
        count += 1
print(count)

def f4(n):
    s = ''
    while n > 0:
        s = str(n %4) + s
        n = n // 4
    return s
for n in  range (1, 260):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[-2:]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4, 4)
    if  r < 261:
        print(n)
    
def f4(n):
    s = ''
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s 
for n in range(1, 368):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[-2:]
    else:
        ost = f4((n%4)*2)
        n4 = n4 + ost
    r = int(n4, 4)
    if r < 1024:
        print(n)


def f4(n):
    s = ''
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s 
for n in range(1, 1024):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[-2:]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4, 4)
    if r >= 1025:
        print(n)
        break

def f4(n):
    s = ''
    while n > 0:
        s = str(n%4) + s
        n = n // 4
    return s
for n in range(1, 1087):
    n4 = f4(n)
    if n % 4 == 0:
        n4 = n4 + n4[-2:]
    else:
        ost = f4((n%4) * 2)
        n4 = n4 + ost
    r = int(n4, 4)
    if r >= 1088:
        print(n)
        break

for x in range(1, 1000):
    n = bin(x)[2:]
    if x%2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1')%2 == 0:
        n = '11' + n[2:]
    else:
        n = '10' + n[2:]
    if int(n, 2) >= 26:
        print(x)
        break

for x in range(1, 10000):
    n = bin(x)[2:]
    if x%2 == 0:
        n = n + '0'
    else:
        n = n + '1'
    if n.count('1')%3 == 0:
        n = '11' + n[2:]
    else:
        n = '10' + n[2:]
    if int(n, 2) <= 37:
        print(x)


a =[]
for x in range(1, 100000):
    n = bin(x)[2:]
    if x % 2 == 0:
        n = '1' + n + '0'
    else: 
        n = '11' + n + '11'
    r = int(n, 2)
    if r > 52:
        a.append(r)
print(min(a))

a = []
for x in range(1, 1000000):
    n = bin(x)[2:]
    if x % 2 == 0:
        n = n + '01'
    else:
        n = '1' + n + '1'
    r = int(n, 2)
    if r > 156:
        a.append(r)
print(min(a))

a = []
for x in range(1, 1000000):
    n = bin(x)[2:]
    if x % 2 == 0:
        n = n + '10'
    else:
        n = '01' + n + '1'
    r = int(n, 2)
    if r > 516:
        a.append(r)
print(min(a))
        
for x in range(1, 10000):
    n = bin(x)[2:]
    if len(n) % 2 == 0:
         n = n[:len(n)//2] + '1' + n[len(n)//2:]
    if int(n, 2) <= 26:
        print(x)

for x in range(100, 1000):
    n = str(x)
    x1 = int(n[0]) * int(n[1]) * int(n[2])
    x2 = int(n[0]) + int(n[1]) + int(n[2])
    res = str(max(x1, x2)) + str(min(x1, x2))
    if res == '33621':
        print(x)

for x in range(100, 1000):
    n = str(x)
    x1 = int(n[0]) * int(n[1]) * int(n[2])
    x2 = int(n[0]) + int(n[1]) + int(n[2])
    res = str(max(x1, x2)) + str(min(x1, x2))
    if res == '24019':
        print(x)

a = []
for x in range(1, 10000):
    n = bin(x - x%4)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n,2) > 56:
        a.append(int(n, 2))
print(min(a))


a = []
for x in range(1, 100000):
    n = bin(x - x%4)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n, 2) > 100:
        a.append(int(n, 2))
print(min(a))

for x in range(1, 100000):
    n = bin(x - x%4)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n, 2) < 64:
        print(x)


for x in range(1, 100000):
    n = bin(x - x%4)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n, 2) < 47:
        print(x)

a = []
for x in range(1, 10000):
    n = bin(x - x%8 + x%2)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n, 2) > 90:
        a.append(int(n, 2))
print(min(a))

a = []
for x in range(1, 10000):
    n = bin(x - x%8 + x%2)[2:]
    n = n + str(n.count('1')%2)
    n = n + str(n.count('1')%2)
    if int(n, 2) > 97:
        a.append(int(n, 2))
print(min(a))

a = []
for x in range(1,1000):
    n = bin(x)[2:]
    n = n.replace('0', '-').replace('1', '*').replace('-', '00').replace('*', '11')
    if int(n,2) > 32:
        a.append(int(n,2))
print(min(a))

a = []
for x in range(1, 10000):
    n = bin(x)[2:]
    n = n.replace('0', '-').replace('1', '*').replace('-', '00').replace('*', '11')
    if int(n,2) > 63:
        a.append(int(n, 2))
print(min(a))

import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 5
    if n > 1:
        return 2*n+1+f(n-1)
print(f(2024)-f(2022))

import sys
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return 3
    if n > 1:
        return 3*n+2*f(n-1)
print(f(2024)-4*f(2022))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n-1)+ f(n-1) + f(n-2)
print(f(2024)-f(2022)-2*f(2021)-f(2020))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return f (n-2) * (n+1)
print(f(8))

 

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n*(n-1)+f(n-1)-f(n-2)
print(f(2024) + f(2020) - f(2019))



def f(n):
    if n < 3:
        return n
    if n % 2 == 0 and n > 2:
        return 2*(n-1)+f(n-1)+2
    if n % 2 != 0 and n > 2:
        return 2*(n+1)+f(n-2)-5
print(f(32))

def f(n): 
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) * (n+2)
print(f(5))

def f(n):
    if n < 3:
        return n
    if n % 2 == 0 and n > 2:
        return 3*(n-1)+f(n-1)+5
    if n % 2 != 0 and n > 2:
        return 3*(n+1)+f(n-2)-2
print(f(35))

def f(n):
    if n < 3:
        return 1
    if n % 2 != 0 and n > 2:
        return f(n-1)+f(n-2)
    if n % 2 == 0 and n > 2:
        return sum(f(i) for i in range(1,n))
print(f(24)) 


import sys
from functools import lru_cache
sys.setrecursionlimit(3000)
@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n % 2 != 0 and n > 2:
        return f(n-1)-f(n-2)
    if n % 2 == 0 and n > 2:
        return sum(f(i) for i in range(1,n))
print(f(39))

def f(n):
    if n <= 1:
        return 1
    if n % 2 != 0 and n > 1:
        return 5*n+f(n-1)+f(2)
    if n % 2 == 0 and n > 1:
        return 3 *f(n-1)
print(f(23))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 2 + f(n-1)
print(f(2023)-f(2019))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 !=0:
        return 3+f(n-1)*f(n-2)-f(n-1)-f(n-2)
    if n > 1 and n % 2 == 0:
        return 2*f(n-1)
print(f(12))

import sys 
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n*(n-1)+f(n-1)+f(n+2)
print(f(2023)-f(2021)-2*f(2020)-f(2019))


import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 3 * f(n-1)
    if n > 1 and n % 2 != 0:
        return 2 + 2 * f(n-2)
print(f(23))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    if n > 1 and n %2 != 0:
        return 2 * f(n-1) + f(n-2)
print(f(20))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    if n > 1 and n % 2 != 0:
        return f(n-1) + 2 * f(n-2)
print(f(19))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print(f(446)/f(443))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return  2 
    if n > 2:
        return n * (n-1) * f(n-1)
print(f(123)/f(120))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 + f(n-1)
    if n > 2 and n % 2 != 0:
        return 3 * n + f(n-2)
print(f(43))


import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return 3 + f(n-1)
    if n > 2 and n % 2 != 0:
        return 2 * n + f(n-2)
print(f(42))

from itertools import product
count = 0
k = 0
for i in product('АВИОРТФ', repeat = 6):
    a = ''.join(i)
    count += 1
    if a.count('Р') == 2 and a[0] != 'О' and (count % 2 == 0): 
        k += 1
print(k)

from itertools import product
count = 0 
k = 0
for i in product('АЕИКЛПР', repeat=6):
    a = ''.join(i)
    count += 1
    if a.count('И') >= 2 and a[0] != 'К' and (count % 2 == 0):
        k += 1
print(k)

from itertools import product
count = 0 
k = 0
for i in product('АГИЛМНОФ', repeat = 5):
    a = ''.join(i)
    count += 1
    if a.count('О') <= 1 and a[0] != 'Н' and (count % 2 == 1):
        k += 1
print(k)

from itertools import product
count = 0
k = 0
for i in product('АГЕИЛНРT', repeat = 5):
    a = ''.join(i)
    count += 1
    if (a.count('Н') == 1 or a.count('Н') == 2) and a[0] != 'T' and (count % 2 == 1):
        k += 1
print(k)


from itertools import product
cnt = 0
for x in product('01234567', repeat = 5):
    q = ''.join(x)
    if q.count('4') == 2 and '14' not in q and '41' not in q\
                            and '34' not in q and '43' not in q\
                            and '54' not in q and '45' not in q\
                            and '74' not in q and '47' not in q\
                            and '94' not in q and '49' not in q\
                            and q[0] != '0':
                            cnt += 1
print(cnt)

from itertools import product
cnt = 0
for i in product('КНОРСЯ', repeat = 6):
    a = ''.join(i)
    cnt += 1
    if a.count('Я') == 2 and a.count('К') <= 3:
        print(cnt)
        break

from itertools import product
cnt = 0
for i in product('АКРУ', repeat = 5):
    a= ''.join(i)
    cnt += 1
    if a.count('У') == 1:
        print(cnt)
        break

from itertools import product
cnt = 0 
for i in product('АЗЛОПЬ', repeat = 6):
    a = ''.join(i)
    cnt += 1
    if a.count('Ь') <= 1 and a.count('А') == 1 and a.count('З') <= 2:
        print(cnt)
        break
       
from itertools import product
cnt = 0 
for i in product('АМОТ', repeat = 4):
    a = ''.join(i)
    cnt += 1
    if a[0] == 'О':
        print(cnt)
        break

from itertools import product
cnt = 0 
for i in product('АВОПР', repeat = 4):
    a = ''.join(i)
    cnt += 1
    if a[0] == 'П':
        print(cnt)
        break


from itertools import product
cnt = 0 
for i in product('АЛМОС', repeat = 5):
    a = ''.join(i)
    cnt += 1
    if a.count('А') <= 1 and a.count('М') == 2 and a.count('Л') == 0:
        print(cnt)
        break

from itertools import product
cnt = 0
for i in product('АПРСУ', repeat = 5):
    a = ''.join(i)
    cnt += 1
    if a.count('А') <= 1 and a.count('У') == 0:
        print(cnt)
        break


from itertools import product
cnt = 0
for x in product('0123', repeat=3):
    a = ''.join(x)
    if int(a[0]) > int(a[1]) > int(a[2]):
        cnt += 1
print(cnt)


from itertools import product
cnt = 0
for x in product('01234', repeat=3):
    a = ''.join(x)
    if int(a[0]) > int(a[1]) > int(a[2]):
        cnt += 1
print(cnt)


from itertools import product
cnt = 0
for x in product('0123', repeat=3):
    a = ''.join(x)
    if int(a[0]) >= int(a[1]) >= int(a[2]):
        cnt += 1
print(cnt-1)

from itertools import product
cnt = 0
for x in product('01234', repeat=3):
    a = ''.join(x)
    if int(a[0]) >= int(a[1]) >= int(a[2]):
        cnt += 1
print(cnt-1)

from itertools import product
cnt = 0
for x in product('01234567', repeat=4):
    a = ''.join(x)
    if a[0] != '0':
        if (a[0] == a[1] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]) or \
            (a[1] == a[2] and a[2] != a[0] and a[2] != a[3] and a[0] != a[3]) or \
            (a[2] == a[3] and a[2] != a[1] and a[2] != a[0] and a[0] != a[1]):
                cnt += 1
print(cnt)


from itertools import product
cnt = 0
for x in product('0123456789', repeat=4):
    a = ''.join(x)
    if a[0] != '0':
        if (a[0] == a[1] and a[1] != a[2] and a[1] != a[3] and a[2] != a[3]) or \
            (a[1] == a[2] and a[2] != a[0] and a[2] != a[3] and a[0] != a[3]) or \
            (a[2] == a[3] and a[2] != a[1] and a[2] != a[0] and a[0] != a[1]):
                cnt += 1
print(cnt)


a = 1024 * 1024
c = 4
print(a*c)

print()

a = 4194304
b = 8 
c = 1024
print(a/c)
print(4096/b)

a = 2100*1024*8
c = 1000*1600
print(a/c)

a = 2 ** 9
print(a)

print('a b c')
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
                if not(c and not(b) or c and a):
                    print(a, b, c)

x = '7' * 200
while ('7777' in x) or ('33333' in x):
    if('33333' in x):
        x = x.replace('33333', '777', 1)
    else:
        x = x.replace('777', '33', 1)
print(x.count('3'))

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not(z <= w) or x or not(y)):
                    print(w, x, y, z)



""" 14 вариант  """
import ipaddress

def ok(net):
    for ip in net:
        bin_ip = bin(int(ip))[2:].zfill(32)
        lt = bin_ip[:16].count('1')
        rt = bin_ip[16:].count('1')
        if lt < rt:
            return False
    return True

for a in range(256):
    net = ipaddress.ip_network(f"126.255.{a}.100/255.255.240.0", False)
    if ok(net):
        print(a)

def f(x):
    return (x % a != 0) <= ((x % 26 == 0) <= ( x % 169 != 0))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)


f = open('files/17/17var14.txt')
nums = [int(i) for i in f]
cnt = 0
mn = float('inf')
for a, b in zip(nums, nums[1:]):
    if abs(a) % 10 == 7 and abs(b) % 10 == 7:
        cnt += 1
        mn = min(mn, abs(a-b))
print(cnt,mn)


def f(s1, s2, m, func=all):
    if s1 + s2 >= 118: 
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s1 * 2, s2, m-1), f(s1, s2 * 2, m-1), f(s1 + 2, s2, m-1), f(s1, s2 + 2, m-1)]
    return any(h) if (m-1) % 2 == 0 else func(h)
print([s for s in range(1, 114) if f(3, s, 2, any)])
print([s for s in range(1, 114) if f(3, s, 3) and not(f(3, s, 1))])
print([s for s in range(1, 114) if f(3, s, 4) and not(f(3, s, 2))])

for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if s.count('2')*2 + s.count('1')*1 + s.count('5')*5 == 64:
        print(n)


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((x and not(z)) or (y == z) or not(w)):
                    print(w, x, y, z)

x = '8' * 45
while ('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '88', 1)
    else:
        x = x.replace('8888', '11', 1)
print(x)

for x in range(0, 27):
    a = 4*27**0 + 2*27**1 + x*27**2 + 3*27**3 + 2*27**4 + 1*27**5
    b = 8*27**0 + 7*27**1 + 1*27**2 + x*27**3
    if(a+b)% 26 == 0:
        print(x, (a+b)//26)


import sys
from functools import lru_cache
sys.setrecursionlimit(3000)
@lru_cache(None)
def f(n):
    if n >= 7:
        return 1
    if n < 7:
        return n + 2 + f(n-1)
print(f(2024)-f(2020))

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if  not((x <= y) or not(w <= z)):
                    print(w, x, y, z)

a = 768 * 600
b = 450 * 8 * 1024
print(b/a)
c = 2 ** 8
print(c)

for n in range(61, 1000):
    x = '1' * n
    while '111' in x:
        x = x.replace('111', '2', 1)
        x = x.replace('222', '11', 1)
    if x == '221':
        print(n)
        break


def f(n):
    if n == 0:
        return 0
    if n % 3 == 0 and n > 0:
        return n + f(n-3)
    if n % 3 > 0:
        return n + f(n-(n % 3))
print(f(22))

def win1(a):
    return a + 1 >= 177 or a * 2 >= 177
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a*2)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a*2))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a*2) or win2(a*2))
for s in range(1, 177):
    if lose2(s):
        print(s)

def win1(a):
    return a + 1 >= 38 or a * 3 >= 38
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a*3)
for s in range(1, 38):
    if lose1(s):
        print(s)


def win1(a):
    return a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a+4) and win1(a*5)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a+4) or (lose1(a*5)))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a+4) or win2(a+4)) and (win1(a*5) or win2(a*5))
for s in range(1, 68):
    if lose2(s):
        print(s)

    

""" 19-21 задание недуачный ход """

from functools import lru_cache
def step(a, b):
    return (a + 2, b), (a, b  + 2), (a * 2, b), (a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 142: return 'END'
    elif any(x + y >= 142 for x, y in step(a, b)): return 'WIN1'
    elif all(game(x, y) == 'WIN1' for x, y in step(a, b)): return 'LOSE1'
    elif any(game(x, y) == 'LOSE1' for x, y in step(a, b)): return 'WIN2'
    elif all(game(x, y) == 'WIN1' or game(x, y) == 'WIN2' for x, y in step(a, b)): return 'LOSE12'

for s in range(1, 138+1):
    if game(2, s) == 'LOSE12':
        print(s)




print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((x or y) <= (z and w)) and (x <= w):
                    print(w, x, y, z)

def f(x, h):
    if  h == 3 and x >= 118:
        return 1
    elif h == 3 and x < 118:
        return 0
    elif x >= 118 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x+1, h+1) or f(x + 2, h + 1) or f(x * 2, h + 1)
        else:
            return f(x+1, h+1) or f(x + 2, h + 1) or f(x * 2, h + 1)
for x in range(1, 118):
    if f(x, 1) == 1:
        print(x)
        break

"""  15 вариант 20-21 задание """

from functools import lru_cache

def step(a, b):
    return (a + 2, b), (a * 2,b),(a,b + 2),(a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 122: return 'END'
    elif any(x + y >= 122 for x, y in step(a, b)): return 'WIN1'
    elif all(game(x, y) == 'WIN1' for x, y in step(a, b)): return 'LOSE1'
    elif any(game(x, y) == 'LOSE1' for x, y in step(a, b)): return 'WIN2'
    elif all(game(x, y) == 'WIN1' or game(x, y) == 'WIN2'  for x, y in step(a, b)): return 'LOSE2'

for s in range(1, 1000):
    if game(3, s) == 'LOSE2':
        print(s)


"""  16 вариант 20-21 задание """
from functools import lru_cache

def step(a, b):
    return (a + 2, b),(a * 3, b),(a,b + 2),(a,b * 3)
@lru_cache(None)
def game(a, b):
    if a + b >= 136: return 'END'
    elif any(x + y >= 136 for x, y in step(a, b)): return 'WIN1'
    elif all (game(x, y) == 'WIN1' for x, y in step(a, b)): return 'LOSE1'
    elif any (game(x, y) == 'LOSE1' for x, y in step(a, b)): return 'WIN2'
    elif all (game(x, y) == 'WIN1' or game(x, y) == 'WIN2' for x, y in step(a, b)): return 'LOSE2'
for s in range(1 , 10000):
    if game(3, s) == 'LOSE2':
        print(s)


"""  17 вариант 20-21 задание """
from functools import lru_cache
def step(a, b):
    return(a + 1, b),(a * 2,b),(a,b + 1),(a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 101: return 'END'
    elif any(x + y >= 101 for x, y in step(a,b)): return 'WIN1'
    elif all(game(x, y) == 'WIN1' for x, y in step(a,b)): return 'LOSE1'
    elif any(game(x, y) == 'LOSE1' for x, y in step(a,b)): return 'WIN2'
    elif all(game(x, y) == 'WIN1' or game(x, y) == 'WIN2'  for x, y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
    if game(7 , s) == 'WIN2':
        print(s)
"""  21 задание(поставить в for)
     if game(7, s) == 'LOSE2':
        print(s)
 """

from functools import lru_cache
def step(a, b):
    return (a + 1, b),(a * 2,b),(a,b + 1),(a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 59: return 'END'
    elif any(x + y >= 59 for x, y in step(a, b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x, y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x, y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x, y in step(a,b)): return 'LOSE2'
for s in range(1, 100):
    if game(5, s) == 'LOSE2':
        print(s)

"""  18 вариант 20-21 задание """
from functools import lru_cache
def step(a, b):
    return (a + 1,b),(a * 2,b),(a,b + 1),(a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 123: return 'END'
    elif any(x + y >= 123 for x, y in step(a, b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x, y in step(a, b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x, y in step(a, b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x, y in step(a, b)): return 'LOSE2'
for s in range(1 , 1000000):
    if game(9, s) == 'LOSE2':
        print(s)

"""  19 вариант 20-21 задание """
from functools import lru_cache
def step(a, b):
    return (a + 1,b),(a * 2,b),(a,b + 1),(a,b * 2)
@lru_cache(None)
def game(a, b):
    if a + b >= 144: return 'END'
    elif any(x + y >= 144 for x, y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x, y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x, y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 143):
    if game(1, s) == 'LOSE2':
        print(s)


from functools import lru_cache
def step(a,b):
  return (a+3,b),(a*2,b),(a,b+3),(a,b*2)
@lru_cache(None)
def game(a,b):
  if a + b >= 143: return 'END'
  elif any (x+y >= 143 for x, y in step(a,b)): return 'WIN1'
  elif all(game(x, y) == 'WIN1' for x, y in step(a,b)): return 'LOSE1'
  elif any (game(x, y) == 'LOSE1' for x, y in step(a,b)): return 'WIN2'
  elif all (game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x, y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
  if game(16, s) == 'WIN2':
    print(s)


from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b + 1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 143: return 'END'
    elif any (x + y >= 143 for x,y in step(a,b)): return 'WIN1'
    elif all (game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any (game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all (game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
    if game(16, s) == 'LOSE2':
        print(s)




"""  5-6 вариант 13 задание """
from ipaddress import *
network = ip_network('252.67.33.87/255.252.0.0', 0)
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin[16:].count('1') > 2 * ip_bin[:16].count('1'):
        cnt += 1
print(cnt)

from ipaddress import *
network = ip_network('122.159.136.144/255.255.255.248', 0)
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4  != 0:
        cnt += 1
print(cnt)

from ipaddress import *
network = ip_network('249.0.33.87/255.252.0.0', 0)
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin[16:].count('1') > 2 * ip_bin[:16].count('1'):
        cnt += 1
print(cnt)


from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4 != 0:
        cnt += 1
print(cnt)

"""7-8 вариант 13 задание """
from ipaddress import *

for mask in range(16, 25):
    network = ip_network(f'255.211.33.160/{mask}', 0)
    A_podoshel = True
    for ip in network:
        ip_bin = f'{ip:b}'
        if (ip_bin[:16].count('1') >= ip_bin[16:].count('1')) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(mask)
        break
print(int('11110000', 2))
    
from ipaddress import *
for mask in range(16, 25):
    network = ip_network(f'191.239.130.3/{mask}', 0)
    A_podoshel = True
    for ip in network:
        ip_bin = f'{ip:b}'
        if(ip_bin[:16].count('1') >= ip_bin[16:].count('1')) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(mask)
        break
print(int('11110000', 2))






print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not(not(x <= y) or (y == w) or y):
                    print(w, x, y, z)

x = '8' * 82
while ('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '8', 1)
    else:
        x = x.replace('8888', '11', 1)
print(x)

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print((f(2024)-f(2023))/f(2022))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return (f(n-1)-f(n-2)) * n
print(f(8))

x = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 ** 2022 - 2024
s = 0
while x:
    if x % 27 > 9:
        s += 1
    x //=27
print(s)

file = open('files/17/17var01.txt')
data = []
for line in file:
    data.append(int(line))
M = 10 ** 40
for elem in data:
    if str(elem)[-2:] == '25':
        M = min(M, elem)
print(M)

troiki = []
dv = lambda x:  10 <= x <= 99
for i in range(len(data) - 2):
    if dv(data[i]) + dv(data[i + 1]) + dv(data[i + 2]) == 1 and (data[i] + data[i + 1] + data[i + 2] < M):
        troiki.append(data[i] + data[i + 1] + data[i + 2])
print(len(troiki), max(troiki))




print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((w <= (y == z)) and (y == (z <= x))) == 1:
                    print(w, x, y, z)

x = 16 ** 18 * 4 ** 10 - 4 ** 6 - 16
s =''
while x > 0:
    s += str(x%4)
    x //= 4
print(s.count('3'))

x = '1' * 7 + '2' * 7
while ('111' in x) or ('222' in x):
    if ('111' in x):
        x = x.replace('111', '2', 1)
    if ('222' in x):
        x = x.replace('222', '1', 1)
print(x)

print(2**6)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0 ,2):
                if (not(x <= z) or (y == w) or y) == 0:
                    print(w, x, y, z)


for x in range(1, 10000):
    r = bin(x)[2:]
    if x % 2 == 0:
        r += '10'
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > 516:
        print(x)
        break

from itertools import product
count = 0
k = 0
for i in product('АВИОРТФ', repeat=6):
    a = ''.join(i)
    count += 1
    if a.count('Р')==2 and a[0]!='О' and (count % 2 == 0):
        k += 1
print(k)

    
from itertools import product
cnt = 0
for i in product('АПРСУ', repeat = 5):
    a = ''.join(i)
    if a.count('У') == 1 and a.count('АА') not in ''.join(i):
        cnt += 1
print(cnt)

x = '8' * 82
while('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '8', 1)
    else:
        x = x.replace('8888', '11', 1)
print(x) 

x = 2 * 729 ** 2014 + 2 * 243 ** 2016 - 2 * 81 ** 2018 + 2 * 27 ** 2020 - 2 * 9 * 2022 - 2024
cnt = 0
while x > 0:
    if x % 27 > 9:
        cnt += 1
    x = x // 27
print(cnt)


import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)
print((f(2024)-f(2023))/f(2022))






a = 1024 * 1024
b = 1024 * 1024 * 8
print(b/a)

from itertools import product
cnt = 0
for i in product('АПРСУ', repeat = 5):
    a = ''.join(i)
    if a.count('У') == 1 and a.count('АА') not in ''.join(i):
        cnt += 1
print(cnt)

from itertools import product
cnt = 0 
for i in product('АБЗИ', repeat = 4):
    a = ''.join(i)
    if a.count('ИЗБА'):
        cnt += 1
print(cnt)

""" 25 задание """
from fnmatch import *
for x in range(31007, 10**10, 31007):
    if fnmatch(str(x), '1*34?5?9'):
        print(x, x // 31007)

from fnmatch import *
for x in range(12007, 10**10, 12007):
    if fnmatch(str(x), '9*?001?1'):
        print(x, x // 12007)

from fnmatch import *
for x in range(5171, 10**8, 5171):
    if fnmatch(str(x), '?19*8?3'):
        print(x, x // 5171)

from fnmatch import *
for x in range(3377, 10**8, 3377):
    if fnmatch(str(x), '?79?8*3'):
        print(x, x // 3377)

from fnmatch import *
for x in range(149, 10**8, 149):
    if fnmatch(str(x), '11*223'):
        print(x, x // 149)

from fnmatch import *
for x in range(123, 10**8, 123):
    if fnmatch(str(x), '32*823'):
        print(x, x // 123)

from fnmatch import *
for x in range(2049, 10**9, 2049):
    if fnmatch(str(x), '32*21?4'):
        print(x, x // 2049)

from fnmatch import *
for x in range(2079, 10**9, 2079):
    if fnmatch(str(x), '33*21?7'):
        print(x, x // 2079)

from fnmatch import * 
for i in range(2024, 10**10, 2024):
  if fnmatch(str(i), '10*2024?'):
    print(i, i//2024)
    
def M(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return n // i - i
    return 0
k = 0
N = 860001
while k < 5:
    m = M(N)
    if m % 100 == 18:
        k += 1
        print(N, m)
    N += 1

def M(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return n // i - i
    return 0
k = 0
N = 860001
while k < 5:
    m = M(N)
    if m % 100 == 30:
        k += 1
        print(N, m)
    N += 1

def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0

c = 0
i = 800000
while c < 5:
    m = M(i)
    if m and m % 17 == 0:
        print(i, m)
        c += 1
    i -= 1

def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0 
c = 0
i = 800000
while c < 5:
    m = M(i)
    if m and m % 23 == 0:
        print(i, m)
        c += 1
    i -= 1

def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0
c = 0
i = 850001
while c < 6:
    m = M(i)
    if m and m % 7 == 0:
        print(i, m)
        c += 1
    i += 1 


def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0
c = 0
i = 850001
while c < 6:
    m = M(i)
    if m and m % 5 == 0:
        print(i, m)
        c += 1
    i += 1 


def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0
c = 0
i = 850001
while c < 6:
    m = M(i)
    if m and m % 3 == 0:
        print(i, m)
        c += 1
    i += 1 

def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0
c = 0
i = 850001
while c < 6:
    m = M(i)
    if m and m % 11 == 0:
        print(i, m)
        c += 1
    i += 1 

def M(n):
    divisors = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    if divisors:
        return max(divisors)-min(divisors)
    else:
        return 0
c = 0
i = 850001
while c < 6:
    m = M(i)
    if m and m % 13 == 0:
        print(i, m)
        c += 1
    i += 1 


import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n >= 7:
        return 1
    if n < 7:
        return n + 2 + f(n-1)
print(f(2024)-f(2020))


for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '01'
    else:
        r = '1' + r + '1'
    s = int(r, 2)
    if s > 156:
        print(n)
        break

f = open('9.txt')
for s in f:
    a = list(map(int, s.split()))


import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2*n + f(n-1)
    if n % 2 != 0 and n > 1:
        return 3 * f(n-2)
print(f(18))

from ipaddress import *
network = ip_network('64.192.192.0/255.255.240.0')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 2 == 0:
        cnt += 1
print(cnt)


from itertools import *
a = '012345679ABCDEF'
cnt = 0
for x in product(a, repeat=3):
    if x[0] != 0:
        if len(set(x)) == len(x):
            if int(x[0],16) % 2 != int(x[1],16) % 2 and int(x[1],16) % 2 != int(x[2],16) % 2:                 
                cnt+=1 
print(cnt)

def prime(n):
    if (n == 2) or (n == 3):
        return True
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(400, 451):
    if prime(i):
        print(i)


x = '8' * 70 
while ('2222' in x) or ('8888' in x):
    if ('2222' in x):
        x = x.replace('2222', '88', 1)
    else:
        x = x.replace('8888', '22', 1)
print(x)

x = '>' + '1' * 10 + '2' * 20 + '3' * 30
while ('>1' in x) or ('>2' in x) or ('>3' in x):
    if ('>1' in x):
        x = x.replace('>1', '22>', 1)
    if ('>2' in x):
        x = x.replace('>2', '2>', 1)
    if ('>3' in x):
        x = x.replace('>3', '1>', 1)
print(x.count('1') + x.count('2') * 2)


x = '>' + '0' * 39 + '1' * n + '2' * 39
while ('>1' in x) or ('>2' in x) or ('>0'):
    if ('>1' in x):
        x = x.replace('>1', '22>', 1)
    if ('>2' in x):
        x = x.replace('>2', '2>', 1)
    if ('>0' in x):
        x = x.replace('>0', '1>', 1)
print(x.count('1') + x.count('2') * 2)


x = '1' * 100
while ('111' in x) or ('88888' in x):
    if ('111' in x):
        x = x.replace('111', '88', 1)
    else:
        x = x.replace('88888', '8', 1)
print(x)

x = '2' * 52
while ('222' in x) or ('000' in x):
    if ('000' in x):
        x = x.replace('000', '2', 1)
    else:
        x = x.replace('222', '02', 1)
print(x)

x = '8' * 86
while ('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '8', 1)
    else:
        x = x.replace('8888', '11', 1)
print(x)

import sys
sys.setrecursionlimit(5000)
from functools import *
@lru_cache (None)
def f(n):
    if n == 1:
        return 1 
    if n % 2 == 0:
        return n + f(n-1)
    if n % 2 != 0:
        return 2 * f(n-2)
print(f(26))

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((w or x or y) <= ((y or z) and x or y and (w or z))):
                    print(w, x, y, z)

from fnmatch import *
for i in range(2025, 10**8, 2025):
    if fnmatch(str(i), '12*34?5'):
        print(i, i // 2025)

def f(a, b):
    if a > b or a == 11 or a == 17:
        return 0
    if a == b:
        return 1
    return f(a + 1, b) + f(a+4,b) + f(a*2,b)
print(f(3, 24))

def f(a, b):
    if a > b or a == 18:
        return 0
    if a == b:
        return 1
    return f(a + 1,b) + f(a+4,b) + f(a*2,b)
print(f(4, 11) * f(11, 28))


def f(a, b):
    if a > b or a == 6 or a == 17: 
        return 0
    if a == b:
        return 1
    return f(a + 2,b) + f(a+3,b) + f(a*5,b)
print(f(1, 31))


def f(a,b):
    if a > b or a == 21:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+3,b) + f(a*5,b)
print(f(1, 6) * f(6,35))

def f(a,b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a-1,b) + f(a // 2,b)

print(f(50, 20) * f(20, 1))


def f(a, b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-1,b) + f(a // 2,b)
print(f(60, 10) * f(10, 2))

def f(a, b):
    if a < b or a == 10:
        return 0 
    if a == b:
        return 1
    return f(a-1,b) + f(a // 2,b)
print(f(50, 20) * f(20, 1))

def f(a,b):
    if a < b or a == 4:
        return 0
    if a == b:
        return 1
    return f(a-1,b) + f(a // 2,b)
print(f(60, 20) * f(20, 1))


def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+7,b)
print(f(5, 49))


def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+7,b)
print(f(7,51))


def f(a,b):
    if a > b:
        return 0 
    if a == b:
        return 1
    return f(a+2,b) + f(a+10,b)
print(f(5,71))

def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-1,b) + f(a // 2,b)
print(f(30, 10) * f(10, 1))

def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-1,b) + f(a // 2,b)
print(f(31, 12) * f(12, 2))


def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1 
    return f(a-1,b) + f(a // 3,b)
print(f(33, 9) * f(9, 1))

def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1 
    return f(a-1,b) + f(a // 3,b)
print(f(37, 10) * f(10, 2))

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1 
    return f(a+2,b) + f(a * 2,b) + f(a *3,b)
print(f(1, 6) * f(6, 24))

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1 
    return f(a+2,b) + f(a * 2,b) + f(a *3,b)
print(f(2, 6) * f(6, 28))

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1 
    return f(a+3,b) + f(a+4,b) + f(a *3,b)
print(f(1, 7) * f(7, 30))

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1 
    return f(a+5,b) + f(a+4,b) + f(a *3,b)
print(f(2, 6) * f(6, 30))


def f(a, b):
  if a > b:
    return 0
  if a == b:
    return 1
  return f(a+1,b) + f(a*2,b)
print(f(3,16) * f(3, 6) * f(6, 16) * f(3, 12) * f(12, 16))

from fnmatch import *
for x in range(2024, 10**10, 2024):
  if fnmatch(str(x), '10*2024?'):
    print(x, x // 2024)


""" 1 ВАРИАНТ """
""" ОТВЕТЫ:
1. 45 +  
2. zxwy + 
3. 820  + 
4. 1111 + 
5. 33 + 
6. 253 257 -
7. 150 +
8. 24 + 
9.(не делал) - 
10. 10  + 
11. 300 + 
12. 888 + 
13. 76.158.125.208 (2, 1, 4, 3) +
14. 38 +
15.(не делал) - 
16. 577 +
17.(не делал) - 
18.(не делал) - 
19. 17 +
20. 13 16 + 
21. 12 +
22.(не делал) - 
23. 11 + 
24.(не делал) - 
25. 123451758 3336534 
    123454718 3336614 +
    123458788 3336724
26.(не делал) - 
27.(не делал) - 
 """
from fnmatch import *
for i in range(37, 10**9, 37):
    if fnmatch(str(i), '12345?7?8'):
        print(i, i//37)


def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-2,b) + f(a-5,b)
print(f(17, 1))

x = 9 ** 11 * 3 ** 20 - 3 ** 9 - 27
s = ''
while x > 0:
    s = s + str(x%3)
    x //= 3
print(s.count('2'))

x = '1' * 84
while ('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '888', 1)
    else:
        x = x.replace('8888', '8', 1)
print(x)

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n-2) - f(n-1)
    if n > 2 and n % 2 != 0:
        return 2 * f(n-1) - f(n-2)
print(f(19))

for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '10'
    if n % 2 != 0:
        r = '11' + r + '1'
    s = int(r, 2)
    if s > 441:
        print(n)
        break

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not(not(y) or z) or (x == w) or x) == 0:
                    print(w, x, y, z)


def win1(a):
    return a + 1 >= 35 or a + 4 >= 35 or a * 2 >= 35
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a+4) and win1(a*2)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a+4) or lose1(a*2))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a+4) or win2(a+4)) and (win1(a*2) or win2(a*2))
for s in range(1, 35):
    if lose2(s):
        print(s)
 

print('k l m n')
for k in range(0, 2):
    for l in range(0, 2):
        for m in range(0, 2):
            for n in range(0, 2):
                if (not(k <= m) and (k or n) or (l <= n)) == 0:
                    print(k, l, m, n)

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4 == 0:
        cnt += 1
print(cnt)

x = 343 ** 515 - 6 * 49 ** 520 + 5 * 49 ** 510 - 3 * 7 ** 530 - 550
s = ''
while x > 0:
    s = s + str(x%7)
    x //= 7
print(s.count('6'))

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + 3 + f(n+3)
print(f(2018)-f(2022))


from fnmatch import *
for n in range(3226, 10**8, 3226):
    if fnmatch(str(n), '3?99?7*8'):
        print(n, n//3226)

def f(a, b):
    if a > b or a == 13:
        return 0
    if a == b:
        return 1
    return f(a + 1,b) + f(a + 2,b) + f(a * 3,b)
print(f(3, 8) * f(8,18))

for n in range(2, 100000):
    r = bin(n)[2:]
    r = str(r)
    r += r[-2]
    r += r[1]
    s = int(r, 2)
    if s > 100:
        print(n)
        break


x = 3 * 5103 ** 2020 + 3 * 729 ** 2021 - 2 * 343 ** 2022 + 27 ** 2023 - 4 * 7 ** 2024 - 2029
cnt = 0
while x != 0:
    if x%27 > 9:
        cnt += 1
    x //= 27
print(cnt)

for x in range(0, 27):
    a = 4*27**0 + 2*27**1 + x*27**2 + 3*27**3 + 2*27**4 + 1*27**5
    b = 8*27**0 + 7*27**1 + x*27**2 + 5*27**3 + 3*27**4 + 1*27**5
    if(a+b)%26 == 0:
        print(x, (a+b)//26)

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4  == 0:
        cnt += 1
print(cnt)

x = '8' * 45
while ('1111' in x) or ('8888' in x):
    if ('1111' in x):
        x = x.replace('1111', '88', 1)
    else:
        x = x.replace('8888', '11', 1)
print(x)
    

a = 2764*1793*13*148
b = 18349566
print(a/b)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((x and not(z)) or (y == z) or not(w)) == 0:
                    print(w, x, y, z)


for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '01'
    if n % 2 != 0:
        r = '1' + r + '1'
    s = int(r, 2)
    if s > 156:
        print(n)
        break


from itertools import product
count = 0
k = 0
for i in product('АВИОРТФ', repeat=6):
    a = ''.join(i)
    count += 1
    if a.count('Р')==2 and a[0]!='О' and (count % 2 == 0):
        k += 1
print(k)

from itertools import product
cnt = 0
for i in product ('АПРСУ', repeat =5):
    a = ''.join(i)
    if a.count('У') <= 1  and 'АА' not in a:
        cnt += 1
print(cnt)

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + f(n-1)
print(f(2024)-f(2020))


from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x, x//2024)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a*2,b)
print(f(4,8)* f(8,10) * f(10,15))

def f(a, b):
    if a >  b or a == 16:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+3,b) + f(a**2,b)
print(f(2,25) * f(25, 42))


def win1(a):
    return a + 1 >= 177 or a * 2 >= 177
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a*2)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a*2))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a*2) or win2(a*2))
for s in range(1, 177):
    if lose2(s):
        print(s)

i = 13
a = 202752/1024
print(a)

def win1(a):
    return a + 1 >= 129 or a * 2 >= 129
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a*2)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a*2))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a*2) or win2(a*2))
for s in range(1, 129):
    if lose2(s):
        print(s)

from functools import lru_cache
def step(a,b):
  return (a+3,b),(a*2,b),(a,b+3),(a,b*2)
@lru_cache(None)
def game(a,b):
  if a + b >= 143: return 'END'
  elif any (x+y >= 143 for x, y in step(a,b)): return 'WIN1'
  elif all(game(x, y) == 'WIN1' for x, y in step(a,b)): return 'LOSE1'
  elif any (game(x, y) == 'LOSE1' for x, y in step(a,b)): return 'WIN2'
  elif all (game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x, y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
  if game(16, s) == 'LOSE2':
    print(s)



from functools import lru_cache
def step(a, b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 123: return 'END'
    elif any(x+y >= 123 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 100000):
    if game(13, s) == 'LOSE2':
        print(s)

import sys
sys.setrecursionlimit(5000)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + f(n-1)
print(f(2024)-f(2020))

for A in range(-1000, 1000):
    if all(((4 * x + y < A) or (x < y) or (22 <= x)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(-1000, 1000):
    if all(((x ** 2 + y ** 2 > 128) or (y < -x + A)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((x < 4) or (x >= 20) or (y >= 3*x + A) or (y < 100)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(-1000, 1000):
    if all(((x >= 20) or (y >= 40) or (y <= x + A) or (y >= 3*x - A)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((x >= A) or (y >= A) or (x * y <= 200)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((x >= A) or (y >= A) or (x * y <= 270)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((x < A) and (y < A) and (x*y > 601)) == False for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((x < A) and (y < A) and (x * y > 1200)) == False for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(-1000, 1000):
    cnt = 0
    for x in range(0, 1000):
        if ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(-1000, 1000):
    cnt = 0
    for x in range(0, 1000):
        if ((x%20 == 0) <= (x%11 != 0)) or (x + A >= 300):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if (x%A != 0) <= ((x%18 == 0) <= (x%81 != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if (x%A != 0) <= ((x%26 == 0) <= (x%169 != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if (x%A != 0) <= ((x%24 == 0) <= (96%x != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break


for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if (x%A != 0) <= ((x%54 == 0) <= (162%x != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break

def t(a,b,c):
    return (a+b > c) and (a+c > b) and (b+c > a)
def f(x,A):
    return not((t(x,11,18) == (not(max(x,5) > 15))) or t(x,A,5))
for a in range(1, 1000):
    if all(f(x,a) for x in range(1, 1000)):
        print(a)


b = list(range(10, 15 + 1))
c = list(range(20, 27 + 1))
a = []
for x in range(1, 100):
    if (((x in b) or (x in c)) <= (x in a)) == False:
        a.append(x)
print(a)

for A in range(-1000, 1000):
    cnt = 0 
    for x in range(1, 1000):
        if ((x%3 != 0) and (x%5 == 0)) or (A >= 42 - x):
            cnt += 1
    if cnt == 999:
        print(A)
        break


x = 15 * 2401 ** 1500 - 10 * 343 ** 1200 + 40 * 49 ** 1000 - 35 * 7 ** 850 - 4805
cnt  = 0
while x != 0:
    if x%49 > 9:
        cnt += 1
    x //= 49
print(cnt)

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n/2 * f(-1)
    if n > 1 and n % 2 != 0:
        return n-1/2 * f(n-1)
print(f(2024)-f(2022)/f(2021))

x = '2' + '9' * 100
while ('19' in x) or ('299' in x) or ('3999' in x):
    x = x.replace('19', '2', 1)
    x = x.replace('299', '3', 1)
    x = x.replace('3999', '1', 1)
print(x)

x = 49 ** 7 + 7 ** 21 - 7
s = ''
while x > 0:
    s = s + str(x%7)
    x //= 7
print(s.count('6'))

for A in range(1000, -1000, -1):
    if all(((x + 3*y > A) or (y < 30) or (x < 30)) == True for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return 2 * f(n-1) + (n-2) * f(n-2)
print(f(6))

from fnmatch import *
for x in range(0, 10**10, 4891):
    if fnmatch(str(x), '1?7602*0'):
        print(x)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a+2,b)
print(f(1,11))

a = 128 * 320
b = 20 * 8 * 1024
print(b/a)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((x and not(y)) or (x == z) or not(w)) == 0:
                    print(w, x, y, z)


from functools import lru_cache
def step(a, b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 123: return 'END'
    elif any(x+y >= 123 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 100000):
    if game(13, s) == 'LOSE2':
        print(s)


from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 62: return 'END'
    elif any(x+y >= 62 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 10000):
    if game(10,s) == 'LOSE2':
        print(s)

print(430080/1024)

""" 12 задание """
for a in range(1, 50):
    for b in range(1, 50):
        for c in range(1, 50):
            x = '0' + a * '1' + b * '2' + c * '3' + '0'
            while '00' not in x:
                x = x.replace('01', '103', 1)
                x = x.replace('02', '2011', 1)
                x = x.replace('03', '130', 1)
            if x.count('1') == 92 and x.count('2') == 16 and x.count('3') == 52:
                print(c)


x = 15 * 2401 ** 1500 - 10 * 343 ** 1200 + 40 * 49 ** 1000 - 35 * 7 ** 850 - 4805
cnt = 0
while x != 0:
    if x%49 > 9:
        cnt += 1
    x //= 49
print(cnt)


for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if (x%A != 0) <= ((x%24 == 0) <= (96%x != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(1000, -1000, -1):
    cnt = 0
    for x in range(1, 1000):
        if not((x%3 != 0) and (x%5 == 0)) or (A >= 42 - x):
            cnt += 1
    if cnt == 999:
        print(A)
        break

def f(a,b):
    if a > b or a == 16:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+3,b) + f(a**2,b)
print(f(2,25) * f(25, 42))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return (n/2) * f(n-1)
    else:
        return (n-1/2) * f(n-1)
print((f(2024)-f(2022))/f(2021))


from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 62: return 'END'
    elif any(x+y >= 62 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 10000):
    if game(10,s) == 'LOSE2':
        print(s)

print(55/7)

from functools import lru_cache
def step(a,b):
    return (a+3,b),(a*2,b),(a*3,b),(a,b+3),(a,b*2),(a,b*3)
@lru_cache(None)
def game(a,b):
    if a + b >= 55: return 'END'
    elif any(x+y >= 55 for x, y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 100000):
    if game(s, s) == 'WIN':
        print(s)

def m(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + n // i
    return 0
cnt = 0
for i in range(424242 + 1, 100000000000):
    if m(i) % 2024  == 42:
        print(i, m(i))
        cnt += 1
    if cnt == 8: break

print('a b c d')
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if ((not(a) and not(b)) or (b == c) or d) == 0:
                    print(a, b, c, d)

x = '7' * 79
while ('7777' in x) or ('3333' in x):
    if ('3333' in x):
        x = x.replace('3333', '77', 1)
    else:
        x = x.replace('7777', '33', 1)
print(x)

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n <= 2:
        return 2
    if n >= 2:
        return 3 * f(n-1) - f(n-2)
print(f(6))

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a*2,b)
print(f(1, 12) * f(12, 25) * f(25, 40))

from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x//1917)

    print(15 + 15 + 15 + 15)

s = list('ФАВОРИТ')
s.sort()
i, cnt = 0, 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        i += 1
                        word = a + b + c + d + e + f
                        if i % 2 == 0 and a != 'О' and word.count('Р') == 2:
                            cnt += 1
print(cnt)

s = list('РЕПЛИКА')
s.sort()
i, cnt = 0, 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        i += 1
                        word = a + b + c + d + e + f
                        if i % 2 == 0 and a != 'К' and word.count('И') > 1:
                            cnt += 1
print(cnt)

s = list("ФЛАМИНГО")
s.sort()
i, cnt = 0, 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    i += 1
                    word = a + b + c + d + e
                    if i % 2 != 0 and a != 'Н' and word.count('О') < 2:
                        cnt += 1
print(cnt)

s = list('ИНТЕГРАЛ')
s.sort()
i, cnt = 0, 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    i += 1
                    word = a + b + c + d + e
                    if i % 2 != 0 and a != 'Т' and word.count('Н') in (1,2):
                        cnt += 1
print(cnt)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not(x <= w) or (y == z) or y) == 0:
                    print(w, x, y, z)

x = '0' + '1' * 12 + '2' * 15 + '3' * 17
while ('01' in x) or ('02' in x) or ('03' in x):
    x = x.replace('01', '20', 1)
    x = x.replace('02', '120', 1)
    x = x.replace('03', '302', 1)
print(x.count('1'))

x = 2 * 216 ** 8 + 4 * 36 ** 12 + 6 ** 15 - 1296
s = ''
while x > 0:
    s = s + str(x%6)
    x //= 6
print(s.count('0'))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n == 1:
        return 2 
    if n == 2:
        return 1
    if n > 2:
        return f(n-2) + f(n-1)
print(f(8))

b = list(range(10, 15 + 1))
c = list(range(20, 27 + 1))
a = []
for x in range(1, 100):
    if (((x in b) or (x in c)) <= (x in a)) == False:
        a.append(x)
print(a)

p = list(range(17, 46 + 1))
q = list(range(22, 57 + 1))
a = []
for x in range(1, 100):
    if ((x not in a ) <= (((x in p) and (x in q)) <= (x in a))) == False:
        a.append(x)
print(a)


from fnmatch import *
for x in range(4173, 10**10, 4173):
    if fnmatch(str(x), '1?7246*1'):
        print(x)

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1,b) + f(a * 2,b) + f(a * 2 + 1,b)
print(f(2, 16))

print(2574/8)
print(65536*322)
print(21102592/1024)


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not(x <= z) or (y == w) or y) == 0:
                    print(w, x, y, z)
    

for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10'
    if n % 2 != 0:
        r = '1' + r + '01'
    s = int(r, 2)
    if s > 516:
        print(n)
        break

from itertools import product
cnt = 0
for i in product('АПРСУ', repeat=5):
    a = ''.join(i)
    if a.count('У') <= 1 and 'АА' not in a:
        print(cnt)
        cnt += 1

print(132096/1024)

from itertools import product
cnt = 0
for i in product('АЁРТШ', repeat=5):
    a = ''.join(i)
    if a.count('А') <= 1 and 'ЁЁ' not in a:
        print(cnt)
        cnt += 1

from functools import lru_cache
def step(a, b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 123: return 'END'
    elif any(x+y >= 123 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 100000):
    if game(13, s) == 'LOSE2':
        print(s)


from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 132: return 'END'
    elif any(x + y >= 132 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
    if game(13, s) == 'WIN2':
        print(s)


from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '10*2024?'):
        print(x, x//2024)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a*2,b)
print(f(3,6) * f(6,12) * f(12, 16))

import sys
from functools import lru_cache
sys.setrecursionlimit(5000)
@lru_cache(None)
def f(n):
    if n <= 12:
        return 1
    if n > 12:
        return f(n-1)+n-2
print(f(2024)-f(2020))


x = '7' * 47
while ('2222' in x) or ('7777' in x):
    if ('2222' in x):
        x = x.replace('2222', '77', 1)
    else:
        x= x.replace('7777', '22', 1)
print(x)

p = list(range(17, 46 + 1))
q = list(range(22, 57 + 1))
a = []
for x in range(1, 100):
    if ((x not in a ) <= (((x in p) and (x in q)) <= (x in a))) == False:
        a.append(x)
print(a)

for x in range(0, 29):
    a = 8*29**0 + 5*29**1 + 1*29**2 + x*29**3 + 2*29**4 + 4*29**5
    b = 4*29**0 + 3*29**1 + 2*29**2 + x*29**3 + 6*29**4 + 1*29**5
    if (a+b)%28 == 0:
        print(x, (a+b)//28)

b = list(range(74,194 + 1))
c = list(range(152,223 + 1))
a = []
for x in range(1, 1000):
    if (((x not in a) and (x in b)) <= ((x in b) <= (x not in c))) == False:
        a.append(x)
print(a)

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4 == 0:
        cnt += 1
print(cnt)

from ipaddress import *
network = ip_network('114.179.203.128/255.255.255.192')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 3 == 0:
        cnt += 1
print(cnt)

a = 13 * 199 * 1079 * 1919 
b = 19999999
print(a/b)

for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '1'
    if n % 2 != 0:
        r += '10'
    s = int(r, 2)
    if s > 179:
        print(n)
        break

print('k l m n')
for k in range(0, 2):
    for l in range(0, 2):
        for m in range(0, 2):
            for n in range(0, 2):
                if (not(n) or k and not(m) or (l == m)) == 0:
                    print(k, l, m, n)

print(127/4)

from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 132: return 'END'
    elif any(x + y >= 132 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 1000):
    if game(13, s) == 'WIN2':
        print(s)


from functools import lru_cache
def step(a,b):
    return (a+3,b),(a*2,b),(a,b+3),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 143: return 'END'
    elif any(x + y >= 143 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2'  for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 10000):
    if game(16, s) == 'LOSE2':
        print(s)

from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 143: return 'END'
    elif any(x + y >= 143 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): 'WIN2'
    elif all(game(x,y) == 'WIN1'  or  game(x,y) == 'WIN2' for x,y in step(a,b)): 'LOSE2'
for s in range(1, 10000): 
    if game(16, s) == 'WIN2':
        print(s)

from fnmatch import *
for x in range(3013, 10**10, 3013):
    if fnmatch(str(x), '1?6961*5'):
        print(x)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a+3,b)
print(f(1,8) * f(8, 15))

import sys
sys.setrecursionlimit(5000)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return 2 * f(n-1) + f(n-2)
print(f(4))

x = 49**6 * 7**19 - 7**9 - 21
s = ''
while x > 0:
    s = s + str(x%7)
    x //= 7
print(s.count('6'))

x = '8' * 69
while ('3333' in x) or ('8888' in x):
    if ('3333' in x):
        x = x.replace('3333', '88', 1)
    else:
        x = x.replace('8888', '33', 1)
print(x)

from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 77: return 'END'
    elif any(x + y >= 77 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 100000):
    if game(8, s) == 'LOSE2':
        print(s)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (w <= x) and ((y <= z) == (x <= y)):
                    print(w, x, y, z)

print('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if ((x == y) or ((y or z) <= x)) == 0:
                print(x, y, z)

x = 4**511 + 2**511 - 511
s = ''
while x > 0:
    s = s + str(x%2)
    x //= 2
print(s.count('1'))


for A in range(1000, -1000, -1):
    if all(((x < A) and (y < A) and (x*y > 601)) == False for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break

for A in range(1000, -1000, -1):
    if all(((2*x + 3*y > 30) or (x + y <= A)) == False for x in range(0, 1000) for y in range(0, 1000)):
        print(A)
        break


for A in range(-1000, 1000):
    cnt = 0
    for x in range(0, 1000):
        if ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500):
            cnt += 1
    if cnt == 999:
        print(A)
        break

for A in range(0, 300):
    cnt = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (2*x + 3*y > 30) or (x + y <= A):
                cnt += 1
    if cnt == 90_000:
        print(A)
        break

import sys
sys.setrecursionlimit(5000)
from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 2:
        return f(n-1)+1
    if n > 0 and n % 3 < 2:
        return f((n-n%3)//3)
i = 0
while f(i) != 5:
    i += 1
print(i)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a+3,b)
print(f(1,9) * f(9, 17))

from fnmatch import *
for x in range(23, 10**9, 23):
    if fnmatch(str(x), '12345?7?8'):
        print(x, x//23)


from fnmatch import *
for x in range(2025, 10**8, 2025):
    if fnmatch(str(x), '12*34?5'):
        print(x, x//2025)

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b) + f(a+2,b) + f(a+5,b)
print(f(21,30))

x = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
s = ''
while x > 0:
    s = s + str(x%5)
    x //= 5
print(s.count('4'))

print(524288/1024)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((w or x or y) <= ((y or z) and x or y and (w or z))) == 0:
                    print(w, x, y, z)
                    
from itertools import product
words = list(product('АИМРЯ', repeat=4))
print(*words[211])

from itertools import product
words = list(product('КЛРТ', repeat=4))
print(*words[66])



def win1(a):
    return a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a+4) and win1(a*5)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a+4) or lose1(a*5))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a+4) or win2(a+4)) and (win1(a*5) or win2(a*5))
for s in range(1, 68):
    if lose2(s):
        print(s)


def win1(a):
    return a + 1 >=37 or a + 2 >= 37 or a * 3 >= 37
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a+2) and win1(a*3)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a+2) or lose1(a*3))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and  (win1(a+2) or win2(a+2)) and (win1(a*3) or win2(a*3))
for s in range(1, 37):
    if lose2(s):
        print(s)

b = list(range(74,194 + 1))
c = list(range(152,223 + 1))
a = []
for x in range(1, 1000):
    if (((x not in a) and (x in b)) <= ((x in b) <= (x not in c))) == False:
        a.append(x)
print(a)
       

P = list(range(1023,2148 + 1))
Q = list(range(1362,3898 + 1))
R = list(range(1813,2566 + 1))
a = []
for x in range(1, 10000):
    if ((((x not in Q) <= ((x in P) or (x in R)))) <= ((x not in a) <= (x not in Q))) == False:
        a.append(x)
print(a)

print(3898-1362)

import sys
sys.setrecursionlimit(5000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n + f(n-1)
k = 0
for n in range(1,101):
    if (f(2023)//f(n)) % 2 == 0:
        k += 1
print(k)

for i in range(100, 1000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    first = str(max(k1,k2))
    second = str(min(k1,k2))
    s1 = first + second
    if s1 == '1711':
        print(i)
        break

a = 128 * 320
b = 40 * 1024 * 8
print(b/a)
print(2**8)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (((y <= x) and (z or w)) <= ((x and not(w)) or (y == z))) == 0:
                    print(w, x, y, z)

x = 5 ** 36 + 5 ** 24 - 25
s = ''
while x > 0:
    s = s + str(x%5)
    x //= 5
print(s.count('4'))

def f(a,b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1,b)+f(a*2,b)+f(a*3,b)
print(f(1,13))

from fnmatch import *
for x in range(1987, 10**10, 1987):
    if fnmatch(str(x), '1*4022?9'):
        print(x)

print('w x y z')
for w in range(0,2):
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                if (((not x) <= y) and (y == (not z)) and (not w)) == 1:
                    print(w, x, y, z)


def to_4(x):
    s = ''
    while x > 0:
        s = s + str(x%4)
        x //= 4
    return s[::-1]

maxim = -10**10
for i in range(1, 10000):
    r = to_4(i)
    r += r[-1]

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                f = y and (x <= w) and ((not x) <= ((not w) == z))
                print(w, x, y, z, int(f))


from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '113?39*4'):
        print(x, x//2024)

def f(a,b):
    if a > b or a == 9 :
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+3,b) + f(a*2,b)
print(f(3,15) * f(15,25))


from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n*f(n-1)
for i in range(2024): f(i)
print((f(2024)+f(2023))/f(2022))

for A in range(-1000, 1000):
    cnt = 0
    for x in range(0,1000):
        if (x % A != 0) <= ((x%7 == 0) and (x%10 == 0) <= (x%4 != 0)):
            cnt += 1
    if cnt == 999:
        print(A)
        break

x = 7 * 729 ** 2024 - 15 * 243 ** 2022 + 7 * 81 ** 2020 - 15 * 27 ** 2010 + 2 * 9 ** 2000
s = 0
while x > 0:
    if 5 < (x%27) <= 13:
        s += 1
    x //= 27
print(s)

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.224')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 4 != 0:
        cnt += 1
print(cnt)

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.240')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 7 != 0:
        cnt += 1
print(cnt)

for n in range(4, 10000):
    x = '3' + n * '5'
    while ('25' in x) or ('355' in x) or ('555' in x):
        if ('25' in x):
            x = x.replace('25', '5', 1)
        if ('355' in x):
            x = x.replace('355', '52', 1)
        if ('555' in x):
            x = x.replace('555', '3', 1)
    if x.count('2') == 0 and x.count('3') == 0:
        print(n)
        break

from functools import lru_cache
def step(a,b):
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 59: return 'END'
    elif any(x + y >= 59 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 1000000):
    if game(5, s) == 'LOSE2':
        print(s)

for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '00'
    if n % 2 != 0:
        r += bin(r.count('1'))[2:]
    s = int(r,2)
    if s > 190:
        print(n)
        break

def f(a,b):
    if a > b or a == 9:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+3,b) + f(a*2,b)
print(f(3,15) * f(15, 25))

for n in range(4, 10000):
    x = '3' + n * '5'
    while ('25' in x) or ('355' in x) or ('555' in x):
        if ('25' in x):
            x = x.replace('25', '5', 1)
        if ('355' in x):
            x = x.replace('355', '52', 1)
        if ('555' in x):
            x = x.replace('555', '3', 1)
    if x.count('2') == 0 and x.count('3') == 0:
        print(n)
        break

from ipaddress import *
network = ip_network('105.224.200.224/255.255.255.240')
cnt = 0
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 7 != 0:
        cnt += 1
print(cnt)

x = 7 * 729 **2024 - 15 * 243**2022 + 7 * 81**2020 - 15 * 27 ** 2010 + 2 * 9**2000
s = 0
while x > 0:
    if 5 < (x%27) <= 13:
        s += 1
    x //= 27
print(s)

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)

for i in range(2024): f(i)
print((f(2024)+f(2023))/f(2022))

from itertools import product
cnt = 0
for i in product('АЁРТШ', repeat=5):
    a = ''.join(i)
    if a.count('А') <= 1 and 'ЁЁ' not in a:
        print(cnt)
        cnt += 1

from itertools import product
cnt = ans = 0
for i in product('АИНПТЦЯ', repeat=6):
    a = ''.join(i)
    cnt += 1
    if cnt%2 == 0 and a[0] != 'Н' and a.count('Я') == 2:
        ans += 1
print(ans)


print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not(y <= z) or (x <= w) or not(x)) == 0:
                    print(w, x, y, z)
            
a = 1024*960*160
b = 8192000 * 288
print(2**13)

from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '112?57*4') and sum(map(int , str(x))) % 2 != 0:
        print(x, x//2024)

from ipaddress import *
cnt = 0
network = ip_network('192.168.32.48/255.255.255.192', 0)
for ip in network:
    ip_bin = f'{ip:b}'
    if ip_bin.count('1') % 5 != 0:
        cnt += 1
print(cnt)

x = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81**169  - 2 * 9**107 + 3017
s = 0
while x > 0:
    if x % 27 <= 25:
        s += x % 27
    x //= 27
print(s)

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)

for i in range(2023): f(i)
print((f(2023)-f(2022))/f(2020))

print(2**11)

a = 1600 * 900 * 11 * 128
b = 2 * 60 * 60
print(a/b)

from itertools import product
cnt = 0
for i in product('АЗИМНОПРТ', repeat=5):
    cnt += 1
    if cnt % 2 == 0 and i[0] == 'Н' and i.count('Р') == 2:
        print(cnt)

from functools import lru_cache
def step(a,b):
    return (a+3,b),(a*2,b),(a,b+3),(a,b*2)
@lru_cache(None)
def game(a,b):
    if a + b >= 375: return 'END'
    elif any(x + y >= 375 for x,y in step(a,b)): return 'WIN1'
    elif all(game(x,y) == 'WIN1' for x,y in step(a,b)): return 'LOSE1'
    elif any(game(x,y) == 'LOSE1' for x,y in step(a,b)): return 'WIN2'
    elif all(game(x,y) == 'WIN1' or game(x,y) == 'WIN2' for x,y in step(a,b)): return 'LOSE2'
for s in range(1, 10000):
    if game(27,s) == 'LOSE2':
        print(s)

P = list(range(1023,2148 + 1))
Q = list(range(1362,3898 + 1))
R = list(range(1813,2566 + 1))
a = []
for x in range(1, 10000):
    if ((((x not in Q) <= ((x in P) or (x in R)))) <= ((x not in a) <= (x not in Q))) == False:
        a.append(x)
print(a)

print(3898-1362)

B = list(range(34,72+1))
C = list(range(32,61+1))
a = []
for x in range(1, 10000):
    if (((x in B) <= (x in a)) and ((x not in C) or (x in a))) == False:
        a.append(x)
print(a)
print(72-32)

print('w x y z')
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if (not(x <= z) or (y == w) or y) == 0:
                    print(w, x, y, z)

def f(a,b):
    if a < b or a == 20:
        return 0 
    if a == b:
        return 1
    return f(a-2,b) + f(a-3,b) + f(a // 5,b)
print(f(41,10) * f(10,5))

for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[3:]
    if n % 3 != 0:
        ost = bin(3 * (n%3))[2:]
        r += ost
    s = int(r, 2)
    if s < 100:
        print(n)


m = 0
for n in range(4, 1000):  
    x = '8' + n * '4'
    while ('11' in x) or ('444' in x) or ('8888' in x):
        if ('11' in x):
            x = x.replace('11', '4', 1)
        if ('444' in x):
            x = x.replace('444', '88', 1)
        if ('8888' in x):
            x = x.replace('8888', '1', 1)
    sm = 0
    for d in x:
        sm += int(d)
    m = max(m, sm)
print(m)

def win1(a):
    return a + 1 >= 68 or a + 4 >= 68 or a * 5 >= 68
def lose1(a):
    return win1(a) == False and win1(a+1) and win1(a+4) and win1(a*5)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a+4) or lose1(a*5))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win2(a+1)) and (win1(a+4) or win2(a+4)) and (win1(a*5) or win2(a*5))
for s in range(1, 68):
    if lose2(s):
        print(s)


def win1(a):
    return a + 1 >= 129 or a * 2 >= 129
def lose1(a):
    return win1(a) == False and win1(a+1) and win2(a*2)
def win2(a):
    return (not(win1(a))) and (not(lose1(a))) and (lose1(a+1) or lose1(a*2))
def lose2(a):
    return (not(win1(a))) and (not(lose1(a))) and (not(win2(a))) and (win1(a+1) or win1(a+1)) and (win1(a*2) or win2(a*2))
for s in range(1, 129):
    if lose2(s):
        print(s)


x = 3 * 289 ** 2024 + 81 * 49 ** 121 - 9 * 16 ** 81 - 6011
s = 0
while x > 0:
    if x % 31 <= 17:
        s += x % 31
    x //= 31
print(s)

from itertools import product
cnt = 0
for w in product('012345678', repeat=6):
    s = ''.join(w)
    if s[0] != 0 and s[0] not in '1357' and s[-1] != '2' and s[-1] != '9' and s.count('1') >= 2:
        cnt += 1
print(cnt)

def f(a,b):
    if a < b:
        return 0
    if a == b:
        return 1
    return f(a-2,b) + f(a//2,b)
print(f(30,14) * f(14,1))

a = []
for n in range(1, 100):
    r = bin(n)[2:]
    r = str(r)
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    s = int(r, 2)
    if s < 35:
        a.append(n)
print(max(a))

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n-1)
for i in range(2023): f(i)
print((f(2024) - 4 * f(2023))/f(2022))


for x in range(1, 2031):
    s = 3 ** 100 - x
    troich = ''
    while s > 0:
        troich += str(s%3)
        s //= 3
    if troich.count('0') == 2:
        print(x)
        break

from string import *
letters = digits + ascii_uppercase[:21]
for x in letters:
    s = int(f'123{x}AB3', 31) + int(f'3CE{x}321', 31)
    if s % 17 == 0:
        print(s//17)

def f(x):
    return (((x % 2 == 0) <= (x % 5 != 0)) or (x + a >= 70))
for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
print(2**18)
