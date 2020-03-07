with open('zodiac.txt') as f:
    zodiacs = [{}]
    traits = ['Name', 'Dates', 'Personality', 'Colours', 'Stones', 'Metals', 'Trees', 'Flowers', 'Planet']
    s = []
    for n in f:
        if n == '\n':
            for i in range(0, 2):
                zodiacs[len(zodiacs)-1][traits[i]] = s[i].replace('\n', '')
                s[i] = ''
            for i in range(1, 7):
                zodiacs[len(zodiacs)-1][traits[len(traits)-i]] = s[len(s)-i].replace('\n', '')
                s[len(s)-i] = ''
            for c in s:
                zodiacs[len(zodiacs)-1][traits[2]] = zodiacs[len(zodiacs)-1].get(traits[2], '') + c
            s = []
            zodiacs.append({})
        else:
            s.append(n)

    for i in range(0, 2):
        zodiacs[len(zodiacs)-1][traits[i]] = s[i].replace('\n', '')
        s[i] = ''
    for i in range(1, 7):
        zodiacs[len(zodiacs)-1][traits[len(traits)-i]] = s[len(s)-i].replace('\n', '')
        s[len(s)-i] = ''
    for c in s:
        zodiacs[len(zodiacs)-1][traits[2]] = zodiacs[len(zodiacs)-1].get(traits[2], '') + c

    for z in range(len(zodiacs)):
        print(str(z+1)+'. '+zodiacs[z]['Name'])
                
    p = int(input('Enter zodiac between 1-12: '))

    print()    
    for t in range(2, 8):
        print(str(t)+'. '+traits[t])
    
    q = [0, 1] + list(map(int, input('Enter zodiac information between 2 to 8: ').split(' ')))

    print('\nYour zodiac sign and qualities are:\n--------------------------------\n')
    
    for r in q:
        print(traits[r]+': '+zodiacs[p-1][traits[r]]+'\n')
