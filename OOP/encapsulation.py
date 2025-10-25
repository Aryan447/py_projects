class student():
    def __init__(self, name="Aryan", marks=90):
        self.name = name
        self.marks = marks


student1 = student()
student2 = student("Jake", 80)

print(student1.name)
print(student2.name)