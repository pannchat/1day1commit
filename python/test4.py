# def test(n,n2):
#     print(n/n2)

# test('x',1)

def foo(s):
    del s
    try:
        s+='1'
    except UnboundLocalError:
        print('wow')
    except:
        print('owo')

foo('abc')