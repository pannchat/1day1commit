class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title
    
    def fib(n):
        a,b = 0 , 1
        while a<n:
            print(a, end=' ')
            a,b = b, a + b
        print()
    def fib2(n):
        a,b = 0 , 1
        res = []
        while a < n:
            res.append(a)
            a,b = b, a + b
        return res