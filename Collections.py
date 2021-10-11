#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

_ = raw_input()

counter = Counter(raw_input().split())

n = raw_input()
money = 0

for _ in range(int(n)):
    number, price = raw_input().split()
    if number in counter:
        counter[number] -= 1
        if counter[number] == 0:
            del counter[number]
        money += int(price)

print(money)

#DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict

n, m = input().split()

d = defaultdict(list)
for x in range(int(n)):
    d['A'].append(input())
for x in range(int(m)):
    word = input()
    indexs = [index for index, value in enumerate(d['A']) if value == word]
    if indexs == []:
        print(-1)
    else:
        out = ""
        for x in range(len(indexs)):
            if x == 0:
                out += str(indexs[x]+1)
            else:
                out += ' ' + str(indexs[x]+1)
        print(out)

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Spreadsheet = namedtuple('Spreadsheet', input().split())
count = 0
for x in range(n):
    a,b,c,d = input().split()
    st = Spreadsheet(a,b,c,d)
    count += int(st.MARKS)
print(count/n)

#Collections.OrderedDict()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

orderedDict = OrderedDict()
for x in range(n):
    command = input()
    product = ' '.join([x for x in command.split() if x.isalpha()])
    price = int(''.join([x for x in command.split() if x.isnumeric()]))
    if product not in orderedDict:
        orderedDict[product] = price
    else:
        orderedDict[product] += price

for x in orderedDict:
    print(x + ' ' + str(orderedDict[x]))

#Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

OD = OrderedDict()

for x in range(n):
    word = input()
    if word in OD:
        OD[word] += 1
    else:
        OD[word] = 1

print(len(OD))
print(' '.join(map(str, list(OD.values()))))

#Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())

dq = deque()

for _ in range(n):
    command = input().split()
    if len(command) == 1:
        if(command[0] == 'pop'):
            dq.pop()
        else:
            dq.popleft()
    else:
        if(command[0] == 'append'):
            dq.append(command[1])
        else:
            dq.appendleft(command[1])

print(' '.join(list(dq)))

#Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    inp = (input())
    s = dict(Counter(list(inp))).items()   
    s = sorted(s, key=lambda l: (-l[1], l[0]))[:3]
    for let, num in s:
        print(let, num, sep=' ')
    
    
#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(input())

for _ in range(t):
    _ = input()
    aux = input().split()
    dq = deque()
    dq.extend(aux)
    #print("INITIAL: ", dq)
    aux = True
    lastpop = float('inf')
    while aux and len(dq) > 0:
        if len(dq) == 1:
            last = dq.pop()
            #print("last: ", last)
            #print("lastpop: ", lastpop)
            if last > lastpop:
                aux = False
        else:
            l = int(dq.popleft())
            r = int(dq.pop())
            #print("l: ", l)
            #print("r: ", r)
            #print("lastpop: ", lastpop)
            if l > lastpop and r > lastpop:
                #print("FAIL")
                aux = False
            elif l <= lastpop and r <= lastpop:
                if l >= r:
                    dq.append(r)
                    lastpop = l
                else:
                    dq.appendleft(l)
                    lastpop = r
            else:
                aux = False
            
            #print("After: ", dq)
    if(aux):
        print("Yes")
    else:
        print("No")


    

