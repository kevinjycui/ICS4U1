n = input('Enter name of book (frankenstein or dracula): ')
word1 = input('Enter first word: ')
word2 = input('Enter second word: ')

with open(n+'.txt') as f:
    lines = ''
    for n in f:
        lines += n.lower()
    punct = ['.', ',', '?', '!', '(', ')', ':', ';', '-', '/', '_', '[', ']', '{', '}', '"']
    for p in punct:
        lines = lines.replace(p, '')
    white = ['\n', '\r', '\t']
    for w in white:
        lines = lines.replace(w, ' ')
    while '  ' in lines:
        lines = lines.replace('  ', ' ')
    text = lines.split(' ')
    val = len(text)

    keyindex = []
    keywords = []

    for c in range(len(text)):
        if text[c] == word1 or text[c] == word2:
            keyindex.append(c)
            keywords.append(text[c])

    if keywords.count(word1) == 0 or keywords.count(word2) == 0:
        print('Invalid')

    else:
        ans = len(text)+1
        passage = ''

        for l in range(len(keywords)):
            if l-1 >= 0 and keywords[l] != keywords[l-1] and ans > keyindex[l] - keyindex[l-1]:
                ans = keyindex[l] - keyindex[l-1]
                passage = ' '.join(text[keyindex[l-1]:keyindex[l]+1])
            if l+1 < len(keywords) and keywords[l] != keywords[l+1] and ans > keyindex[l+1] - keyindex[l]:
                ans = keyindex[l+1] - keyindex[l]
                passage = ' '.join(text[keyindex[l]:keyindex[l+1]+1])
        
        print('Shortest distance is', ans, 'words.')
        print(passage)
