#Array Mathematics
import numpy

n, m = input().split()
a = [numpy.array(list(map(int,input().split())), int)]
b = [numpy.array(list(map(int,input().split())), int)]

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.array(numpy.divide(a,b), int))
print(numpy.mod(a,b))
print(numpy.power(a,b))

#Arrays


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr, float)[::-1]

#Shape and Reshape

import numpy



arr = numpy.array(list(map(int,input().split())))
print(numpy.reshape(arr,(3,3)))

#Transpose and Flatten

import numpy

n, m = input().split()

arr = numpy.array([input().split() for _ in range(int(n))], int)

print(numpy.transpose(arr))
print(arr.flatten())


#Concatenate

import numpy



n, m, p = list(map(int,input().split()))

arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((arr1, arr2), axis = 0)) 


#Zeros and Ones

import numpy



shape = list(map(int,input().split()))

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))

#Eye and Identity

import numpy
numpy.set_printoptions(legacy='1.13')

n, m = list(map(int,input().split()))

print(numpy.eye(n,m))

#Floor, Ceil and Rint

import numpy

numpy.set_printoptions(legacy='1.13')

arr = list(map(float,input().split()))

aux = numpy.floor(arr)
print(aux)
aux = numpy.ceil(arr)
print(aux)
aux = numpy.rint(arr)
print(aux)


#Sum and Prod
import numpy

n,m = list(map(int,input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
    

print(numpy.prod(numpy.sum(arr, axis = 0)))
    
    
#Min and Max

import numpy

n, m = list(map(int,input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
print(numpy.max(numpy.min(arr, axis=1)))

#Mean, Var, and Std
import numpy
n, m = list(map(int,input().split()))

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.around(numpy.std(arr),decimals=11) ) #found numpy.araund in Discussions section


#Dot and Cross

import numpy


n = int(input())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

B = []
for _ in range(n):
    B.append(list(map(int, input().split())))
    

print(numpy.dot(A,B))

#Inner and Outer

import numpy


arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

print(numpy.inner(arr1, arr2))
print(numpy.outer(arr1, arr2))

#Polynomials
import numpy

arr = list(map(float, input().split()))
n = float(input())

print(numpy.polyval(arr, n))

#Linear Algebra

import numpy


n = int(input())

mat = []
for _ in range(n):
    mat.append(list(map(float,input().split())))
print(numpy.around(numpy.linalg.det(mat), decimals=2))
