class UserInfo:
    def __init__(self,name):
        self.name = name
    def print_user(self):
        print("Name : ", self.name)

user1 = UserInfo('jiwon') 
user1.print_user()
user2 = UserInfo('sana') 
user2.print_user()

class SelfTest:
    def function1():
        print('func 1')
    def function2(self):
        print('func 2')

self_test = SelfTest()
# SelfTest.function1()
# SelfTest.function2()
# self_test.function2()

class WareHouse:
    stock_num = 0 # 클래스변수 self 가 없기 때문에 여러 인스턴스에서 공유한다.
    def __init__(self,name):
        self.name = name
        WareHouse.stock_num +=1  #클래스 변수는 self 가 없으므로 직접 접근
    def __del__(self): # 인스턴스가 종료될 때 호출되는 함수
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)
print(user1.stock_num)