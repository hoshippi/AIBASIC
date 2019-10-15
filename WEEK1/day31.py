"""
def f(x):
    y = 2**x + 3*x + 2
    return y

number = int(input("Enter a number : "))
print(f(number))


# 関数内では「return」をしておかないと、その関数以外でその受け取り値を使うことができない。
# 例えば、関数内で「print()」をしたとしても、それを関数の外で使うことはできない。

def add (x,y) :
    return x + y

num1 = int(input("Please input number 1"))
num2 = int(input("Please input number 2"))

print(add( num1, num2 ))


def subtract (x,y):
    return x-y

print(subtract(1,3))

def multiply(x,y):
    return x*y

print(multiply(4,9))

def divide(x,y) :
    return x/y


x=5

print(divide(5,5))

def change():
    global x
    x = 2

# 関数内でglobal変数を変更したい場合は、まず一度読んで、そのあと変更する


# ---activity

def sale_time (price, items):
    return price * items * 0.9

def sale_items (price, items):
    return price * items * 0.9

def sale_mix (price, items):
    return price * items * 0.9**2

time = int(input("What time is it now ? (24H) :"))
price = int(input("How much is what you're gonna buy ? :"))
items = int(input("How many items are you gonna buy ? :"))

if time >= 15 and time <= 24 :
    
    if items >= 5 :
        print( sale_mix(price, items))

    if items < 5 :
        print( sale_time(price, items))

elif items > 5 :
    print(sale_time(price, items))

elif time < 15 and time >= 0:
    print(price * items) 

else :
    print("It seems you are living in a different world")


"""
import os 

class Car:
    def __init__(self, color, brand, speedlimit, fuellimit, fuel):
        self.color = color
        self.brand = brand
        self.speedlimit = speedlimit
        self.speed = 0
        self.fuellimit = fuellimit
        self.fuel = fuel
    
    def information(self) :
        return f"color:{self.color}, brand:{self.brand}, speedlimit:{self.speedlimit} "
    
    def startUp(self):
        self.speed += 1
        return f"Car is Starting and Speed is {self.speed}"

    def speedUp(self):
        if self.speed <= self.speedlimit and self.speed > 0 and self.fuel> 0 :
            self.speed += 50
            self.fuel -= 1
            return f"Car is Speeding up and Speed is {self.speed}"
        elif self.speed > self.speedlimit :
            return "You cannot go faster than the limit"
        elif self.fuel <= 0:
            return "It seems the car is running out of gas"
        elif self.speed == 0 :
            return "You have to startup the car first"

    def speedDown(self):
        if self.speed > 10 and self.fuel > 0:
            self.speed -= 10
            self.fuel -= 1
            return f"Car is Speeding down and Speed is {self.speed}"
        elif self.speed < 10 :
            return "You shouldn't drive the car lower than the current speed"
        elif self.fuel < 0 :
            return "You don't have fuel to speed it donw"
        elif self.speed <= 0 :
            return "your cour has alredy stopped."
    
    def fuelUp(self):
        if self.fuel < self.fuellimit:
            self.fuel += 3
            return self.fuel

    def stop(self):
        self.speed = 0
        return "Now the car has stopped. Thank you for riding"


Car1 = Car("red", "Toyota", 200, 35, 5)
Car2 = Car("blue", "Ferrari", 280, 30, 15)

# メソッドとプロパティを区別するのは、末尾に引数を渡すための（）がついているのかで見分ける

print(Car1.information())
print(Car2.startUp())


while True :
    print("Welcome to My Car")
    print("[1]information")
    print("[2]startup")
    print("[3]speedup")
    print("[4]speeddown")
    print("[5]fuelup")
    print("[0]stop and exit from My Car")

    choice = int(input("Make Your Choice! :"))

    if choice == 1 :
        os.system("cls")
        print(Car1.information())
        print("Now the car has "+ str(Car1.fuel) + "L of fuel")
    elif choice == 2:
        os.system("cls")
        print(Car1.startUp())
        print("Now the car has "+ str(Car1.fuel) + "L of fuel")
    elif choice == 3:
        os.system("cls")
        print(Car1.speedUp())
        print("Now the car has "+ str(Car1.fuel) + "L of fuel")
    elif choice == 4:
        os.system("cls")
        print(Car1.speedDown())
        print("Now the car has "+ str(Car1.fuel) + "L of fuel")
    elif choice == 5:
        os.system("cls")
        Car1.fuelUp()
        print("Now the car has "+ str(Car1.fuel) + "L of fuel")
    elif choice == 0:
        os.system("cls")
        print(Car1.stop())
        break
    else:
        break
