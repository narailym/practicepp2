#1
'''
class Str_toup:
    def __init__(self):
        self.text = ""
    def get(self):
        self.text = input()
    def pribt(self):
        print(self.text.upper())
strobj = Str_toup()
strobj.get()
strobj.pribt()'''
#2
'''
class shape:
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
shape11 = shape()
print(shape11.area())  

square11 = square(5)
print(square11.area()) 
'''
#3
'''
class shape:
    def area(self):
        return 0
class rect(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectan = rect(5, 6)
print(rectan.area())'''
#4
'''
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("Point:", self.x, self.y)
    
    def move(self, zh_x, zh_y):
        self.x = zh_x
        self.y = zh_y
    
    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
point1 = Point(2, 3)
point2 = Point(6, 8)
point1.show()
point2.show()
print("d = ",point1.distance(point2))
'''

#5
import math
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposi(self, amnt):
        self.balance += amnt
        print("Deposid:", amnt, "Newbalance:", self.balance)
    
    def withdraw(self, amnt):
        if amnt > self.balance:
            print("aksha zhetkiliksiz")
        else:
            self.balance -= amnt
            print("withdraw:", amnt, "Newbalance:", self.balance)

account = Account("Ali", 125)
print("Owner:", account.owner)
print("Initbalance:", account.balance)
account.deposi(60)
account.withdraw(20)  
account.withdraw(500)
#6
def is_p(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nums = list(range(1, 21)) 
prime_nums = list(filter(lambda x: is_p(x), nums))
print("Prime num:", prime_nums)