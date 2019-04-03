import numpy as np

#file = input()
lines = np.loadtxt('sample.txt', delimiter=", ", comments = '#')

#print(lines)
print(np.corrcoef(lines))
