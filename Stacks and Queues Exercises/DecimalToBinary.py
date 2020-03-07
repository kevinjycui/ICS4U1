# Name: Kevin Cui
# Date: 2020-02-28
# Description: Decimal to Binary

from Structures import Stack

number = int(input()) # Take input decimal number
digits = Stack() # init stack

while number > 0:
    digits.push(number%2) # Push binary values to stack
    number //= 2

ans = ''
while not digits.isEmpty():
    ans += str(digits.pop()) # Append digits to string

print(ans) # Output
