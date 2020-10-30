import sys

n = sys.stdin.readline()
s = sys.stdin.readline()
s = s.strip()
temp = 0
for i in s:
    temp += int(i)

print(temp)
