# parent class
class Animal:
    alive = True
    def eat(self):
        print("This Animal eats")

    def sleep(self):
        print("This Animal sleeps")
# Child classes
class Dog(Animal):
    def bark(self):
        print("This Dog barks")
class Cat(Animal):
    def run(self):
        print("This Cat runs")
class Bird(Animal):
    def fly(self):
        print("This Bird flies")
class Lion(Animal):
    def roar(self):
        print("This Lion roars")
# Objects
dog=Dog()
cat=Cat()
bird=Bird()
lion = Lion()

print(dog.alive)
cat.eat()
bird.sleep()
print(lion.alive)

dog.bark()
cat.run()
bird.fly()
lion.roar()