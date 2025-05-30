class Engine:
    def engine_type(self):
        print("This vehicle has a diesel engine.")
class Wheels:
    def number_of_wheels(self):
        print("This vehicle has four wheels.")
class Truck(Engine,Wheels):
    pass
truck=Truck()
truck.engine_type()
truck.number_of_wheels()