class calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        

    def addition(self):
        print(self.a+self.b)

    def mult(self):
        print(self.a*self.b)
    
    def subract(self):
        if (self.a>self.b):
            print(self.a-self.b)
        else:
            print(self.b-self.a)

    def division(self):
        if (self.a>self.b):
            print(self.a/self.b)
        else:
            print(self.b/self.a)

num1 = calculator(10, 12)

num1.addition()
num1.mult()
num1.subract()
num1.division()

num2 = calculator(5, 10)
num2.addition()
num2.mult()
num2.subract()
num2.division()