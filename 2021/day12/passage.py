from sys import exit
import sys
#sys.setrecursionlimit(5000)

connections = {}
#Create connections between caves
with open("input.txt") as f:
    for line in f:
        line2 = line[:-1].split('-')
        if line2[0] not in connections:
            connections.update( {line2[0] : [line2[1]]} )
        else:
            current = connections[line2[0]]
            current.append(line2[1])
            connections.update( {line2[0] : current} )
        if line2[1] not in connections:
            connections.update( {line2[1] : [line2[0]]} )
        else:
            current = connections[line2[1]]
            current.append(line2[0])
            connections.update( {line2[1] : current} )

print(connections)

def is_lower_twice(path):
    '''Check if a cave has been visited twice in a given path'''
    dict_count = {}
    for el in path:
        if el.islower() and el not in dict_count:
            dict_count.update( {el : 0} )
        if el.islower():
            dict_count.update( {el : dict_count[el]+1} )
    for key,value in dict_count.items():
        if value == 2:
            return True
    return False

all_paths = []

def search_path(current_path):
    global all_paths

    if not current_path:
        return 

    current_cave = current_path[-1]

    #Go through neighbouring caves
    for cave in connections[current_cave]:
        nextpath = current_path + list([cave])
        nb_lower = nextpath.count(cave) #Count number of times the latest cave has been visited
        if cave == "end":
            all_paths.append(nextpath.copy())
        #elif cave in current_path and cave.islower(): # Part 1
        #If it's a small cave, and any given small cave has already been visited twice, skip
        elif ( cave.islower() and is_lower_twice(current_path) and nb_lower>1 ) or cave == "start": # Part 2
            pass
        else:
            search_path(nextpath)

search_path(["start"])

#print(len(all_paths),"paths were found:")
#for path in all_paths:
#    print(path)
print(len(all_paths),"paths were found")
