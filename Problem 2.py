#Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    aux = Counter(candles)
    return aux[max(list(aux.keys()))]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):

    if(x1%2 == 0 and x2%2 != 0 and v1%2 == 0 and v2%2 == 0):
        return "NO"
    elif(x2%2 == 0 and x1%2 != 0 and v1%2 == 0 and v2%2 == 0):
        return "NO"
    while True:
        if (x1 == x2): 
            return "YES"
        elif(x1 > x2 and v1 > v2):
            return "NO"
        elif (x1 < x2 and v1 < v2):
            return "NO"
        x1 += v1
        x2 += v2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    ppl = 5
    count = 0
    for i in range(n):
        ppl = int(ppl/2)
        count += ppl
        ppl *= 3
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def sumaP(p, acc):
    if len(p) == 1:
        suma = acc + int(p)
        return suma
    else:
        return sumaP(p[1:], acc + int(p[:1]))
    

def superDigit(n, k):
    # Write your code here
    p = n*k
    while(len(p) != 1):
        p = str(sumaP(p,0))
    return p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[n-1]

    for x in reversed(range(len(arr)-1)):
        #print("arr[x]: ", arr[x])
        #print("val: ", val)
        if (arr[x] > val):
            arr[x+1] = arr[x]
            if(x == 0):
                print(' '.join(list(map(str,arr))))
                arr[x] = val
            print(' '.join(list(map(str,arr))))
        else:
            arr[x+1] = val
            print(' '.join(list(map(str,arr))))
            break
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    # Write your code here
    #print("N: ", n)
    #print("arr: ", arr)
    val = arr[n-1]

    for x in reversed(range(len(arr)-1)):
        #print("arr[x]: ", arr[x])
        #print("val: ", val)
        if (arr[x] > val):
            arr[x+1] = arr[x]
            if(x == 0):
                arr[x] = val
                return arr
        else:
            arr[x+1] = val
            return arr
        
def insertionSort2(n, arr):
    for x in range(1,len(arr)):
        aux = arr[:x+1]
        aux2 = arr[x+1:]
        aux = insertionSort1(len(aux), aux)
        arr = aux + aux2
        print(' '.join(list(map(str,arr)))) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
