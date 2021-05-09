important = list(input())
n = int(input())

for _ in range(n):
    obj = []
    arr = list(input())
    for i in arr:
        if any(i == j for j in important):
            if obj==[] or i not in obj:
                obj.append(i)

    if obj == important:
        print("YES")
    else:
        print("NO")
