# Name: Kevin Cui
# Date: 2020-02-05
# Description: HugeInteger Class

class HugeInteger(object):

    def __init__(self, value='0'):
        '''
        Data structure that represents any arbitrarily large integer number
        in the following format:
            sign   : int value +1, 0, or -1
            size   : int value equal to the number of digits
            values : list of digits in order (most significant digit is first)
        '''
        if type(value) == int:
            self.value = [0]*value
            self.sign = 0
        elif type(value) == str:
            if value.replace('-', '').count('0') == len(value.replace('-', '')):
                self.sign = 0
            elif value[0] == '-':
                self.sign = -1
            else:
                self.sign = 1
            self.value = list(map(int, value.replace('-', '')))
        self.size = self.getSize()

    def __str__(self):
        '''
        (None) -> str

        Returns string number representation of HugeInteger (excluding leading zeroes).
        '''
        if self.sign == -1:
            return '-'+''.join(map(str, self.value[-self.size:]))
        return ''.join(map(str, self.value[-self.size:]))

    def getSize(self):
        '''
        (None) -> int

        Returns number significant digits (excluding leading zeroes).
        '''
        if self.sign == 0:
            return 1
        for d in range(len(self.value)):
            if self.value[d] != 0:
                return len(self.value)-d
        return 0

    def absGreater(self, other):
        '''
        (HugeInteger) -> (bool)

        Returns true if absolute value of self is greater than absolute value of other HugeInteger, otherwise returns false.
        '''
        if self.size != other.size:
            return self.size > other.size
        for c in range(self.size):
            if int(self.value[len(self.value)-self.size+c]) != int(other.value[len(other.value)-other.size+c]):
                return int(self.value[len(self.value)-self.size+c]) > int(other.value[len(other.value)-other.size+c])
        return False        

    def add_digit(self, other, carry, i, sol):
        '''
        (HugeInteger, int, int, list) -> (list)
    
        Adds single digit in self to other HugeInteger. Component of addition.
        '''
        if i > len(self.value) and i > len(other.value):
            sol.reverse()
            return sol
        a = 0
        b = 0
        if i < len(self.value):
            a = self.value[len(self.value)-1-i]
        if i < len(other.value):
            b = other.value[len(other.value)-1-i]
        d = str(a + b + carry)
        sol.append(d[-1:])
        if d[:-1] != '':
            return self.add_digit(other, int(d[:-1]), i+1, sol)
        return self.add_digit(other, 0, i+1, sol)

    def subtract_digit(self, other, carry, i, sol):
        '''
        (HugeInteger, int, int, list) -> (list)
    
        Subtracts single digit in self to other HugeInteger. Component of subtraction.
        '''
        if i > len(self.value) and i > len(other.value):
            sol.reverse()
            return sol
        a = 0
        b = 0
        if i < len(self.value):
            a = self.value[len(self.value)-1-i]
        if i < len(other.value):
            b = other.value[len(other.value)-1-i]
        if b > a - carry:        
            d = str(a - carry + 10 - b)
            sol.append(d)
            return self.subtract_digit(other, 1, i+1, sol)
        d = str(a - carry - b)
        sol.append(d)
        return self.subtract_digit(other, 0, i+1, sol)

    def multiply_digit(self, other, carry, i, sol, deg, mem):
        '''
        (HugeInteger, int, int, list, int, list) -> (list)

        Multiplies single digit in self to other HugeInteger. Component of multiplication.
        '''
        if deg == len(other.value):
            return mem
        if i > len(self.value) and i > len(other.value):
            sol.reverse()
            mem.append(HugeInteger(''.join(sol)))
            return self.multiply_digit(other, 0, 0, ['0']*(deg+1), deg+1, mem)
        a = 0
        if i < len(self.value):
            a = self.value[len(self.value)-1-i]
        d = str(a * other.value[len(other.value)-1-deg] + carry)
        sol.append(d[-1:])
        if d[:-1] != '':
            return self.multiply_digit(other, int(d[:-1]), i+1, sol, deg, mem)
        return self.multiply_digit(other, 0, i+1, sol, deg, mem)

    def add(self, other):
        '''
        (HugeInteger) -> (HugeInteger)

        Performs addition with other HugeInteger and returns sum.
        '''
        if self.sign != -1 and other.sign != -1:
            return HugeInteger(''.join(self.add_digit(other, 0, 0, [])))
        elif self.sign != -1 and other.sign == -1:
            if self.absGreater(other):
                return HugeInteger(''.join(self.subtract_digit(other, 0, 0, [])))
            return HugeInteger('-'+''.join(other.subtract_digit(self, 0, 0, [])))
        elif self.sign == -1 and other.sign != -1:
            if not self.absGreater(other):
                return HugeInteger(''.join(other.subtract_digit(self, 0, 0, [])))
            return HugeInteger('-'+''.join(self.subtract_digit(other, 0, 0, [])))
        return HugeInteger('-'+''.join(self.add_digit(other, 0, 0, [])))

    def subtract(self, other):
        '''
        (HugeInteger) -> (HugeInteger)

        Performs subtraction with other HugeInteger and returns difference.
        '''
        if self.sign != -1 and other.sign != -1:
            if self.absGreater(other):
                return HugeInteger(''.join(self.subtract_digit(other, 0, 0, [])))
            return HugeInteger('-'+''.join(other.subtract_digit(self, 0, 0, [])))
        elif self.sign != -1 and other.sign == -1:
            return HugeInteger(''.join(self.add_digit(other, 0, 0, [])))
        elif self.sign == -1 and other.sign != -1:
            return HugeInteger('-'+''.join(self.add_digit(other, 0, 0, [])))
        if self.absGreater(other):
            return HugeInteger('-'+''.join(self.subtract_digit(other, 0, 0, [])))
        return HugeInteger(''.join(other.subtract_digit(self, 0, 0, [])))

    def multiply(self, other):
        '''
        (HugeInteger) -> (HugeInteger)

        Performs multiplication with other HugeInteger and returns product.
        '''
        prod = HugeInteger('0')
        digs = self.multiply_digit(other, 0, 0, [], 0, [])
        for d in digs:
            prod = prod.add(d)
        if self.sign == other.sign:
            return prod
        return HugeInteger('-'+str(prod))        

