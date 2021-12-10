import numpy as np
import sys

#coord = np.loadtxt('min_input.txt',dtype='int')
coord1 = []
coord2 = []
coords = []

with open('input.txt') as f:
    #Read coordinates and stores them as [ [[x1,y1],[x2,y2]], etc.]
    for line in f:
        coord1,coord2 = line[:-1].split(' -> ') #-1 to remove the '\n'
        coord1 = list(map(int,coord1.split(',')))
        coord2 = list(map(int,coord2.split(',')))
        coords.append([coord1]+[coord2])

coords = np.array(coords)
#Find the max coordinate (in any direction)
coords_flat = coords.flatten()
max_coord = np.max(coords_flat)

#Represent the grid of hydrothermal vents
grid = np.zeros((max_coord+1,max_coord+1),dtype=int)

for coord in coords:
    x1 = coord[0][0]
    x2 = coord[1][0]
    y1 = coord[0][1]
    y2 = coord[1][1]
    #Part 1
    #if x1 == x2: #vertical line
    #    sign = np.sign(y2-y1)
    #    for i in range(y1,y2+sign,sign):
    #        grid[i,x1] += 1 #Note: x correspond aux colonnes, y aux lignes...
    #elif y1 == y2: #horizontal line
    #    sign = np.sign(x2-x1)
    #    for i in range(x1,x2+sign,sign):
    #        grid[y1,i] += 1 #Note: x correspond aux colonnes, y aux lignes...
    #else: #diagonal
    #    signx = np.sign(x2-x1)
    #    signy = np.sign(y2-y1)
    #    for i in range(abs(x1-x2)+1):
    #        grid[y1+i*signy,x1+i*signx] += 1 #Note: x correspond aux colonnes, y aux lignes...
    #Part 2
    signx = np.sign(x2-x1)
    signy = np.sign(y2-y1)
    maxrange = max(abs(x2-x1),abs(y2-y1))
    for i in range(maxrange+1):
        grid[y1+i*signy,x1+i*signx] += 1 #Note: x correspond aux colonnes, y aux lignes...



print(grid)
#On compte le nombre de points de la grille où au moins 2 lignes s'intersectent
nb_overlap = sum(grid.flatten()>1)
print(nb_overlap)
