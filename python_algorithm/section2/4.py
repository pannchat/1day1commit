n = int(input())
score = list(map(int,input().split()))
ave = round_half_up(sum(score)/n)
min = 1000000
for idx, x in enumerate(score):
    tmp = abs(x-ave)
    if tmp < min :
        min = tmp
        s = x
        res=idx+1
    elif tmp == min:
        if x > s:
            s = x
            res = idx+1
print(ave,res)