# 1
print(''.join([str((a, b, c))+'\n' if c == 6 else str((a, b, c))+'\t' for a in range(1, 7) for b in range(1, 7) for c in range(1, 7)]))

# 2
print('Farenheit to Celsius:\n'+str([(a[0], round(a[1], 1)) for a in zip([f for f in range(0, 101, 10)], [(f-32)*5/9 for f in range(0, 101, 10)])])+'\n')
print('Celsius to Farenheit:\n'+str([(a[0], round(a[1], 1)) for a in zip([c for c in range(-10, 51, 5)], [c*(9/5)+32 for c in range(-10, 51, 5)])])+'\n')

# 3
def toZero(l):
    rot = [[l[a][b] for a in range(len(l))] for b in range(len(l[0]))]
    return [[0 if l[b].count(0) > 0 or rot[a].count(0) > 0 else l[b][a] for a in range(len(l[b]))] for b in range(len(l))]

import random
d = [[random.randint(0, 9) for i in range(6)] for j in range(6)]
print('\n'.join(map(str, d))+'\n')
print('Zero Matrix:\n'+'\n'.join(map(str, toZero(d))))
