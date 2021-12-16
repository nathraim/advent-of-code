from sys import exit

lst = []
with open("input.txt") as f:
    for line in f:
        lst.append(line[:-1])

openings = ['(','[','{','<']
closures = [')',']','}','>']
table = [3,57,1197,25137]
syntax_score = 0
id_corrupted = []

for id_line,line in enumerate(lst):
    nb_symb = [0,0,0,0]
    pos_open = [[],[],[],[]]
    for pos,symb in enumerate(line):
        if symb in openings:
            idx = openings.index(symb)
            nb_symb[idx] += 1
            pos_open[idx].append(pos)
        elif symb in closures:
            idx = closures.index(symb)
            nb_symb[idx] -= 1
            if nb_symb[idx] < 0: 
                print(line)
                print("Corruption must be fought! 1", symb,pos,table[idx])
                id_corrupted.append(id_line)
                syntax_score += table[idx]
                #incomplete.pop(id_line)
                break
                exit()
            #elif nb_symb[idx] == 0:
            else:
                idx_last_open = pos_open[idx][-1]
                nb_symbin = [0,0,0,0]
                for posin,symbin in enumerate(line[idx_last_open+1:pos]):
                    #print("yeah",pos,idx_last_open)
                    if symbin in openings:
                        idxin = openings.index(symbin)
                        nb_symbin[idxin] += 1
                    elif symbin in closures:
                        idxin = closures.index(symbin)
                        nb_symbin[idxin] -= 1
                    if nb_symbin[idxin] < 0: 
                        print(line)
                        print("Corruption must be fought! 2", symb,pos,table[idx])
                        id_corrupted.append(id_line)
                        syntax_score += table[idx]
                        break
                        exit()
                if nb_symbin != [0,0,0,0] and pos<len(line)-1:
                    #print("oh",nb_symbin)
                    print(line)
                    print("Corruption must be fought! 3", symb,pos,table[idx])
                    id_corrupted.append(id_line)
                    syntax_score += table[idx]
                    break
                    exit()
                else:
                    #print("pop",pos,idx_last_open,pos_open)
                    pos_open[idx].pop(-1)
                    if pos_open[idx] != []:
                        idx_last_open = pos_open[idx][-1]
                    #print("pop",pos,idx_last_open,pos_open)
            #elif nb_symb[idx] > 0:
            #    pos_open[idx].pop(-1)
            #    if pos_open[idx] != []:
            #        idx_last_open = pos_open[idx][-1]

print("Highscore!", syntax_score)
        

# Part 2

table = [1,2,3,4]
syntax_scores = []
for el in sorted(id_corrupted,reverse=True):
    del lst[el]

for id_line,line in enumerate(lst):
    syntax_score = 0
    print(line)
    nb_symb = [0,0,0,0]
    pos_open = [[],[],[],[]]
    for pos,symb in enumerate(line):
        if symb in openings:
            idx = openings.index(symb)
            nb_symb[idx] += 1
            pos_open[idx].append(pos)
        elif symb in closures:
            idx = closures.index(symb)
            nb_symb[idx] -= 1
            idx_last_open = pos_open[idx][-1]
            pos_open[idx].pop(-1)
            if pos_open[idx] != []:
                idx_last_open = pos_open[idx][-1]
    pos_open = sorted([item for sublst in pos_open for item in sublst],reverse=True)
    for id_open in pos_open:
        symb = line[id_open]
        idx = openings.index(symb)
        syntax_score = 5*syntax_score + table[idx]
    syntax_scores.append(syntax_score)
syntax_scores = sorted(syntax_scores)
print("Highscore!",syntax_scores[len(syntax_scores)//2])
