with open('inputFile2.txt') as f:
    for n in f:
        seq = n.split(' ')
    number = int(seq[0])
    res = ''
    digit = '0'
    for c in range(1, number+1):
        res += (digit+' ')*int(seq[c])
        digit = str(1-int(digit))
    res = str(len(res.split(' '))-1) + ' ' + res[:-1]
    with open('outputFile2.txt', 'w') as g:
        g.write(res)
