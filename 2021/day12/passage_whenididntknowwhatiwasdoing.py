from sys import exit
import sys
#sys.setrecursionlimit(5000)

connections = {}
#Create connections
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

all_paths = []
wrong_paths = []

def search_path(current_path):
    global all_paths
    global wrong_paths
    #print("current",current_path)

    if not current_path:
        return all_paths
    #print("current",current_path)
    current_cave = current_path[-1]
    #Go through neighbouring caves
    for cave in connections[current_cave]:
        nextpath = current_path + list([cave])
        #print("next",nextpath)
        #if nextpath in wrong_paths:
            #print("if in wrong")
        #    pass
        if cave == "end":
            #print("if end")
            all_paths.append(nextpath.copy())
            #wrong_paths.append(nextpath.copy())
        #elif cave in current_path and cave.islower() and nextpath not in wrong_paths:
        elif cave in current_path and cave.islower():
            #print("if lower twice")
            pass
        else:
            #print("else")
            #return search_path(nextpath)
            search_path(nextpath)

    # At this point all paths available from the current cave should have been visited
    #if current_path:
    #    print("loop finished")
    #    wrong_paths.append(current_path.copy())
    #    current_path.pop()
    #    #return search_path(current_path)
    #    #return 1
    #else:
    #    return all_paths

search_path(["start"])

#print(len(all_paths),"paths were found:")
#for path in all_paths:
#    print(path)
print(len(all_paths),"paths were found")

#for path in wrong_paths:
#    print(path)
