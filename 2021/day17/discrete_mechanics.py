import numpy as  np
from sys import exit

#Example input : target area: x=20..30, y=-10..-5
#my input : target area: x=209..238, y=-86..-59

# Part 1
# For a positive v0y, you can easiy prove that ymax = (v0y*v0y+1)/2
# The important thing is that whenever you reach ymax, you then go down following the exact same consecutive altitudes you reached going up, in reverse. You arrive at y=0 with the same initial vertical velocity you had,+1
# The bottom of the target is at y=d. To reach y=d in 1 go, you need a velocity of d (in absolute value). But that's the velocity downward ! We have just said that the initial velocity corresponding to that downward velocity is actually d-1. Hence the result : (d-1)d/2
print(85*86//2)

# Part 2

def bound(ymax,y):
    return (-1+np.sqrt(1+8*(ymax-y)))/2

#Confine y region

#x1,x2 = (20,30)
#y1,y2 = (-10,-5)

x1,x2 = (209,238)
y1,y2 = (-86,-59)

v0ymax = abs(y1)-1 # for a positive v0y

#count = 0
#for v0y in range(1,v0ymax+1):
#    ymax = v0y*(v0y+1)//2
#    low = bound(ymax,y2)
#    high = int(bound(ymax,y1))
#    if low.is_integer(): #always integer if y2=0 !
#        low = int(low)
#    else:
#        low = int(low)+1
#    if low <= high:
#        count += high - low + 1
#
#print(count)

#Confine x region

v0xmin = (-1+np.sqrt(1+8*x1))/2
v0xmax = x2

if v0xmin.is_integer():
    v0xmin = int(v0xmin)
else:
    v0xmin = int(v0xmin) + 1

#for v0x in range(v0xmin,v0xmax+1):
#    print(v0x)


count = 0
for v0x in range(v0xmin,v0xmax+1):
    for v0y in range(-v0ymax-1,v0ymax+1):
#for v0x in range(1,100):
#    for v0y in range(-100,100):
        nxmax,nymax = (v0x,v0y)
        #n = np.arange(2*max(v0ymax,v0xmax))
        #x = v0x*n - n*(n-1)//2
        #x[nxmax+1:] = x[nxmax]
        #y = v0y*n - n*(n-1)//2
        #condition_x = np.logical_and(x>x1,x<x2)
        #condition_y = np.logical_and(y>y1,y<y2)
        #yes = np.logical_and(condition_x,condition_y)
        #if yes.any():
        #    count+=1
        x,y = (0,0)
        n = 0
        while y>=y1:
            if n <= nxmax:
                x = v0x*n - n*(n-1)//2
            y = v0y*n - n*(n-1)//2
            if x>=x1 and x<=x2 and y>=y1 and y<=y2:
                count+=1
                break
            n+=1


print(count)
