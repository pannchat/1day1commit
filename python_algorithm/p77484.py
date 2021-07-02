
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    min = list(filter(lambda x : x in win_nums, lottos))
    zero = list(filter(lambda x : x==0, lottos))
    max = min + zero
    answer = [rank[len(max)], rank[len(min)]]

    return answer
