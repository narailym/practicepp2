#1operaters
print(500 > 98)
print(6 == 3)
print(6.2233 < 7)


#1.1
f = 9.002
h = 9.001
if f < h:
    print("f is less than h")
else:
    print("nooo,is not")

print(bool("Help"))
print(bool(56666))


u = "help"
l = 56666
print(bool(u))
print(bool(l))

class job():
    def __len__(self):
        return 0
fni = job()
print(bool(fni))    

def makefunof():

    return True
print(makefunof())


def makefunof():
    return True

if makefunof():
    print("da")
else:    
    print("net")

i = 899
print(isinstance(i, str))#its false



#2Lists
y = 7
o = 4
print(y ** 4)
print(y % o)
print(67 // 9)


k = 18
k &= 5
print(k)

o = 98
print(o > 97 and o < 599)
print(o < 78 or o < 377)
print(not(o > 4 and o < 100))

o2 = ["lolipop", "cakepop"]
i = ["lolipop", "cakepop"]
u = o2
print(o2 is i)
print(o2 is u)
print(o2 == i)

print(12 & 2)#and
print(8 | 4)#or
print(9 ^ 8)#xor
print(~ 2)

#2.1
hollywood = ["films","movie","series","doramas"]
print(hollywood)

hollywood = ["films","movie","series","doramas"]
print(len(hollywood))

list1st = ["home","family","dinner"]
print(type(list1st))

hollywood = list(("films","movie","series","doramas"))
print(hollywood)


#2.2
hollywood = ["films","movie","series","doramas"]
print(hollywood[2])

hollywood = ["films","movie","series","doramas"]
print(hollywood[-3])


hollywood = ["films","movie","series","doramas"]
print(hollywood[1:3])

hollywood = ["films","movie","series","doramas","TV shows"]
print(hollywood[:4])

hollywood = ["films","movie","series","doramas","TV shows"]
print(hollywood[1:])

hollywood = ["films","movie","series","doramas","TV shows"]
print(hollywood[-3:-1])

hollywood = ["films","movie","series","doramas","TV shows"]
if "triology" in hollywood:
    print("YES")
else:
    print("there is is nothing like that, psycho")





#2.3
nolisten = ["pop","r&b","rock"]
nolisten[2] = "fonk"
print(nolisten)
 
nolisten = ["pop","r&b","rock","metall","remix"]
nolisten[0:2] = ["kpop","qpop"]
print(nolisten)

nolisten = ["pop","r&b","rock","metall","remix"]
nolisten[0:3] = ["kpop"]
print(nolisten)


nolisten = ["pop","r&b","rock","metall","remix"]
nolisten.insert (3, "jpop")
print(nolisten)



#2.4
nolisten = ["pop","r&b","rock","metall","remix"]
nolisten.append("kpop")
print(nolisten)

nolisten = ["pop","r&b","rock","metall","remix"]
yes = ["kpop","qpop"]
nolisten.extend(yes)
print(nolisten)

nolisten = ["pop","r&b","rock","metall","remix"]
yes = ("kpop","qpop")
nolisten.extend(yes)
print(nolisten)


#2.5
ios = ["iphone","ipad","aispods1999"]
ios.remove("iphone")
print(ios)

ios = ["iphone","ipad","aispods1999"]
ios.pop(2)
print(ios)


ios = ["iphone","ipad","aispods1999"]
del ios[1]
print(ios)


ios = ["iphone","ipad","aispods1999"]
ios.clear()
print(ios)




#2.6
numbers = ["one", "twelve", "ten"]
for y in numbers:
    print (y)


numbers = ["one", "twelve", "ten"]
for o in range(len(numbers)):
    print(numbers[o])


numbers = ["one", "twelve", "ten"]
p = 0
while p < len(numbers):
    print(numbers[p])
    p += 1


numbers = ["one", "twelve", "ten"]
[print(i) for i in numbers]


#2.7
diction = ["soz","kitap","sozdik","aryp"]
newd = [i for i in diction if "o" in i]
print(newd)

diction = ["soz","kitap","sozdik","aryp"]
newd = [i for i in diction if i != "z"]
print(newd)

op = [i for i in range(9)]
print (op)

op = [i for i in range(9) if i > 4]
print (op)


diction = ["soz","kitap","sozdik","aryp"]
newd = [i.upper() for i in diction]
print(newd)

diction = ["soz","kitap","sozdik","aryp"]
newd = ["yes" for i in diction]
print(newd)


diction = ["soz","kitap","sozdik","aryp"]
newd = [i if i != "soz" else "kalam" for i in diction]
print(newd)

g_alpha = ["lambda","tetta","omega","alfa","beta","etta"]
g_alpha.sort(reverse = True)
print(g_alpha)


def fc(x):
    return abs(x - 40)
you = [5, 6, 92, 36, 566]
you.sort(key = fc)
print(you)

g_alpha = ["lambda","Tetta","omega","Alfa","beta","Etta"]
g_alpha.sort()
print(g_alpha)


g_alpha = ["lambda","Tetta","omega","Alfa","beta","Etta"]
g_alpha.sort(key = str.lower)
print(g_alpha)


g_alpha = ["lambda","Tetta","omega","Alfa","beta","Etta"]
g_alpha.reverse()
print(g_alpha)




#2.8
stuff = ["note", "pen", "pencil"]
newstaff = stuff.copy()
print(newstaff)

stuff = ["note", "pen", "pencil"]
newstaff = list(stuff)
print(newstaff)

stuff = ["note", "pen", "pencil"]
price = [345, 100, 30]
add = stuff + price
print(add)

stuff = ["note", "pen", "pencil"]
price = [345, 100, 30]

for i in price:
    stuff.append(i)
print(stuff)

stuff = ["note", "pen", "pencil"]
price = [345, 100, 30]
stuff.extend(price)
print(stuff)


#tuple
tuple1 = ("a","b","b","a")
print(len(tuple1))

tuple2 = ("abcd",)
print(type(tuple2))

tuple2 = ("abcd")
print(type(tuple2))

#acces tuple
tup = ("pjf", "fhdih", "sdji")
print(tup[2])


tup = ("pjf", "fhdih", "sdji")
print(tup[-2])

tup = ("pjf", "fhdih", "sdji", "jfis", "pspo")
print(tup[:3])


#update

ip = ("lc","ms","kb","bo")
op = list(ip)
op[0] = "lo"
ip = tuple(op)

print(ip)
#add items


pe = ("lc","ms","kb","bo")
j = list(pe)
j.append("sos")
pe = tuple(j)
print(pe)

#addutpletotuple
pe = ("lc","ms","kb","bo")
j = ("sos",)
pe += j
print(pe)

#remove

pe = ("lc","ms","kb","bo")
j = list(pe)
j.remove("ms")
pe = tuple(j)
print(pe)
 
 #unpack
io = ("k", "a", "p", "p", "p")
(kletter, aletter, *pletter) = io
print(kletter)
print(aletter)
print(pletter)
#loop
ple = ("lo", "xo", "yo")
for y in ple:
  print(y)

ple = ("lo", "xo", "yo")
for y in range(len( ple)):
  print(ple[y])

ple = ("lo", "xo", "yo")
y = 1
while y < len( ple):
  print(ple[y])
  y += 1


#join
obj = ("plus", "minus", "addition")
multple = obj * 2

print(multple)

#sets

my = {"only", "one", "one", "only"}

print(my)


my = {"only", "one", "one", "only"}

print(len(my))

#access items

ofo = {"kleo", "patra", "patrick","ta"}
print("ta" in ofo)

ofo = {"kleo", "patra", "patrick","ta"}
print("op" not in ofo)

#add items
ofo = {"kleo", "patra", "patrick","ta"}
ofo.add("aa")
print(ofo)

ofo = {"kleo", "patra", "patrick","ta"}
jk = {"jlo", "shakira", "selena"}
ofo.update(jk)
print(ofo)

ofo = {"kleo", "patra", "patrick","ta"}
ofo.remove("patra")
print(ofo)

ofo = {"kleo", "patra", "patrick","ta"}
ofo.discard("ta")
print(ofo)

ofo = {"kleo", "patra", "patrick","ta"}
p = ofo.pop()
print(p)
print(ofo)


ofo = {"kleo", "patra", "patrick","ta"}
for i in ofo:
    print(i)

#join

or1 = {"'",".",":"}
or2 = {"{", "*","&"}

or3 = or1.union(or2)
print(or3)

or1 = {"'",".",":"}
or2 = {"{", "*","&"}

or3 = or1 | or2 #means | union
print(or3)



o = {"'",".",":"}
r = {"{", "*","&"}

i = o.union(r)
print(i)

#dictionaries

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp"
}
print(st1)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp"
}
print(st1["tel"])


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
    "ios" : "airdots"
}
print(len(st1))

