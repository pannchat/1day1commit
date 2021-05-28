def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += arr[L]
            DFS(L+1)
            money[i] -= arr[L]
if __name__ == "__main__":
    n = int(input())
    arr = []
    money = [0] * 3
    res = 2147483648
    for _ in range(n):
        arr.append(int(input()))
    DFS(0)
    print(res)