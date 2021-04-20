def reverse(x):
    result = []
    for i in x:
        num = str(i)
        result.append(int(num[::-1]))
    return result

def isPrime(x):
    rev = reverse(x)
    maxResult = max(rev)
    arr = [True for i in range(maxResult+1)]
    arr[1] = False
    for i in range(2,maxResult+1):
        if arr[i] == True:
            for j in range(i+i, maxResult+1, i):
                arr[j] = False

    for i in rev:
        if arr[i] == True :
            print(i)

n = input()
x = list(map(int,input().split()))
isPrime(x)