#1
print("Hello, friend. Have a good day,god bless you:)")
#2
if 10000>0:
    print ("ten thousand is greater than zero")
if 40>39:
    print("fourty is greater than thirty nine")
#3
#this is a comment or
"""
this is a comment too
"""
print("cool")
#4
m=5
e="alma"
print(m)
print(e)
#4.1
n_d=3
n_d="grapes"
print(n_d)
#4.2
r=str(8)
i=int(8)
p=float(8)
print(r)
print(i)
print(p)
x=15
o="day"
print(type(x))
print(type(o))
#4.3
y,o,k = "I", "see", "you"
print(y)
print(o)
print(k)
u = r = f = "my friend"
print(u)
print(r)
print(f)
#4.4
programming_languages=["C++","JavaScript","Pytonchik"]
a, i, c=programming_languages
print(a)
print(i)
print (c)
#4.5
p="Let"
o="it"
l="goooo"
print(p, o, l)
p="Let"
o="it"
l="goooo"
print(p+o +l)
l=9 
v=9
print(l+v)

#4.5
person="Kleo"

def funk():
  print("her name is " + person)

funk()

adj="gorgeous"

def sen():
  adj="special"
  print("You are " + adj)

sen()

print("you are " + adj)
#4.6 global
def functioni():
   global ios
   ios="six"
functioni()
print("there are " + ios + " guys in this club")

men="nine"
def function():
   global men
   men="seven"
function()
print("there are " + men + " guys in this club")
#5
j=7
k=800.9
l=23j
i=float(j)
m=int(k)
g=complex(l)
print(i, m, g)
#5.1
import random
print(random.randrange(4, 9))
#6
l=int(6)
p=int(0.88)
i=int("90")
print(l, p, i)
c=float(3)
k=float(3.90)
y=float("4.90")
print(c, k, y)
#7
text="""Fish in the sea, you know how I feel
River running free, you know how I feel
Blossom in the trees, you know how I feel
"""
print(text)
text1="array"
print(text1[4])

for i in "language":
   print (i)


text2="great"
print(len(text2))

example = "I'm feeling good"
print("pop" in example)
print("good" in example)

example = "I'm feeling good"
if "feeling" in example:
   print("yia, 'feeling' bar")

example = "I'm feeling good"
print("good" not in example)

example = "Im feeling good"
if "and" not in example:
   print("zhok, 'and' tabylmady")

#7.1
go="eagle"
print(go.upper())
go="eAgLLLLe"
print(go.lower())
go="     eagle !  "
print(go.strip())
go="eagle"
print(go.replace("e", "E"))

i="fridge"
p="empty"
h=i+p
print(h)
i="fridge"
p="empty"
h=i+ " "+ p
print(h)
san= 90
tx=f"he is {san} years old"
print(tx)
tx=f"he is {6+8} years old"
print(tx)
uo="just \"relax\" for a minute"
print(uo)