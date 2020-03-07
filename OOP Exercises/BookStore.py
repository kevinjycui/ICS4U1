# Name: Kevin Cui
# Date: 2020-02-05
# Description: Product Class

class Product(object):

    def __init__(self, name, upc, weight, cost):
        self.name = name
        self.upc = upc
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)

class NonConsumable(Product):

    def __init__(self, name, upc, weight, cost, isbn, title):
        self.isbn = isbn
        self.title = title
        Product.__init__(self, name, upc, weight, cost)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; ISBN: '+str(self.isbn)+'; Title: '+str(self.title)

class Consumable(Product):

    def __init__(self, name, upc, weight, cost, expiryDate):
        self.expiryDate = expiryDate
        Product.__init__(self, name, upc, weight, cost)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; Expiry Date: '+str(self.expiryDate)

class Book(NonConsumable):

    def __init__(self, name, upc, weight, cost, isbn, title, author):
        self.author = author
        NonConsumable.__init__(self, name, upc, weight, cost, isbn, title)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; ISBN: '+str(self.isbn)+'; Title: '+str(self.title)+'; Author: '+str(self.author)

class Video(NonConsumable):

    def __init__(self, name, upc, weight, cost, isbn, title, director):
        self.director = director
        NonConsumable.__init__(self, name, upc, weight, cost, isbn, title)
    
    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; ISBN: '+str(self.isbn)+'; Title: '+str(self.title)+'; Director: '+str(self.director)

class CD(NonConsumable):

    def __init__(self, name, upc, weight, cost, isbn, title, artist):
        self.artist = artist
        NonConsumable.__init__(self, name, upc, weight, cost, isbn, title)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; ISBN: '+str(self.isbn)+'; Title: '+str(self.title)+'; Artist: '+str(self.artist)

class Drink(Consumable):

    def __init__(self, name, upc, weight, cost, expiryDate, containerType):
        self.containerType = containerType
        Consumable.__init__(self, name, upc, weight, cost, expiryDate)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; Expiry Date: '+str(self.expiryDate)+'; Container Type: '+str(self.containerType)

class Food(Consumable):

    def __init__(self, name, upc, weight, cost, expiryDate, packagingType):
        self.packagingType = packagingType
        Consumable.__init__(self, name, upc, weight, cost, expiryDate)

    def __str__(self):
        return 'Name: '+str(self.name)+'; UPC: '+str(self.upc)+'; Weight: '+str(self.weight)+'g; Cost: $'+str(self.cost)+'; Expiry Date: '+str(self.expiryDate)+'; Packaging Type: '+str(self.packagingType)

products = [
    Book('Python for Dummies by Elon Zuckergates', 123456789, 10, 14.99, 24680, 'Python for Dummies', 'Elon Zuckergates'),
    Video('Kungfu Cars: Tokyo Drift (2001), Pixworks Animation Studios', 1123581321, 5, 4.99, 3691215, 'Kungfu Cars: Tokyo Drift', 'John Johnson'),
    CD('Have a Java Palooza', 1010101010, 5, 7.00, 2222222, 'Have a Java Palooza', 'Mr. Java'),
    Drink('High-fat camel milk, 200mg calcium', 3141592653, 100, 6.00, '1988-02-07', 'Mega-sized family chug jug'),
    Food('Buttered Beans', 987654321, 40, 2.99, '4000-01-01', 'Can')
]
print('\n'.join(map(str, products)))
