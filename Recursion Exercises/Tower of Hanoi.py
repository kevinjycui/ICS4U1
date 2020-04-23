1# Name: Kevin Cui
# Date: 2020-04-22
# Description: Recursive Tower of Hanoi


class Stack: # generic stack class
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Towers(object):  # hanoi towers class that stores three tower stacks

    def __init__(self, size):  # initialize with size input
        self.size = size
        self.evenNotOdd = self.size % 2 == 0  # check even or odd to determine sequence
        self.towers = [Stack(), Stack(), Stack()]  # three towers
        for i in range(size, 0, -1):
            self.towers[0].push(i)  # add initial towers to tower A
        self.moveCount = 0  # set move count to 0

    def __str__(self):  # string method for printing
        out = '< Move ' + str(self.moveCount) + ' >\n'
        for i, t in enumerate(self.towers):
            out += 'Tower ' + str(i + 1) + ': ' + str(t) + '\n'
        return out

    def print(self):  # print method
        print(self)  # print on the screen
        print('Vertical visual:\n')
        self.drawVertical()  # draw vertically
        print('\nHorizontal visual:\n')
        self.drawHorizontal()  # draw horizontally

    def drawTowerVertical(self, tower, temp, idx):  # draw a single row of a single tower vertically
        if idx <= self.towers[tower].size():  # if there is a disk at this level
            temp[tower].push(self.towers[tower].pop())
            val = temp[tower].peek()
            print((' ' * (self.size - val)) + ('=' * (2 * val + 1)) + (' ' * (self.size - val)), end='\t')  # draw disk
        else:  # if there is no disk
            print((' ' * self.size) + '|' + (' ' * self.size), end='\t')  # draw empty pole

    def drawVertical(self):  # draw entire three towers vertically
        temp = [Stack(), Stack(), Stack()]  # temporary list to hold values when popping for output
        for i in range(self.size, 0, -1):
            for t in range(len(self.towers)):
                self.drawTowerVertical(t, temp, i)  # call the single row drawing method
            print()
        print('#' * (self.size * 9))  # draw the base
        for t in range(len(temp)):
            while not temp[t].isEmpty():
                self.towers[t].push(temp[t].pop())  # set towers back using temporary list

    def drawTowerHorizontal(self, tower, temp):  # draw a tower horizontally
        grid = []
        for i in range(2 * self.size + 1):
            grid.append([])
            for j in range(self.size):
                if i == self.size:
                    grid[len(grid) - 1].append('--')
                else:
                    grid[len(grid) - 1].append('  ')  # create empty towers represented by matrix

        while not self.towers[tower].isEmpty():
            temp[tower].push(self.towers[tower].pop())
            val = temp[tower].peek()
            for i in range(val + 1):
                grid[self.size + i][self.size - self.towers[tower].size() - 1] = '||'  # draw disks where present
                grid[self.size - i][self.size - self.towers[tower].size() - 1] = '||'

        for row in grid:  # output generated matrix
            print('#', end=' ')
            for pic in range(len(row) - 1, -1, -1):
                print(row[pic], end=' ')
            print()

        for t in range(len(temp)):
            while not temp[t].isEmpty():
                self.towers[t].push(temp[t].pop())  # set tower back using temporary list

    def drawHorizontal(self):
        temp = [Stack(), Stack(), Stack()]  # temporary list to hold values when popping for output
        for t in range(len(self.towers)):
            self.drawTowerHorizontal(t, temp)  # draw each tower

    def move(self, a, b):  # perform single move
        words = ['First', 'Second', 'Third']  # words for numbering when outputting
        self.towers[b].push(self.towers[a].pop())  # perform move
        self.moveCount += 1  # increment move count
        self.print()  # draw towers
        print('Moved a disk from', words[a], 'pole to', words[b], 'pole.')  # output move
        print('\n')

    def moveSequence(self, disk, beg, end, aux): # recursive function to move tower
        if disk == 1: # check base case
            self.move(beg, end) # move smallest disk
            return
        self.moveSequence(disk-1, beg, aux, end) # move tower to temporary pole
        self.move(beg, end) # move last disk to end pole
        self.moveSequence(disk-1, aux, end, beg) # move tower to end pole

while True:
    try:
        n = int(input('How many discs do you want?'))  # prompt for input
        if n <= 0: # check for positive integer
            raise ValueError
    except ValueError:
        print('Invalid value inputted')  # warn invalid input
    else:
        break

towers = Towers(n)  # instantiate towers object
towers.moveSequence(n, 0, 2, 1) # call recursive moving tower function

print('Complete!')  # end game
