import numpy as np

#part 1: 1-measurement sliding window

measurements = np.loadtxt('input.txt',dtype='int')

diff = np.sum(measurements[1:] > measurements[:-1]) #sum booleans
print(diff)

#Former version
#N = len(measurements) - 1
# Creates an array containing the difference of consecutive numbers, then take only the sign and sum all terms
#diff = np.sum(np.sign(measurements[1:] - measurements[:-1]))
#print((N + diff)//2)
# Notes
#npos + nneg = N
#npos + (-1)nneg = diff
# Thus npos = (N + diff)/2

#Part 2: 3-measurements sliding window

threesum = measurements[2:] + measurements[1:-1] + measurements[:-2]
diff = np.sum(threesum[1:] > threesum[:-1])
print(diff)
