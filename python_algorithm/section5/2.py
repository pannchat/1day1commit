strn = list(input())
stack=[]
cnt = 0
for i in range(len(strn)):
    
    if strn[i-1] == '(' and strn[i] == ')' and stack != []:
        stack.pop()
        cnt += len(stack) 
    elif strn[i-1] ==')' and strn[i] == ')':
        cnt += 1
        stack.pop()
    else:
        stack.append(strn[i])

print(cnt)
