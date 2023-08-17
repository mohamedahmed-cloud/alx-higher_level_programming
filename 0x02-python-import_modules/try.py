l = [(x,y) for x in [1,2,3] for y in [1,2,3] if x != y]
vec = [-4, -2, 0, 2, 4]
vec = [abs(x ) for x in vec ]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit = [x.strip()  for x in freshfruit]
print(freshfruit)
vec = [(x, x**2) for x in vec]
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec = [x for y in vec for x in y]
from math import pi
ll = [round(pi,i) for i in range(1,4)]
print(ll)
n = 4
lll =[[0 for x in range(n)] for y in range(n)]
print(lll)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(zip(*matrix))

