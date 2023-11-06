# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 17:54:58 2023

@author: Mario
"""

import time

start = time.time()
#elapsed = 0

N = 6

num_list = []
    
for i in range(0, 2**N):
    num_list.append(bin(i))
    
end = time.time()

print(num_list)
print(end - start)