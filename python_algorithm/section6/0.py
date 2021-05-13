import sys
def DFS(x):
    if x > 0:
        # print(x)
        DFS(x-1)
        print(x)

if __name__ == "__main__":
    x = int(input())
    DFS(x)