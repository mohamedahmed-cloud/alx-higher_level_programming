#!/usr/bin/python3

mat = [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
new_mat = [row[:] for row in mat]
mat[0][0] = 3

print(new_mat)