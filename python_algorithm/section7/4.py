def DFS(L, sum):
    global cnt
    if L == k:
        if sum == t:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum + (cv[L]*i))

if __name__ == "__main__" :
    t = int(input())
    k = int(input())
    cv = []
    cn = []
    for _ in range(k):
        a,b = map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0,0)
    print(cnt)