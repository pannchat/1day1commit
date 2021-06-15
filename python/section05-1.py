a = 10
b = 0

print( a == b )
print( a != b )
print( a > b )
print( a < b ) 
print( a >= b ) 
print( a <= b )

if [] :
	print("True")
else:
	print("False")

a = 3
b = 2
c = 1 
print('and : ', a > b and b > c)
print('or : ', a > b or c > b)
print('not : ', not a > b)

print(5 + 10 > 0 and not 7 + 3 == 10)


score = 90
if score >= 90:
    print("등급 A")
elif score >= 80:
    print("등급 B")
elif score >= 70:
    print("등급 C")
else:
    print("등급 F")

age = 27
height = 175
if age >= 20:
    if height >= 170:
        print("A지망 지원가능")
    elif height >= 160:
        print("B 지망 지원 가능")
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")
    