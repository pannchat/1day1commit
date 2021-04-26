def s():
    arr = [list(map(int,input().split())) for _ in range(9)]
    cs=0
    ce=2
    rs=0
    re=2
    count = 0
    while(not(cs==9)):
        tmp=set()
        for i in range(cs,ce+1):
            for j in range(rs,re+1):
                tmp.add(arr[i][j])
                
        else:
            if(len(tmp) != 9):
                return False

            if(rs==6 and re==8):
                cs += 3
                ce += 3
                rs=0
                re=2
            else:
                rs += 3
                re += 3
    for i in range(9):
        ch1 = [0]*9
        ch2 = [0]*9
        for j in range(9):
            ch1[arr[i][j] -1] = 1
            ch2[arr[j][i] -1] = 1
        if(sum(ch1)!= 9 or sum(ch2)!=9):
            return False
    return True

if s() == True:
    print("YES")
else:
    print("NO")
