class AIML():
    def __init__(self):
        self.name = input("Enter student's name: ")
        self.roll = input("Enter student's roll number: ")

class dld_marks(AIML):
    def __init__(self):
        super().__init__()
        
        print("In child class")

    def marks(self):
        mid = int(input("Enter mid sem marks: "))
        prof = int(input("Enter proficiency marks: "))
        end = int(input("Enter end sem marks: "))
        result = mid+prof+end
        print()
        print("Student Details: ", self.name, self.roll)
        print("Marks: ", mid, prof, end)
        print("Total: ", result)

        if (result>=33):
            print("Student is Pass")

        else:
            print("Student is Fail")

obj1 = dld_marks()
obj1.marks()