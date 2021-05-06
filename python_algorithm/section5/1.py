n,m = map(int,(input().split()))

res =[]
strn = str(n)

for i in strn:
 
    while res and m>0 and res[-1]<i:
            res.pop()
            m -= 1
    res.append(i)
if m!= 0:
    res=res[:-m]
res = ''.join(map(str,res))
print(res)