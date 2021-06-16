def hi(name):
    print('hi,', name)

hi('jiwon')
hi('python')

def hi_return(name):
    val = 'Hi, ' + str(name)
    return val

print(hi_return('apple'))

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1,y2,y3

val1 = func_mul(100)

print(type(val1))

def args_ex(*args):
    for idx,val in enumerate(args):
        print(idx,val)

args_ex('a','b','c','d')

def kwargs_ex(**kwargs):
    for key, val in kwargs.items():
        print(key, val)
kwargs_ex(name='kim', age='21')

def function_ex(arg1, arg2, *args, **kwargs):
	print(arg1, arg2, args, kwargs)

function_ex('a','b') # a b () {}

function_ex('a','b','park','kim') # a b ('park', 'kim') {}
function_ex('a','b','park','kim',age=21, age2=31) # a b ('park', 'kim') {'age': 21, 'age2': 31}

def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in function")
    func_in_func(num + 10000)

nested_func(10000)

def func_mul3(x:int) -> tuple:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1,y2,y3

val2 = func_mul3(100)
print(val2)

def mul_10(num:int) -> int:
    return num*10
var_func = mul_10
print(type(var_func))

lambda_mul_10 = lambda num : num * 10
print(lambda_mul_10(10))

def func_final(x,y,func):
    print(x * y * func(10))
func_final(10,10,lambda_mul_10)