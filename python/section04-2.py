str1 = "Hello world"
str2 = 'I love newyork'

print(len(str1) , len(str2))

escape_test = "\"Hello world\""
print(escape_test)
escape_test2 = "Tab \t Tab \t"
print(escape_test2)

raw_str = r'C:\Programs\test'
print(raw_str)
raw_str2 = r'tab \t \'tab\''
print(raw_str2)

multi = \
"""
멀티라인
테스트
여러줄로
"""
print(multi)

str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'

print(str_o1 * 10)
print(str_o2 + str_o3)
# print(str_o1 + 3) # ERROR


print(str(123))
print(str(12.34))

print(type(str(123)))
print(str(123)+'test')



b = 'betta'
c = ''
# print(a.islower())
# print(c.islower())
# print(a.endswith('a',0,12))
# print(a.capitalize())

# print(b.replace('etta', 'atman'))

# a = 'api'
# print(a)
a = 'apistogramma'
print(a[0])
# a[0] = 'A'
print(a[0:11:1])
print(a[::-1])