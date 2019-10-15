import os

class Car:
    def __init__(self, car_data):
        self.color = car_data[0]["color"]
        self.brand = car_data[0]["brand"]
        self.speedlimit = car_data[0]["speedlimit"]
        self.speed = 0
        self.fuellimit = car_data[0]["fuellimit"]
        self.fuel = 10
    
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




class Owner(Car) :
    def __init__(self,name,address, car_data):
        super().__init__(car_data)
        self.name = name
        self.address = address

    def ownerView(self):
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
                print(owner1.information())
                print("Now the car has "+ str(owner1.fuel) + "L of fuel")
            elif choice == 2:
                os.system("cls")
                print(owner1.startUp())
                print("Now the car has "+ str(owner1.fuel) + "L of fuel")
            elif choice == 3:
                os.system("cls")
                print(owner1.speedUp())
                print("Now the car has "+ str(owner1.fuel) + "L of fuel")
            elif choice == 4:
                os.system("cls")
                print(owner1.speedDown())
                print("Now the car has "+ str(owner1.fuel) + "L of fuel")
            elif choice == 5:
                os.system("cls")
                owner1.fuelUp()
                print("Now the car has "+ str(owner1.fuel) + "L of fuel")
            elif choice == 0:
                os.system("cls")
                print(owner1.stop())
                break
            else:
                break
                

car_data = [
    {"owner_id":"1", "owner_name":"Taka", "brand":"ferrari", "color":"red", "speedlimit":130, "fuellimit":30},
    {"owner_id":"1", "owner_name":"Taka", "brand":"ferrari", "color":"red", "speedlimit":130, "fuellimit":30},
    {"owner_id":"1", "owner_name":"Taka", "brand":"ferrari", "color":"red", "speedlimit":130, "fuellimit":30},
    {"owner_id":"1", "owner_name":"Taka", "brand":"ferrari", "color":"red", "speedlimit":130, "fuellimit":30}
]

owner1 = Owner("Taka", "Cebu", car_data)

#owner1.ownerView()

# print(len(car_data))

# print(dir(owner1))

owner1.ownerView()