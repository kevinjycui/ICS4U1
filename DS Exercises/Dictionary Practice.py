# Name: Kevin Cui
# Date: 2020-02-16
# Description: Dictionary Practice

# 1
# Sub-description: Frequency Dice Chart
combos = []
for i in range(1, 7):
    combos.append([])
    for j in range(1, 7):
        combos[i-1].append(i+j)

freq = {}
for r in combos:
    for c in r:
        freq[c] = freq.get(c, 0) + 1

print(freq)

# 2
# Sub-description: Inverted Dictionary
students_to_marks = {
    'Jean Valjean': 100,
    'Javert': 100,
    'Eponine': 90,
    'Cosette': 90,
    'Marius': 90,
    'Monsieur Thenardier': 95,
    'Madame Thenardier': 95,
    'Fantine': 85,
    'Gavroche': 80,
    'Enjolras': 80
    }

marks_to_students = {}
for stud in students_to_marks:
    mark = students_to_marks[stud]
    if mark in marks_to_students:
        marks_to_students[mark].append(stud)
    else:
        marks_to_students[mark] = [stud]

print(students_to_marks)
print(marks_to_students)
for mark in marks_to_students:
    print(mark, ': ('+str(len(marks_to_students[mark]))+')', marks_to_students[mark])

# 3
# Sub-description: Cipher with Dictionary
import random

alphabet = ' '
for a in range(ord('a'), ord('z')+1):
    alphabet += chr(a)
alphabet = list(alphabet)
original = alphabet[:]
random.shuffle(alphabet)
code = {}
for c in range(len(alphabet)):
    code[alphabet[c]] = original[c]

def encoder(dictionary, msg):
    enc = ''
    for m in msg:
        enc += dictionary[m]
    return enc

def decoder(dictionary, coded):
    inv = {}
    for d in dictionary:
        val = dictionary[d]
        inv[val] = d
    dec = ''
    for c in coded:
        dec += inv[c]
    return dec

message = input('Input message: ')
coded = encoder(code, message)
print('Encoded:', coded)
decoded = decoder(code, coded)
print('Decoded', decoded)
