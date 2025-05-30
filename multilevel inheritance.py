class Animal():
    def eat(self):
        print("Eating...")
class Dog(Animal):
    def bark(self):
        print("Barking...")
class Puppy(Dog):
    def sleep(self):
        print("Sleeping...")
puppy=Puppy()
puppy.sleep()
puppy.bark()
puppy.eat()