file1 = open("./text_file.txt", "r")
print(file1.read())

file1.close()


with open("./text_file.txt", "a") as file:
    file.write(" appended_text")

with open("./text_file.txt", "r") as file:
    print(file.read())

with open("./text_file.txt", "w") as file:
    file.write("new content")

with open("./text_file.txt", "r") as file:
    print(file.read())