#1
def moci(movies):
    return movies["imdb"] > 5.5
 #2
def iop(movies):
    res = []
    for i in movies:
        if i["imdb"] > 5.5:
            res.append(i)
    return res

#3
def gpt(movies, category):
    res = []
    for dap in movies:
        if dap["category"] == category:
            res.append(dap)
    return res


#4
def ave(movies):
    total = 0
    for i in movies:
        total += i["imdb"]
    return total/len(movies)


#5
def aveact(movies, category):
    catmovies = []
    for i in movies:
        if i["category"] == category:
            catmovies.append(i)
    tot = 0
    for i in catmovies:
        tot += i["imdb"]
    return tot/len(catmovies)
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(moci(movies[9]))




obsh = iop(movies)
for i in obsh:
    print(i["name"],"-", i["imdb"])


ppap = gpt(movies, "Thriller")
for dap in ppap:
    print(f"{dap['name']} - {dap['imdb']}")

print(ave(movies))

print(aveact(movies, "Romance"))