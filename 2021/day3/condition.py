import numpy as np
import sys

binary = []

with open('min_input.txt') as f:
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

while len(bin_oxy) != 1:
    idx = 0
    bin_oxy_trans = np.transpose(bin_oxy)
    bin_co2_trans = np.transpose(bin_co2)
    n0 = 0
    n1 = 0
    for el in bin_oxy_trans[idx]:
        if el == '0':
            n0 += 1
        elif el == '1':
            n1 += 1
    if n1 >= n0:
        most_frequent = '1'
    else:
        most_frequent = '0'
    for i range(len(bin_oxy)):
        if bin_oxy_trans[i] != most_frequent



