car = {
  "brand": "BMW",
  "model": "X7",
  "year": 2022
}
print(car)
print(type(car))

car["color"] = "White" # adding another attribute
print(car)

car.update({"color": "Blue"}) # updating value of color attribute
print(car)

car.pop("color") # removing color attribute using pop()
print(car)

car2 = car.copy()
print("Copied Dictionary", car2)