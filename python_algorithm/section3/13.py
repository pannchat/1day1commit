arr =  [list(map(int,input().split())) for _ in range(7)]
count = 0

for i in range(7):
    for j in range(3):
        if arr[i][j] == arr[i][j+4] and arr[i][j+1] == arr[i][j+3]:
            count+=1
        if arr[j][i] == arr[j+4][i] and arr[j+1][i] == arr[j+3][i]:
                    count+=1
print(count)
