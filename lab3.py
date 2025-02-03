'''#1
def my_ing(gramm):
    ounces = 28.3495231 * gramm
    return ounces
gramm = int(input())
res = my_ing(gramm)
print(res)
#2

def calc(cen):
    cen = (5 / 9) * (F - 32)
    return cen
F  = int(input())
resl=calc(F)
print(resl)
'''
#3
'''
def solve(numheads, numlegs):
    rabb = (numlegs - 2*numheads)/2
    chica = numheads - rabb
    return (rabb, chica)
numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))
'''
#4


#5
'''
from itertools import permutations
def func(k):
    return list(permutations(k))


k = str(input())
print(func(k))
'''
'''#6
def reve(k):
    
    res = k.split()
    res.reverse()
    return " ".join(res)

k = str(input())
print(reve(k))'''
#7
'''
def cons(nums):
    for y in range(len(nums)-1):
        if nums[y]==3 and nums[y+1]==3:
            return True
    return False
print(cons([1, 3, 3]))
print(cons([1, 3, 1, 3]) )
print(cons([3, 1, 3])) 
'''
#8
'''
def spy_game(nums):
    san=[0, 0, 7]
    index=0
    for i in nums:
        if i == san[index]:
            index+=1
            if index == len(san):
                return True
    return False
print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))
'''

#9
'''import math
def opp(r):
    volume = (4/3) * math.pi * r**3
    return volume
r = int(input())
print(opp(r))'''
#11
'''
def funct(lay):
    return lay == lay[::-1]
lay= input()
print(funct(lay))
'''
#10

def func(snd):
    uni = []
    for i in snd:
        if i not in uni:
            uni.append(i)
    return uni       
snd = input()
print(func(snd))

#12
'''
def histogram(st):
    for value in st:
        print('*' * value)
histogram([4, 7, 9])
'''
#13
import random
def gpt():
    inte = random.randint(1,20)
    tryit = 0
    odj = 0
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    while tryit != inte:
        tryit = int(input("take a guess: "))
        odj += 1
        if tryit < inte:
            print("Your guess is too low")
        elif tryit > inte:
            print("Your guess is too high")
    print(f"Good job, {name}! You guessed my number in {odj} guesses!")
gpt()