#Map and Lambda Function

cube = lambda x: x * x * x# complete the lambda function 

def fibonacci(n):
    arr = []
    for x in range(n):
        if x == 0:
            arr.append(0)
        elif x == 1:
            arr.append(1)
        else:
            arr.append(arr[x-1] + arr[x-2])
    return arr

