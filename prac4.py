'''
Aim: Write a program to implement Page Rank Algorithm.
Note : Install modules with the help of pip
 pip install sklearn 
Then Execute the code prac4.py

'''

import numpy as np
from scipy.sparse import csc_matrix
from fractions import Fraction
def float_format(vector, decimal):
    return np.round((vector).astype(np.float), decimals=decimal)
G = np.matrix([[1,1,0],
               [1,0,1],
               [0,1,0]])

n=len(G)
#print(n)
# transform G into markov matrix A
M = csc_matrix(G,dtype=np.float)
rsums = np.array(M.sum(1))[:,0]
ri, ci = M.nonzero()
M.data /= rsums[ri]

# WWW matrix
# we have 3 webpages and probability of landing to each one is 1/3
#(default Probability)
#n=len(M)
dp = Fraction(1,n)

E = np.zeros((3,3))
E[:] = dp

# taxation
beta = 0.85

# WWW matrix
A = beta * M + ((1-beta) * E)

# initial vector
r = np.matrix([dp, dp, dp])
r = np.transpose(r)

previous_r = r
for it in range(1,30):
    r = A * r
    #check if converged
    if (previous_r==r).all():
        break
    previous_r = r

print ("Final:\n", float_format(r,3))
print( "sum", np.sum(r))
