# import copy
# a1 = ('a','b',['c','d'])
# a2 = {3:[1,5], 5:[10,20]}
# a3 = []
# a4 = (((((1),),),),)

## b1 = copy.copy(a1)
# b1_1 = copy.deepcopy(a1)

## b2 = copy.copy(a2)
## b2_1 = copy.deepcopy(a2)

# b3 = copy.copy(a3)
# b3_1 = copy.deepcopy(a3)

# b4 = copy.copy(a4)
# b4_1 = copy.deepcopy(a4)

# print(id(b4), id(b4_1))


# def prob8(x,y):
# cnt = 0
# for i in x:
#     if i in y:
#         cnt+=1
# return cnt


# y = [1,5,3,2]
# x = [2,7,8,9,1,3,10,14]
# print(prob8(x,y))

# def prob9(x):
# for idx in range(1,len(x)):
#     v = x[idx]
#     i = idx
#     while i>0 and x[i-1] > v:
#         x[i] = x[i-1]
#         i -= 1
#     x[i]= v


# x = [4,23,7,52,31,2,3,6]
# print(prob9(x))
# print(x)

# def prob10(x,y):
#     print(x,y)
#     if x == y :
#         return True
#     elif x > y :

#         return(prob10(x,pow(y,)))
        
#     elif y > x:
#         return False

# print(prob10(100,10))
# def prob10(x, y):
#     if x == y:
#         print(True)
#         return
#     else:
#         y = y ** 2
#         if x < y:
#             print(False)
#             return
#         prob10(x, y)

prob10(8,2)