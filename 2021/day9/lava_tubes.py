import numpy as np
from sys import exit

# Read heightmap
heightmap = []
with open("input.txt") as f:
    for line in f:
        heightmap.append(list(map(int,line[:-1])))

heightmap = np.array(heightmap)
print(heightmap)

def find_lowest(heightmap):
    # Compute lowest point on a line left to right
    diff_hor_lr = heightmap[:,:-1]-heightmap[:,1:] < 0
    # Add missing column, which should be the negation of the current last column
    add = ~ np.transpose(diff_hor_lr)[-1]
    diff_hor_lr = np.transpose(diff_hor_lr)
    diff_hor_lr = np.transpose(np.vstack((diff_hor_lr,add)))
    
    # Compute lowest point on a line right to left
    diff_hor_rl = heightmap[:,1:]-heightmap[:,:-1] < 0
    # Add missing column, which should be the negation of the current first column (and also the same as the 1st column in left to right)
    add = ~ np.transpose(diff_hor_rl)[0]
    diff_hor_rl = np.transpose(diff_hor_rl)
    diff_hor_rl = np.transpose(np.vstack((add,diff_hor_rl)))
    # The lowest point horizontally is obtained by summing logically
    diff_hor = np.logical_and(diff_hor_lr,diff_hor_rl)
    return diff_hor

#Lowest horizontally
diff_hor = find_lowest(heightmap)
#Lowest vertically
diff_vert = np.transpose(find_lowest(np.transpose(heightmap)))
mask = np.logical_and(diff_hor,diff_vert)
print(np.sum(mask*(heightmap+1)))


# Part 2
# Retrieve lowest points location
lowest_points = []
for i,el in enumerate(mask):
    for j,el2 in enumerate(el):
        if el2:
            lowest_points.append([i,j])

def find_higher_neighbours(point,higher_neighbours):
    xp = point[0]
    yp = point[1]
    higher_neighbours_current = []
    Nx = len(heightmap[0])
    Ny = len(heightmap[:,0])
    neighbours = []
    for coord in [[xp-1,yp],[xp+1,yp],[xp,yp-1],[xp,yp+1]]:
        if coord[0]>=0 and coord[0]<Ny and coord[1]>=0 and coord[1]<Nx:
            neighbours.append(coord)
    for coord in neighbours:
        if heightmap[coord[0],coord[1]] > heightmap[xp,yp] and heightmap[coord[0],coord[1]]<9:
            if coord not in higher_neighbours:
                higher_neighbours.append(coord)
                higher_neighbours_current.append(coord)
    if higher_neighbours_current == []:
        return
    else:
        for pt in higher_neighbours_current:
            find_higher_neighbours(pt,higher_neighbours)
        return higher_neighbours

# Loop on lowest_points
lengths = []
for lp in lowest_points:
    high_neighbours = find_higher_neighbours(lp,[lp])
    print(len(high_neighbours),high_neighbours)
    lengths.append(len(high_neighbours))

lengths = sorted(lengths)
print(lengths, lengths[-1]*lengths[-2]*lengths[-3])


