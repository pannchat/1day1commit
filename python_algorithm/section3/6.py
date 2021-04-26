n , m = map(int,input().split())
l = list(map(int,input().split()))
count = 0
lt = 0
rt = 1
tot = l[0]
while(True):
    if tot < m:
        if rt < n:
            tot += l[rt]
            rt += 1
        else:
            break
    elif tot == m:
        count += 1 
        tot -= l[lt]
        lt+=1
    else:
        tot -= l[lt]
        lt+=1
    

print( count )