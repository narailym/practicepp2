#1
'''
def nums(n):
    for i in range(1, n+1):
        yield i**2
n = int(input())
for y in nums(n):
    print(y)
#2
def even(innout):
    for u in range(innout):
        if u % 2 == 0:
            yield u

innout = int(input())
for y in even(innout):
    print(y)

#3
def func(m):
    for i in range(m):
        if i % 3 == 0 and i % 4 == 0:
            yield i
m = int(input())
for io in func(m):
    print (io)
#4
def between(a, b):
    for inn in range(a, b):
        yield inn ** 2

a = int(input())
b = int(input())
for i in between(a, b):
    print (i)

#5
def imple(n):
   while n >= 0:
       yield n
       n-= 1

n = int(input())
for i in imple(n):
    print(i)
'''
#math
'''
import math
def rad(n):
    torad = (n * math.pi)/180
    return torad


n = float(input("Input degree: ")) 
print(f"Output radian: {rad(n)}")'''

#2
'''
import math
def uni(h, firstval, secval):
    area = (h* (firstval+secval))/2
    return area
h = int(input("Height: "))
firstval = int(input("Base, first value: "))
secval = int(input("Base, second value: "))
print(f"Expected Output: {uni(h, firstval, secval)}")'''

#3
'''
import math
def polygon(n,s):
    areap = ((n*s**2)*math.tan(math.pi/n))/4
    return areap


n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {polygon(n,s)}")
#4
n = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
areapara = n*h
print(f"Expected Output: {areapara}")'''

'''date = datetime.datetime.today()-datetime.timedelta(days=5)
print(date)
'''
from datetime import datetime, timedelta
nowday = datetime.today()
yestr = nowday - timedelta(1)
tomorrow = nowday + timedelta(1)
print("Yesterday = ", yestr.strftime('%d-%m-%Y'))
print("Today = ", nowday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))
#3
from datetime import datetime
day =datetime.now()
print("org: ", day)

daymicro = day.replace(microsecond=0)
print("without microsec: ", daymicro)
#4
from  datetime import datetime
start = datetime.strptime("8:56:35", "%H:%M:%S")
end = datetime.strptime("20:45:25", "%H:%M:%S")

diff = end - start

print("diff in seconds: ", diff.total_seconds(), "seconds")


#json
import json

with open("text.json") as json_file:
    a = json.load(json_file)

print(f"{'DN':<60} {'Description':<20} {'Speed':<10}")
print("-" * 90)

for item in a["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "N/A"
    speed = attributes["speed"]
    print(f"{dn:<60} {descr:<20} {speed:<10}")
