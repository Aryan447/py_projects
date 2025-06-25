from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(ABC):
        print("Abstract Method")
        return
    
    def method2(self):
        print("Concrete Method")

class concreteClass(demo):
    def method1(self):
        super().method1()
        return


myobj = concreteClass()

myobj.method1()
myobj.method2()