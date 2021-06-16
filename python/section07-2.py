class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp 
        self.color = color
    
    def show(self):
        return 'Car class "Show Method"'

class BmwCar(Car):
    """Sub class"""
    def __init__(self,car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    def show_model(self):
        return 'Your Car Name : %s' %(self.car_name)

class BenzCar(Car):
    """Sub class"""
    def __init__(self,car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name
    def show_model(self):
        return 'Your Car Name : %s' %(self.car_name)
    
    def show(self):
        print(super().show())
        return 'Car info : %s %s %s' % (self.car_name, self.type, self.color) 

model1 = BmwCar('520d','sedan','red')
print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Sub
print(model1.__dict__)

model2 = BenzCar('220d', 'suv', 'black')
print(model2.show())

model3 = BenzCar('350s','sedan','silver')
print(model3.show())

print(BmwCar.mro())

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass

print(M.mro())