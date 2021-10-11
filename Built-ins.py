#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = list(map(int,input().split()))

l = []

for _ in range(x):
    l.append(list(map(float, input().split())))

l = list(zip(*l))
for i in range(len(l)):
    print(sum(l[i])/x)

#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x: x[k])
    for x in arr:
        aux = map(str, x)
        print(' '.join(aux))

#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

lower = [x for x in s if x.islower()]
upper = [x for x in s if x.isupper()]
odd = [x for x in s if x.isdigit() and int(x)%2 == 1]
even = [x for x in s if x.isdigit() and int(x)%2 == 0]

lower.sort()
upper.sort()
odd.sort()
even.sort()

lower = ''.join(lower)
upper = ''.join(upper)
odd = ''.join(odd)
even = ''.join(even)

print(lower + upper + odd + even)

#print(''.join(lower.sort()) + ''.join(upper.sort()) + ''.join(odd.sort()) + ''.join(even.sort())) 
