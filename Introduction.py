#Say "Hello, World!" With Python

if __name__ == '__main__':
    print "Hello, World!"

#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 == 1 :
        print("Weird")
    else:
        if n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")

#Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)

#Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(int(a/b))
    print(a/b)

#Loops

if __name__ == '__main__':
    n = int(raw_input())
    for x in range(0,n):
        print(x*x)

#Write a function
def is_leap(year):
    leap = False
    if year%4 == 0:
        if(not year%100 == 0):
            leap = True
        else:
            if(year%400 == 0):
                leap = True
    # Write your logic here
    
    return leap

#Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    aux = "1"
    for x in range(2,n):
        aux += str(x)
    if(not n == 1):
        aux += str(n)
    print(aux)
