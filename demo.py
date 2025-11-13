import random
import numpy as np

matrix = [
    ["a", "b", 2],
    ["b", "c", 3],
    ["a", "c", 4],
    ["a", "d", 5],
    ["c", "d", 6]
]
print(matrix)
# def custom_sort(row):
#     num = sorted([i for i in row if isinstance(i, int)])
#     char = sorted([i for i in row if isinstance(i, str)])

# sorted_matrix = []
# for row in matrix:
#     sorted_row = custom_sort(row) 
#     sorted_matrix.append(sorted_row)

# print("Sorted:  ", sorted_matrix)