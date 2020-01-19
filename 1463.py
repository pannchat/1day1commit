a = int(input())
l1 = [0,0,1,1]

for i in range(4, a+1):
    l1.append(l1[i-1]+1) #d[i]에 저장

    if(i%2==0): #2로나눠지면
        l1[i]=min(l1[i],l1[i//2]+1)
    if(i%3==0):
        l1[i]=min(l1[i],l1[i//3]+1)
print(l1[a])