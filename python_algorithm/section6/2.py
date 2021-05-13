
def DFS(x):
    # 전위순회
    if x > 7:
        return
    else:
        
        DFS((x * 2))
        print(x)
        DFS((x*2)+1)

    
if __name__ == "__main__":
    DFS(1)