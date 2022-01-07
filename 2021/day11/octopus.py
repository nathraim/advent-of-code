import numpy as np

energy_grid = []
with open("input.txt") as f:
    for line in f:
        energy_grid.append(list(map(int,line[:-1])))

energy_grid = np.array(energy_grid)

Nx = len(energy_grid[0])
Ny = len(energy_grid[:,0])
neighbours = [[[] for i in range(Ny)] for j in range(Nx)]
#print(neighbours)
for idx,el in enumerate(energy_grid):
    for idy,_ in enumerate(el):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not (i == 0 and j == 0) and idx+i >= 0 and idx+i < Ny and idy+j >= 0 and idy+j < Nx:
                    neighbours[idx][idy].append([idx+i,idy+j])
#neighbours = np.array(neighbours)
#print(neighbours)
#print("00",neighbours[0,0])
#print("53",neighbours[5,3])

def get_nines(grid,flashed):
    nines = []
    for i,line in enumerate(grid):
        for j,el in enumerate(line):
            if el > 9 and not flashed[i,j]:
                nines.append([i,j])
    return nines

def increase_energy(coord,energy_grid):
    idx,idy = (coord[0],coord[1])
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if not (i == 0 and j == 0) and idx+i >= 0 and idx+i < Ny and idy+j >= 0 and idy+j < Nx:
                energy_grid[idx+i,idy+j] += 1
    return energy_grid

def reset(grid,flashed):
    for i,line in enumerate(grid):
        for j,el in enumerate(line):
            if el > 9:
                grid[i,j] = 0
    return grid

nb_flash = 0
synchro = []
#print(energy_grid)
for step in range(500):
    energy_grid += 1
    has_flashed = np.zeros((Nx,Ny),dtype=bool)
    #trouver les octopus qui ont 9 ou plus
    nines = get_nines(energy_grid,has_flashed)
    while(nines != []):
        #augmenter de 1 les voisins de 9 ou plus et mettre à jour la liste de ceux qui ont flashé
        for coord in nines:
            energy_grid = increase_energy(coord,energy_grid)
            has_flashed[coord[0],coord[1]] = True
        #recommencer jusqu'à ce qu'il n'y ait plus de 9 ou plus qui n'aient pas déjà flashé 
        nines = get_nines(energy_grid,has_flashed)
    energy_grid = reset(energy_grid,has_flashed)
    nb_flash += np.sum(has_flashed)
    if has_flashed.all():
        synchro.append(step+1)

    #print(step+1,energy_grid)

print("It flashed",nb_flash, "times!")
if synchro != []:
    print("First synchronization at step",synchro[0])



