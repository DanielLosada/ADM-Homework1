#sWAP cASE

def swap_case(s):
    return s.swapcase()

#String Split and Join
def split_and_join(line):
    return "-".join(line.split(" "))

#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")
    # Write your code here

#Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

#Find a string

def count_substring(string, sub_string):
    count = 0
    sublen = len(sub_string)
    for x in range(0, len(string)):
        if string[x:].startswith(sub_string):
            count += 1
        
    return count

#String Validators

if __name__ == '__main__':
    s = raw_input()
    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    
    for x in s:
        if x.isalnum():
            alphanum = True
        if x.isalpha():
            alpha = True
        if x.isdigit():
            digit = True
        if x.islower():
            lower = True
        if x.isupper():
            upper = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

#Text Alignment

# Enter your code here. Read input from STDIN. Print output to STDOUT
thickness = int(raw_input())

s = 'H'

for x in range(0,thickness):
    print((s*x).rjust(thickness-1)+s+(s*x).ljust(thickness-1))
    
for x in range(0,thickness+1):
    print((s*thickness).center(thickness*2-1)+(s*thickness).center((thickness*6)+1))
    
for x in range(0,(thickness+1)//2):
    print((s*(thickness*5)).center(((thickness*6))))

for x in range(0,thickness+1):
    print((s*thickness).center(thickness*2-1)+(s*thickness).center((thickness*6)+1))
    
for x in reversed(range(0, thickness)):
    print((' '*thickness*4) + (s*x).rjust(thickness-1) + s + (s*x).ljust(thickness -1))

#Text Wrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string,max_width))

#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int,raw_input().split())

aux = 1
for x in range((n//2)):
    print(('.|.'*aux).center(m,'-'))
    aux += 2
    
print('WELCOME'.center(m,'-'))

aux = n-2
for x in reversed(range(1,(n//2)+1)):
    print(('.|.'*aux).center(m,'-'))
    aux -= 2

#String Formatting

def remove0(s):
    for x in s:
        if(x == '0'):
            s = s[1:]
        else:
            return s

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) -2

    for x in range(1, number+1):
        octal = remove0(oct(x))
        hexa = hex(x)[2:].upper()
        bina = bin(x)[2:]
        print((width-len(str(x)))*' ' + str(x) + ' ' + (width-len(octal))*' ' + octal + ' ' + (width-len(hexa))*' ' + hexa + ' ' + (width-len(bina))*' ' + bina )
        
        

#Alphabet Rangoli

def insert_char(string, index, char):
    return string[:index] + char + string[index:]

def next_letter(char, n):
    return chr(ord(char) + n)

def create_line(x,size):
    nlet = size - x
    maxwidth = size*4 - 3
    firstletter = next_letter('a', nlet)
    line = firstletter
    for i in range(1,x):
        nextl = next_letter(firstletter, i)
        line = insert_char(line, 0, '-')
        line = insert_char(line, len(line), '-')
        line = insert_char(line, 0, nextl)
        line = insert_char(line, len(line), nextl)
        
    line = line.center(maxwidth,'-')
    return line

    
    

def print_rangoli(size):
    # your code goes here
    
    for x in range(1,size):
        print(create_line(x, size))
    print(create_line(size,size))
    for x in reversed(range(1,size)):
        print(create_line(x, size))
        
    
    
#Capitalize!

def insert_char(string, index, char):
    return string[:index] + char + string[index:]

# Complete the solve function below.
def solve(s):
    arr = s.split(' ')
    for x in range(0,len(arr)):
        if(arr[x] != ''):
            first = arr[x][0]
            arr[x] = arr[x][1:]
            arr[x] = insert_char(arr[x],0,first.upper())
    arr = ' '.join(arr)
    return arr
        
#The Minion Game
def minion_game(string):
    # your code goes here
    vowels = ['a', 'e', 'i', 'o', 'u']
    sScore = 0
    kScore = 0
    
    for x in range(0, len(string)):
        if string[x].lower() in vowels:#kevin
            kScore += len(string) - x
            
        else:#stuart
            sScore += len(string) - x
    if(sScore > kScore):
        print("Stuart " + str(sScore))
    elif(sScore < kScore):
        print("Kevin " + str(kScore))
    else:
        print("Draw")
    
#Merge the Tools!

def removeRep(subS):
    out = ""
    for y in subS:
        if y not in out:
            out += y
    return out

def merge_the_tools(string, k):
    # your code goes here
    aux = 0
    for x in range(len(string)/k):
        
        subS = string[aux:aux+k]
        print(removeRep(subS))
        aux += k
    






