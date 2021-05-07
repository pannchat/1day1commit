strn = list(input())

digit = []
arr = []
res = 0
for s in strn:
    if s.isdecimal():
        digit.append(int(s))
    else:
        if s == '+' :
            n1 = digit.pop()
            n2 = digit.pop()
            digit.append(n2+n1)
        elif s== '-':

            n1 = digit.pop()
            n2 = digit.pop()
            digit.append(n2-n1)

        elif s== '*':
            n1 = digit.pop()
            n2 = digit.pop()
            digit.append(n2*n1)
        elif s== '/':
            n1 = digit.pop()
            n2 = digit.pop()
            digit.append(n2/n1)

print(digit[0])
