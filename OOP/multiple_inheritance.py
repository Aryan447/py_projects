class parent1():
    def __init__(self):
        self.a = int(input("Enter number 1 "))
        self.b = int(input("Enter number 2 "))

    def add(self):
        return self.a + self.b

class child(parent1):
    def __init__(self):
        super().__init__()
        print(super().add())
        print("In child class")


obj1 = child()