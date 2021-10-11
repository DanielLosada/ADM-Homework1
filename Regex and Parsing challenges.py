#Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for _ in range(t):
    aux = re.search(r'^[-+]?[0-9]*\.[0-9]+$', input())
    print(bool(aux))

#Re.split()

regex_pattern = r"[.,]"	# Do not delete 'r'.

#Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

m = re.search(r'([a-z0-9A-Z])\1', s)

if m :
    print(m.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

match = re.findall(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)

for x in match:
    print(x)
if len(match) == 0:
    print('-1')

#Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for x in range(n):
    s = input()
    s = re.sub(r"(?<=[ ])&{2}(?=[ ])", 'and', s)
    s = re.sub(r"(?<=[ ])\|{2}(?=[ ])", 'or', s)
    print(s)

#Validating Roman Numerals
regex_pattern = r"[MDCLXVI]+"	# Do not delete 'r'.

#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for x in range(n):
    s = input()
    if bool(re.match(r'^[789]{1}[0123456789]{9}$', s)):
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

n = int(input())

for x in range(n):
    name, em = input().split()
    aux = bool(re.search(r'[<][A-Za-z][A-Za-z0-9._-]*[@][A-Za-z]+[.][A-Za-z]{1,3}[>]', em))
    if aux:
        print(name + ' ' + em)

#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for x in range(n):
    s = input()
    
    #aux = re.findall(r'[#]([0123456789ABCDEFabcdef]{3}(?!\w)|[0123456789ABCDEFabcdef]{6}(?!\w))', s)
    
    aux = re.findall(r'[#]([0123456789ABCDEFabcdef]{3}(?=[;,)])|[0123456789ABCDEFabcdef]{6}(?=[;,)]))', s)
    for i in aux:
        print('#' +i)

#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    s = input()
    valid = True
    aux = re.findall(r'[A-Z]', s)
    if len(aux) < 2:
        valid = False
    aux = re.findall(r'[0-9]', s)
    if len(aux) < 3:
        valid = False
    aux = s.isalnum()
    if not aux:
        valid = False
    if len(s) != 10:
        valid = False
    if not len(set(s)) == len(s):
        valid = False

    if valid:
        print("Valid")
    else:
        print("Invalid")
    




