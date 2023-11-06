# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 02:58:09 2023

@author: Mario
"""

from math import prod
import matplotlib.pyplot as plt

N = 33
# The largest here is N=1028. For N=1030 it 
# yields 'inf' in each entry of possible_comb
# while for N=1029 yields OverflowError

A = [None]*(N+1)
A[0] = 1.0

for i in range(1, len(A)-1):
    A[i] = (N + 1 - i)/i
    
possible_comb = []

for k in range(1, len(A)):
    num_k_comb = prod(A[:k])
    possible_comb.append(num_k_comb)
possible_comb.append(1.0)


fig, ax = plt.subplots()

ax.tick_params(direction="in", length=6)
ax.plot(range(0, len(possible_comb)), possible_comb, "C4", linewidth=1, marker="s", markerfacecolor="none")

ax.set_xlabel('number of H, $k$')
ax.set_ylabel('number of $k$-combinations')

plt.show()