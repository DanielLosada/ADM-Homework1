#Introduction to Sets



def average(array):
    # your code goes here
    set1 = set(array)
    return sum(set1)/len(set1)

#No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = raw_input().split()

arr = raw_input().split()

A = set(raw_input().split())
B = set(raw_input().split())

countA = [i in A for i in arr]
countB = [i in B for i in arr]


print(sum(countA) - sum(countB))


#Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(raw_input())
set1=set(map(int,raw_input().split()))
m=int(raw_input())
set2=set(map(int,raw_input().split()))


inter = set1.intersection(set2)
part1 = set1 - inter
part2 = set2 - inter
full = part1.union(part2)
full = list(full)
full.sort()
for x in full:
    print(x)

#Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

myset = set()
for _ in range(int(n)):
    myset.add(raw_input())

print(len(myset))

#Set .discard(), .remove() & .pop()

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

myset = set(map(int,raw_input().split()))

m = raw_input()

for x in range(int(m)):
    command = raw_input().split()
    if len(command) == 1:
        myset.pop()
    else:
        if command[0] == "remove":
            myset.remove(int(command[1]))
        elif command[0] == "discard":
            myset.discard(int(command[1]))
    
print(sum(myset))

#Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

english = set(raw_input().split())

m = raw_input()

french = set(raw_input().split())

english.update(french)

print(len(english))

#Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

english = set(raw_input().split())

m = raw_input()

french = set(raw_input().split())



print(len(english.intersection(french)))

#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

english = set(raw_input().split())

m = raw_input()

french = set(raw_input().split())

print(len(english - french))

#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT


# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

english = set(raw_input().split())

m = raw_input()

french = set(raw_input().split())


print(len(english.symmetric_difference(french)))

#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()

mySet = set(map(int,raw_input().split()))

m = raw_input()

for _ in range(int(m)):
    command = raw_input().split()
    command = command[0]
    aux = set(map(int,raw_input().split()))
    if command == "update":
        mySet.update(aux)
    elif command == "symmetric_difference_update":
        mySet.symmetric_difference_update(aux)
    elif command == "difference_update":
        mySet.difference_update(aux)
    else:
        mySet.intersection_update(aux)
print(sum(mySet))

#The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(raw_input())

arr = map(int,raw_input().split())

mySet = set()
auxSet = set()
for x in arr:
    if x in mySet:
        auxSet.add(x)
    else:
        mySet.add(x)

print((mySet - auxSet).pop())

#Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for _ in range(t):
    _ = raw_input()
    A = set(raw_input().split())
    _ = raw_input()
    B = set(raw_input().split())
    print(A == A.intersection(B))

#Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT

mySet = set(raw_input().split())

n = raw_input()

superSet = True
for _ in range(int(n)):
    auxSet = set(raw_input().split())
    if not mySet.intersection(auxSet) == auxSet or len(auxSet.difference(mySet)) != 0:
        superSet = False

print(superSet)
