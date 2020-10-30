# import sys
# A,B = map(int,sys.stdin.readline().split())
# while(A!=0 and B!=0):
#     print(A+B)
#     A,B = map(int,sys.stdin.readline().split())
    
import sys

while(True):
    A,B = map(int,sys.stdin.readline().split())
    
    if A == 0 and B == 0 : break
    print(A+B)
    
