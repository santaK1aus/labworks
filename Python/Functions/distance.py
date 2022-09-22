#9.29
from math import sqrt

def dist(p1,p2):
    print('Points are :',p1,p2)
    print('Euclidean Distance is',(sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)))
    print('Manhattan Distance is',(abs(p1[0]-p2[0])+abs(p1[1]-p2[1])))

dist((2,3),(9,10))