st1 = dict(ios = "iphone",tel = "blackberry",linux = "comp")

print(st1)

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
    "ios" : "airdots"
}
p = st1.get("ios")
print(p)

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
    "ios" : "airdots"
}
p = st1.keys()
print(p)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
    "ios" : "airdots"
}
p = st1.keys()
print(p)
st1["laptop"] = "acer"
print(p)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
p = st1.values()
print(p)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
p = st1.values()
print(p)
st1["laptop"] = "op"
print(p)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
p = st1.items()
print(p)

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
p = st1.items()
print(p)
st1["laptop"] = "lp"
print(p)

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
if "ios" in st1:
    print("yeesss")

#change

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
st1["tel"] = "nokialegendary"
print(st1)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
st1.update({"tel" : "nokia"})
print(st1)

#add
st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
st1["ko"] = "dary"
print(st1)
#remove

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
st1.pop("tel")
print(st1)

st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
st1.popitem()
print(st1)


st1 = {
    "ios":"iphone",
    "tel" : "blackberry",
    "linux" : "comp",
}
del st1["ios"]
print(st1)

#loop


ppap = {
    "pen" :"apple",
    "applepen" : "pineapple",
    "pineapplepen" : "penpineappleapplepen"
    }
for x in ppap:
    print(ppap[x])

