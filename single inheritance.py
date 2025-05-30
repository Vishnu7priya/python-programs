class Vehicle:
    def start(self):
        print("vehicle has started.")
class Car(Vehicle):
    def drive(self):
        print("car is driving.")
car=Car()
car.start()
car.drive()