number1 = HugeInteger('123456789')
number2 = HugeInteger('987654321')
number3 = HugeInteger('-55555555')
number4 = HugeInteger()

print(str(number1)+' + '+str(number2)+' = '+str(number1.add(number2)))
print(str(number2)+' - '+str(number1)+' = '+str(number2.subtract(number1)))
print(str(number3)+' - '+str(number2)+' = '+str(number3.subtract(number2)))
print(str(number1)+' - '+str(number3)+' = '+str(number1.subtract(number3)))
print(str(number3)+' + '+str(number2)+' = '+str(number3.add(number2)))
print(str(number1)+' + '+str(number3)+' = '+str(number1.add(number3)))
print(str(number1)+' * '+str(number2)+' = '+str(number1.multiply(number2)))
print(str(number3)+' * '+str(number2)+' = '+str(number3.multiply(number2)))
print(str(number1)+' + '+str(number4)+' = '+str(number1.add(number4)))
print(str(number2)+' - '+str(number4)+' = '+str(number2.subtract(number4)))
print(str(number3)+' * '+str(number4)+' = '+str(number3.multiply(number4)))
print(str(number4)+' - '+str(number2)+' = '+str(number4.subtract(number2)))

from random import randint
import time

while True:
    a = randint(-10000000000000000, 10000000000000000)
    b = randint(-10000000000000000, 10000000000000000)
    number1 = HugeInteger(str(a))
    number2 = HugeInteger(str(b))
    sm = number1.add(number2)
    df = number1.subtract(number2)
    pd = number1.multiply(number2)
    if str(sm) != str(a + b):
        print('ADDITION ERROR!', a, b)
        break
    if str(df) != str(a - b):
        print('SUBTRACTION ERROR!', a, b)
        break
    if str(pd) != str(a * b):
        print('MULTIPLICATION ERROR!', a, b)
        break
    
    print(str(number1)+' + '+str(number2)+' = '+str(sm))
    print(str(number1)+' - '+str(number2)+' = '+str(df))
    print(str(number1)+' * '+str(number2)+' = '+str(pd))
    
