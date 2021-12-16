import numpy as np

with open("input.txt") as f:
    crabs_pos = np.array(list(map(int,f.readline()[:-1].split(','))))

#Part 1
#median = int(np.median(crabs_pos)) #Fortunately, the median is an integer, so we don't have to test 2 cases
#fuel = abs(crabs_pos-median)
#print("Fuel needed:",sum(fuel))


#Part 2

minimum = min(crabs_pos)
maximum = max(crabs_pos)
sum_fuel = -1

# We don't know which position is optimal, so loop through all possible
for target in range(minimum,maximum,1):
    diff = abs(crabs_pos-target)
    fuel = diff*(diff+1)//2 #since each step costs 1 more each time, the consumption of 1 crab is n*(n+1)/2
    if sum_fuel > 0:
        sum_fuel = min(sum(fuel),sum_fuel)
    else:
        sum_fuel = sum(fuel)

print("Fuel needed:",sum_fuel)
