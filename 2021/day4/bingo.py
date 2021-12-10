import sys
import numpy as np

# Read draws and boards
with open('input.txt') as f:
    #Read numbers drawn and store them as list of strings
    draws = f.readline()[:-1].split(',') #-1 to remove the '\n'
    draws = list(map(int,draws)) #For this bingo type, let's work with int types
    #Read 5x5 boards
    boards = []
    while True:
        line = f.readline() #pass empty line
        if not line:
            break
        current_board = []
        for i in range(5):
            line = f.readline()[:-1].split()
            line = list(map(int,line)) #For this bingo type, let's work with int types
            current_board.append(line)
        boards.append(current_board)

#Create masks that will contain 0 or 1 whether a number in the board has been drawn or not
#masks = np.ones((len(boards),5,5),dtype=bool) #Part 1: start with only 1s, i.e. non-drawn numbers
masks = np.zeros((len(boards),5,5),dtype=bool) #Part 2

draws.reverse() #Part 2: let's start from the end, and remove elements called progressively

#boucle sur les numéros tires
for num in draws:
    #boucle sur les grilles
    for idx,board in enumerate(boards):    
        #on regarde si le numéro est dans la grille. Si oui, on change le masque. Si non, on ne fait rien.
        for idx_r,row in enumerate(board):
            if num in row:
                idx_c = row.index(num)
                #masks[idx,idx_r,idx_c] = False #Part1
                masks[idx,idx_r,idx_c] = True #Part 2
        #on regarde si une ligne ou une colonne du masque contient uniquement des 0 (si le numéro précédent était dans la grille). Si oui, on a le gagnant et on fait la somme des numéros non tirés.
        #Check if a column or a row is completed
        #if (np.sum(masks[idx],axis=0)==0).any() or (np.sum(masks[idx],axis=1)==0).any(): # Part 1
        if (np.sum(masks[idx],axis=0)!=0).all() and (np.sum(masks[idx],axis=1)!=0).all(): # Part 2
            print('Bingo! \nDernier numéro :',num, '\nGrille gagnante n° :',idx)
            masked_board = np.multiply(masks[idx],boards[idx])
            print('Les numéros restant sont :\n',masked_board)
            #Part 1 :
            #print(np.sum(masked_board),'*',num,'=',np.sum(masked_board)*num)
            #Part 2 : masked_board contient tous les numéros non tirés + le dernier numéro tiré. Il faut donc le retrancher à la somme.
            print(np.sum(masked_board)-num,'*',num,'=',(np.sum(masked_board)-num)*num)
            sys.exit()


