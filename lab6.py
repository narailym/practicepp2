#1

from functools import reduce
from operator import mul
texts = list(map(int,input().split()))
res = reduce(mul,texts)
print(res)
#2
string = input()
count = 0
counit = 0
for i in string:
    if i.isupper():
        count +=1
    elif i.islower():
        counit += 1
print(f"l = {count} up = {counit}" )
#3
p = input()
if p.lower() == p[::-1].lower():
    print("palindrome")
else:
    print("not palindrom")

#4
import time,math
num = input()
timm = input()
time.sleep(timm/1000)
print(f"answer {math.sqrt(num)}")
#5
text = tuple(map(int,input().split()))
tui = all(text)
print(tui)



#1
import os

path = input()

print("\n", next(os.walk(path))[1])
print("\n", next(os.walk(path))[2])
print("\n", os.listdir(path))

#2
import os

path = input()

print("Exist", os.path.exists(path))
print("Readable", os.access(path, os.R_OK)) 
print("Writeable", os.access(path, os.W_OK)) 
print("executable", os.access(path, os.X_OK)) 


#3

import os
path1 = input()
if os.path.exists(path1):
    dir_name = os.path.dirname(path1)
    file_name = os.path.basename(path1)
    print(f"dirname: {dir_name}\nfilename: {file_name}")
else:
    print("there is no ")


#4
file = input()
with open(file, "r") as file:
    line = file.readlines()
    print(len(line))
#5
pasthf = input()
txt = input()
with open(pasthf, "w") as file:  
    file.write("\n".join(txt)) 

print(f"saved{pasthf}")

#6
import string
for fill in string.ascii_uppercase:
    with open(f"{fill}.txt", "w") as file:
        file.write(f"{fill} yes")

#7
f1st= input()
s2nd = input()
with open(f1st, "r") as ff1st, open(s2nd, "w") as ss2nd:
    ss2nd.write(ff1st.read())
print("Done")

#8
import os
filpath = input()
if os.path.exists(filpath) and os.acces(filpath, os.W_OK):
    os.remove(filpath)
    print("deleted")
else:
    print("not exists")
