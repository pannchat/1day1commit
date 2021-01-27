import sys

while(True):
    try:
        A,B = map(int,sys.stdin.readline().split())
        print(A+B)
    except ValueError:
        break

# import sys
# for line in sys.stdin:
#     A,B = map(int,line.split())
#     print(A+B)