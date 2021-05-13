import sys
def print_binary(n):
    if n > 0:
        remainder = n % 2 
        n = n // 2
        print_binary(n)
        print(remainder, end="")

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print_binary(n)
    

