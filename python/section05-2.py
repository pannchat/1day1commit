
# ten = 0
# while ten != 10 :
#         print(ten)
#         ten += 1

# range(5,10) # 5 6 7 8 9

for i in range(0, 6, 2): # 0 2 4 6
    print(i)

names = ["kim", "park", "Cho", "Choi", "Yoo"]
for name in names:
    print("He is ", name)

str1 = "Hello"
for i in str1:
    print(i)

dict = {
    'name': 'kim',
    'age' : 33,
    'city': 'seoul'
}

for key in dict:
    print(key)

for key in dict.values():
    print(key)

for key in dict.keys():
    print(key)
for key,value in dict.items():
    print(key , value)

numbers = [14, 2, 64, 22, 39, 88, 37, 52, 8]
for num in numbers:
    if num == 33:
        print("found 33")
        break
else:
    print("not found 33 ....")

lt = ["1", 2, 3, True, 4.3, complex(4)]
for v in lt:
    if type(v) is float:
        continue
    print("타입 : ", type(v))