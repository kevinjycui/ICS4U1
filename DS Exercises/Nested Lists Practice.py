# Name: Kevin Cui
# Date: 2020-02-14
# Description: Nest Lists Practice

# 1
dice = [] # init list
for row in range(1, 7):
    dice.append([])
    for col in range(1, 7):
        dice[row-1].append(row + col) # fill matrix

for row in range(6): # loop through matrix
    for col in dice[row]:
        if len(str(col)) == 1: # check num of digits for formatting
            print('  '+str(col), end=' |\t')
        else:
            print(' '+str(col), end=' |\t')
    print('\n'+'-'*45) # print horizontal border

# 2
dice3 = [] # init list
for r in range(1, 7):
    dice3.append([])
    for c in range(1, 7):
        dice3[r-1].append([])
        for h in range(1, 7):
            dice3[r-1][c-1].append(r+c+h) # fill 3 dimensional list

freq = [0]*16 # init freq list
for r in range(1, 7):
    for c in range(1, 7):
        for h in dice3[r-1][c-1]:
            freq[h-3] += 1 # find frequencies (shifted by 3)
for f in range(16): # output freq table
    print((' '*(2-len(str(f+3z))))+str(f+3)+' |\t'+(' '*(2-len(str(freq[f]))))+str(freq[f]), end='\n----------\n')

# 3
pascals = [[0]*10 for i in range(10)] # init matrix
for i in range(10):
    for j in range(10):
        if i == 0 or j == 0:
            pascals[i][j] = 1 # set begin to 1
        else:
            pascals[i][j] = pascals[i-1][j] + pascals[i][j-1] # set values to sum of values before
for i in range(10):
    for j in range(10):
        print('\t', ' '*(5-len(str(pascals[i][j]))), pascals[i][j], end='') # output pascal's triangle
    print()

# 4
def get_zeros(l): # define function to change rows and columns with zero to zero
    rot = [[l[a][b] for a in range(len(l))] for b in range(len(l[0]))] # get rotated matrix
    return [[0 if l[b].count(0) > 0 or rot[a].count(0) > 0 else l[b][a] for a in range(len(l[b]))] for b in range(len(l))]

import random
d = [[random.randint(0, 9) for i in range(6)] for j in range(6)] # init random matrix
print('\n'.join(map(str, d))+'\n')
print('Zero Matrix:\n'+'\n'.join(map(str, get_zeros(d)))+'\n') # call and output to zero matrix

# 5
n = int(input())
mat = [[random.randint(0, 9) for i in range(n)] for j in range(n)] # init matrix
rot = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ') # output right-side up matrix
        rot[j][n-1-i] = mat[i][j] # create rotated matrix
    print()

    
print('\nRotated:')
for i in range(n):
    for j in range(n):
        print(rot[i][j], end=' ') # output rotated matrix
    print()
