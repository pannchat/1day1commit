t = int(input())
for i in range(t):
    n,s,e,k = list(map(int,input().split()))
    n_list = list(map(int,input().split()))
    n_list = n_list[s-1:e]
    n_list.sort()
    print("#%d %d" %(i+1,n_list[k-1]))
