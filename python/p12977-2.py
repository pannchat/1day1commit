
def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def solution(nums):
    from itertools import combinations as cb
    
    answer = 0
    for i in cb(nums, 3):
        if isPrime(sum(i)):
            answer += 1
    return answer
