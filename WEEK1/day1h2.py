print("---problem 1")
print()

name = "Takahiro Hoshino"
age = 23


intro = "My name is " + name + ". I'm " + str(age) + " years old."
print(intro)
print()
print()



print("---problem2")
print()

weight = int(input("Input your weight(kg)"))
height = float(input("Input your height(m)"))

bmi = weight / height / height

print(bmi)
print()
print()


print("---problem3")
print()

students =  ["ichiro","jiro","saburo","siro","goro"]

print(students[2])
print(students[1:4])

print()
print()

print("---problem4")
print()

students_spec = {"ichiro":1.7,"jiro":1.5,"saburo":1.4,"siro":1.8,"goro":1.7}
print(students_spec["jiro"])

print()
print()

print("---problem5")
print()

students_specs = [
    {"name":"ichiro", "height":1.7, "weight":65},
    {"jiro":1.5, "height":1.6, "weight":70},
    {"saburo":1.4, "height":1.9, "weight":80}
]

print(students_specs[2])
