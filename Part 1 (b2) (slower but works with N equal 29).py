# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:44:24 2023

@author: Mario
"""

import time

start = time.time()
#elapsed = 0

N = 28

num_list = [[] for x in range(0, N+1)]

#while elapsed < 300:
    
for i in range(0, 2**N):
    #num_list[bin(i).count('1')].append(format(i, '010b'))
    num_list[bin(i).count('1')].append(bin(i))
        #elapsed = time.time() - start
    
end = time.time()

#print(num_list)
print(end - start)