import numpy as np
import sys

binary = []

with open('input.txt') as f:
    for line in f:
        line2 = list(line) #transform a string into a list of chars
        line2.remove('\n')
        binary.append(line2)

bin_trans = np.transpose(binary)

gamma = ''
epsilon = ''

for line in bin_trans:
    n0 = 0
    n1 = 0
    for el in line:
        if el == '0':
            n0 += 1
        elif el == '1':
            n1 += 1
    if n1 > n0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

#def convert_bin_to_decimal(binary):
#    deci = 0
#    l = len(binary)
#    for i,num in enumerate(binary):
#        deci += num*2**(l-1-i)
#    return deci

#gamma_rate = convert_bin_to_decimal(gamma)
#epsilon_rate = convert_bin_to_decimal(epsilon)

# Convert binary to decimal
gamma_rate = int(gamma,2)
epsilon_rate = int(epsilon,2)

print(gamma,gamma_rate,epsilon,epsilon_rate)
print("consumption rate: ", gamma_rate*epsilon_rate)

#part 2

oxygen = ''
co2 = ''

bin_oxy = binary.copy()
bin_co2 = binary.copy()

idx = 0
while len(bin_oxy) != 1:
    bin_oxy_trans = np.transpose(bin_oxy)

    n0 = 0
    n1 = 0
    # First pass to determine which bit is most frequent
    for el in bin_oxy_trans[idx]:
        if el == '0':
            n0 += 1
        elif el == '1':
            n1 += 1
    if n1 >= n0:
        noxy = '1'
    else:
        noxy = '0'
    # Now go through binaries again and discard those which do not start by the most frequent bit 
    count = 0
    for j,el in enumerate(bin_oxy_trans[idx]):
        if el != noxy:
            bin_oxy.pop(j-count)
            count += 1
    idx += 1

#print(bin_co2)
idx = 0
while len(bin_co2) != 1:
    bin_co2_trans = np.transpose(bin_co2)
    n0 = 0
    n1 = 0
    # First pass to determine which bit is least frequent
    for el in bin_co2_trans[idx]:
        if el == '0':
            n0 += 1
        elif el == '1':
            n1 += 1
    if n1 >= n0:
        nco2 = '0'
    else:
        nco2 = '1'
    # Now go through binaries again and discard those which do not start by the most frequent bit 
    count = 0
    for j,el in enumerate(bin_co2_trans[idx]):
        if el != nco2:
            bin_co2.pop(j-count)
            count += 1
    #print(bin_co2)

    idx += 1

bin_oxy = ''.join(bin_oxy[0])
bin_co2 = ''.join(bin_co2[0])

print(bin_oxy,bin_co2,int(bin_oxy,2)*int(bin_co2,2))

