n = int(input())
for i in range(n):
    s = input().lower()
    for j in s:
        if j != s[-1]:
            print("#%d NO" %(i+1))
            break
        s = s[0:-1]
    else:
        print("#%d YES" %(i+1))