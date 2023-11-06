# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 02:36:12 2023

@author: Mario
"""

N = 7

possible_outcomes = [[] for x in range(0, N+1)]
    
for i in range(0, 2**N):
    binary = format(i, '07b')
    for d in binary:
        if d == '1':
            binary = binary.replace(d, 'H')
        elif d == '0':
            binary = binary.replace(d, 'T')
    possible_outcomes[bin(i).count('1')].append(binary)

file = open('possible_outcomes_with_N=7_coins', "w")
for macrostate in possible_outcomes:
    for outcome in macrostate:
        file.write(outcome + ", ")
    file.write("\n")
file.close()