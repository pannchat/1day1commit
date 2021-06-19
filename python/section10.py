# print('test) 
# # SyntaxError: EOL while scanning string literal

# if True
#     pass
# # SyntaxError: invalid syntax

# # NameError : 참조변수 없음

# a = 10 
# print(c)
# # NameError: name 'c' is not defined

# #ZeroDivisionError : 0으로 나누기 에러

# print(10/0)
# #ZeroDivisionError: division by zero
# # IndexError : index 범위 오버
# li = [1,2,3]
# print(li[3])

# # IndexError: list index out of range

# # KeyError : 없는 key를 조회했을 때 발생함.

# dic = {'name':'kim', 'age':33, 'city':'seoul'}
# print(dic['hobby'])
# #KeyError: 'hobby'
# # 이는 get메서드를 사용해서 방지할 수 있다.

# # AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# import time
# print(time.time()) # 불러온 모듈에 대해 있는 속성은 사용이 가능하지만
# print(time.test()) # 이와같이 없는 attribute는 AttributeError 를 발생시킨다.

# ValueError : 참조값이 없을 때 발생
# x = [1,5,9]
# x.remove(10)
# x.index(10)
# ValueError: list.remove(x): x not in list
# 리스트에 포함되어있지 않은 요소를 제거하려고 할때나 접근하려고 할 때 발생함

# FileNotFoundError :
# f = open('test.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# 주로 외부 파일을 처리할 때 발생하는 에러로 없는 파일을 처리하려고 할 때 발생한다.

# TypeError
# x = [1,2]
# y = (1,2)
# z = 'test'

# print(x+y)
# print(y+z)
# # TypeError: can only concatenate list (not "tuple") to list
# # 튜플과 리스트는 결합이 안되고 문자열과 리스트, 문자열과 튜플도 결합할 수 없다. 형변환을 통해 처리가 가능하다.

# EAFP(It's Easier to Ask Forgiveness than Permission) 허락보다 용서구하는것이 쉽다
# 라는 코딩스타일로 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩을한뒤 런타임 에러발생시 예외 처리 코딩을 권장하는 방식이다.
# EAFP는 python에서 표준이다.




# name = ['kim','park','lee']

# try:
#     z = 'choi'
#     x = name.index(z)
#     print('{} Found it!'.format(z,x+1))
# except:
#     print(' Not found it! ')
# else:
#     print("ok")
# finally:
#     print('finally')

# name = ['kim','park','lee']

# try:
#     z = 'choi'
#     x = name.index(z)
#     print('{} Found it!'.format(z,x+1))
# except ValueError as v:
#     print(v)
# except IndexError:
#     print('index Error')
# except Exception:
#     print('Error')
# else:
#     print("ok")
# finally:
#     print('finally')

try:
    a = 'kim'
    if a == 'park':
        print('허가')
    else:
        raise ValueError
except ValueError:
    print('문제발생')
except Exception as f:
    print(f)
else:
    print('ok')