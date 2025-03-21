squares = []
for i in range(1, 101):
    squares.append(i ** 2)

print(squares)

squares2 = [i ** 2 for i in range(1, 101)]
print(squares2)

remainders5 = [x ** 2 % 5 for x in range(1, 101)]
print(remainders5)

var = [x ** 2 % 11 for x in range(1, 101)]
print(var)

'''
Problem
The problem of finding which numbers appear in the list is Quadratic Reciprocity solved by Gauss
p_remainders = [x**2%p for x in range(1, p)]
len(p_remainders) = (p+1)/2
'''

movies = ["The Shawshank Redemption",
          "The Godfather",
          "The Dark Knight",
          "Pulp Fiction",
          "The Lord of the Rings: The Return of the King",
          "Forrest Gump",
          "Inception",
          "Fight Club",
          "The Matrix",
          "Goodfellas"]

themovies = []
for title in movies:
    if title.startswith("The"):
        themovies.append(title)

print(themovies)

themovies2 = [title for title in movies if title.startswith("The")]
print(themovies2)

'''
find movies released before the year 2000
'''

movies = [("The Shining", 1980),
          ("Star Wars: Episode V - The Empire Strikes Back", 1980),
          ("Raging Bull", 1980),
          ("Goodfellas", 1990),
          ("Home Alone", 1990),
          ("Dances with Wolves", 1990),
          ("Gladiator", 2000),
          ("Memento", 2000),
          ("Requiem for a Dream", 2000),
          ("The Blues Brothers", 1980),
          ("Total Recall", 1990),
          ("Cast Away", 2000)]

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

#Scalar mutiplication
v = [2, -3, 1]
print(4 * v)

w = [4 * x for x in v]
print(w)

#cartesian Product
'''
If A and B are sets, then the Cartesian product is the set of pairs (a,b)
where a is in A and b is in B.
'''

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)

