nb_easy = 0
output_nb = 0

def is_in_string(str1,str2):
    for char in str1:
        if char not in str2:
            return False
    return True

def find_mapping(signal):
    mapping = {}
    #Let us first rearrange signal by length and alphabetical order
    signal = sorted(signal,key=len) #Sort elements by length
    signal_alpha = []
    for el in signal:
        el2 = "".join(sorted(el)) #transforms the sorted list into a single string
        signal_alpha.append(el2)
    signal = signal_alpha
    #Maps the easy numbers
    for el in signal:
        if len(el)==2:
            mapping['1'] = el
        elif len(el)==3:
            mapping['7'] = el
        elif len(el)==4:
            mapping['4'] = el
        elif len(el)==7:
            mapping['8'] = el
    for el in signal[3:6]: # Loop through elements of length 5
        if is_in_string(mapping['7'],el):
            mapping['3'] = el
    for el in signal[6:9]: # Loop through elements of length 6
        if not is_in_string(mapping['1'],el):
            mapping['6'] = el
        elif is_in_string(mapping['3'],el):
            mapping['9'] = el
        else:
            mapping['0'] = el
    for el in signal[3:6]: # Loop through elements of length 5 again to find encoding for numbers 2 and 5
        if is_in_string(el,mapping['6']):
            mapping['5'] = el
        elif el != mapping['3']:
            mapping['2'] = el

    reversed_mapping = dict(map(reversed, mapping.items()))
    return reversed_mapping


with open("input.txt") as f:
    for line in f:
        line2 = line[:-1].split(' ')
        signal = line2[:10]
        output = line2[11:]
        # Part 1
        #for el in output:
        #    if len(el) in [2,3,4,7]:
        #        nb_easy += 1
        # Part 2
        mapping = find_mapping(signal)
        nb = ''
        for el in output:
            el2 = "".join(sorted(el))
            nb += mapping[el2]
        output_nb += int(nb)

print(output_nb)

