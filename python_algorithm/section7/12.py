dx = [1,0,-1,0]
dy = [0,-1,0,1]

def DFS(x,y):
    global cnt
    arr[x][y] = '0'
    cnt += 1 # 일단 1인 경우에만 호출되므로 cnt를 증가
    

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx < n and 0 <= yy < n :
            if arr[xx][yy] == '1':
                DFS(xx,yy)


if __name__ == "__main__":
    n = int(input())
    arr = [ list(input()) for _ in range(n)] # 붙어있는 숫자이므로 문자열로 입력됩니다.
    res = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1':
                cnt = 0 # cnt를 지속적으로 초기화
                DFS(i,j) #DFS를 호출하면 집을 탐색후 cnt의 값을 바꿈.
                res.append(cnt) # cnt 값을 차례로 출력하기 위해 배열을 이용한다.
                
    print(len(res))
    res.sort()
    for i in res:
        print(i)
