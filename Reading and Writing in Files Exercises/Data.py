with open('data.txt') as f:
    numbers = []
    for n in f:
        numbers = n[:-1].split(' ')
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1
    with open('frequency.txt', 'w') as w:
        w.write(str(freq))
