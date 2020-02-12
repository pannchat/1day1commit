# merge sort


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid] # list의 첫번째요소부터 mid번째 요소까지
    right = list[mid:] # list의 mid번째 요소부터 끝까지]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left,right):
    result=[]
    while len(left) > 0 or len(right) > 0 :
        if len(left)>0 and len(right) >0:
            if left[0] <= right[0]:
                result.append(left[0])
                left=left[1:]
            else:
                result.append(right[0])
                right=right[1:]
        elif len(left)> 0 :
            result.append(left[0])
            left=left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right=right[1:]
    return result

N = int(sys.stdin.readline())
list = []
for i in range(N):
    list.append(int(sys.stdin.readline()))

print(merge_sort(list))
