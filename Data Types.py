#List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    aux = [[x,y,z] for x in range(0,x+1) for y in range(0, y+1) for z in range(0,z+1) if x+y+z != n]
    print(aux)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    aux = max(arr)
    while max(arr) == aux:
        arr.remove(aux)
        
    print(max(arr))

#Nested Lists
if __name__ == '__main__':
    names = []
    scores = []
    nested = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        names.append(name)
        scores.append(score)
        nested.append([name, score])
    
    aux = min(scores)
    auxList = scores
    while aux == min(auxList):
        auxList.remove(aux)
    aux = min(auxList)
    
    result = [x for x in nested if x[1] == aux]
    finalNames = map(lambda x: x[0],result)
    finalNames.sort()
    for x in finalNames:
        print(x)
    
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

#List
if __name__ == '__main__':
    result = []
    for _ in range(0, int(raw_input())):
        line = raw_input().split()
        command = line[0]
        line.pop(0)
        
        if(command == "insert"):
            result.insert(int(line[0]), int(line[1]))
        elif(command == "remove"):
            result.remove(int(line[0]))
        elif(command == "append"):
            result.append(int(line[0]))
        elif(command == "pop"):
            result.pop()
        elif(command == "reverse"):
            result.reverse()
        elif(command == "sort"):
            result.sort()
        else:
            print(result)

#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    
    print(hash(tuple(integer_list)))
