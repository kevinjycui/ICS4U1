with open('inputFile1.txt') as f:
    for n in f:
        seq = n.split(' ')
    number = int(seq[0])
    with open('outputFile1.txt', 'w') as g:
        digit = '0'
        prev = 1
        res = ''
        for c in range(1, number+1):
            if seq[c] != digit:
                res += str(c-prev)+' '
                prev = c
                digit = seq[c]
        res = str(len(res.split(' ')))+' '+res+str(number+1-prev)
        g.write(res)
    
