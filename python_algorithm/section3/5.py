n = int(input())
arrN =list(map(int,input().split()))
m = int(input())
arrM = list(map(int,input().split()))
result = []

while(arrN!=[] and arrM!=[]):
    if arrN[0] <= arrM[0]:
        result.append(arrN.pop(0))
    elif arrN[0] >= arrM[0]:
        result.append(arrM.pop(0))
    if arrN==[] or arrM == []:
        result += arrN
        result += arrM


[ print(i, end=" ") for i in result ]