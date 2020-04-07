# gcd

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

a, b = map(int, input('Input two integers seperated by a space\n--> ').split(' '))
print('The greatest common divisor is %d' % gcd(a, b))

# palindrome

def palindrome(phrase):
    if len(phrase) <= 1:
        return 1
    elif phrase[:1] == phrase[-1:]:
        return palindrome(phrase[1:-1])
    return 0

phrase = input('Input a word or phrase\n--> ').replace(' ', '').lower()
print(('%s is ' % phrase) + ('a palindrome' if palindrome(phrase) else 'not a palindrome'))

# permutations

def permutations(word):
    if len(word) == 0:
        yield ''
    for index in range(len(word)):
        for perm in list(permutations(word[:index] + word[index+1:])):
            yield word[index] + perm

word = input('Input a word\n--> ').lower()
sub = input('Input another word\n--> ').lower()
print(('%s is ' % sub) + ('' if sub in list(permutations(word)) else 'not ') + ('an anagram of %s' % word))
