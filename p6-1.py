# import math 
import numpy as np
import nnfs

nnfs.init()

layer_outputs = [[4.8, 1.21, 2.385],
                 [8.9, -1.81, 0.2],
                 [1.41, 1.051, 0.026]]
'''
# E = 2.718
E = math.e
'''

exp_values = np.exp(layer_outputs)

print(np.sum(layer_outputs, axis=1)) # axis=none --> add_all, axis = 0 --> add_column, axis = 1 --> add_row
'''
exp_values = []

for output in layer_outputs:
    exp_values.append(E**output)
'''

# norm_values = exp_values / np.sum(exp_values)

'''
norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)
'''
# print(norm_values)
