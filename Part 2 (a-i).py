# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 01:09:01 2023

@author: Mario
"""

from math import prod
from math import log

M = 50
N = int(100 + M)

A = [None]*(N+1)
A[0] = 1.0

for i in range(1, len(A)-1):
    A[i] = (N + 1 - i)/i
    
possible_comb = []

for k in range(1, len(A)):
    num_k_comb = prod(A[:k])
    possible_comb.append(num_k_comb)
possible_comb.append(1.0)

all_comb = sum(possible_comb)
Pr = []

for k in range(0, len(possible_comb)):
    pr = possible_comb[k]/all_comb
    Pr.append(pr)
    
print(Pr[10])
print(Pr[int(N/2)])
print(sum(Pr[int(N/2)-5:int(N/2)+6]))
print(sum(Pr[int(N/2)-25:int(N/2)+26]))

kB = 1.380649e-23
S = []

for k in range(0, len(possible_comb)):
    S.append(kB*log(possible_comb[k]))
    
print(S[int(N/2)+10] - S[int(N/2)])
print(S[int(N/2)+5] - S[int(N/2)])
print(S[int(N/2)] - S[2])

print("The expected number of tosses to get a 2-combination is " + str(1/Pr[2]))

print("it is " + str(possible_comb[int(N/2)]/possible_comb[M])
      + " times more likely to obtain N/2 than M heads.")