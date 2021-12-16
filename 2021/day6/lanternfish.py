import numpy as np

with open("input.txt") as f:
    fishlist = np.array(list(map(int,f.readline()[:-1].split(','))))

#Slow
#for day in range(170):
#    fishlist -= 1
#    nb_newfish = np.sum(fishlist == -1)
#    fishlist[fishlist==-1] = 6 #Replace -1 by 6
#    newfish = np.full(nb_newfish,8,dtype=int)
#    fishlist = np.append(fishlist,newfish)

#print(fishlist,len(fishlist))

#Fast

# Create an array of size 9, the elements of which contain the number of fish with a given timer
fishtimers, _ = np.histogram(fishlist,bins=range(10))

for day in range(256):
    fishtimers = np.roll(fishtimers,-1) #circular permutation (nb of 7 become nb of 6, etc.)
    fishtimers[6] += fishtimers[8] #reset timer to 6 for the ones who have just given life to new fish!

print(sum(fishtimers))