ppap = {
    "pen" :"apple",
    "applepen" : "pineapple",
    "pineapplepen" : "penpineappleapplepen"
    }
for x in ppap.values():
    print(x)

ppap = {
    "pen" :"apple",
    "applepen" : "pineapple",
    "pineapplepen" : "penpineappleapplepen"
    }
for x in ppap.keys():
    print(x)


ppap = {
    "pen" :"apple",
    "applepen" : "pineapple",
    "pineapplepen" : "penpineappleapplepen"
    }
for x, p in ppap.items():
    print(x, p)



#if else

a = 45
b = 5
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

a = 5.66
b = 7
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


nine = 9
fifty = 54
print("xxx") if nine > fifty else print("lll")

l = 88
m = 25
n = 100
if l > m and n > l:
  print("Botharetrue")


l = 88
m = 25
n = 100
if l > m or n > l:
  print("one of true")

#while loops

add = 6
while add < 10:
   print(add)
   add += 2


f = 3
while f < 15:
    print(f)
    if f == 9:
       break
    f += 3   



lp = 0
while lp < 20:
    lp += 4
    if lp == 15:
        continue
    print(lp)


u = 2
while u < 7:
   print(u)
   u += 1
else:
   print("u is no longer less than 7")


#for loops
for  i in "lalaplolaza":
    print(i)


took = ["shelter", "ceremony", "practice", "time"]
for i in took:
   print(i)
   if i == "ceremony":
      break
   


took = ["shelter", "ceremony", "practice", "time"]
for i in took:
   if i == "ceremony":
      break
   print(i)


took = ["shelter", "ceremony", "practice", "time"]
for i in took:
   if i == "practice":
      continue
   print(i)



for i in range(9, 15):
    print(i)

for t in range(9, 36, 6):
   print(t)



for h in range(23):
   if h == 21:
      break
   print(h)
else:
   print("finish!!!")


jop = ["obo", "pfok","pfjp"]
pf = ["fj","al", "pow"]
for u in jop:
   for o in pf:
      print(u, o)