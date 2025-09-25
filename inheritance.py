# parent class
class Animal:
    alive = True
    def eat(self):
        print("This Animal eats")

    def sleep(self):
        print("This Animal sleeps")
# Child classes
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Bird(Animal):
    pass
class Lion(Animal):
    pass
# Objects
dog=Dog()
cat=Cat()
bird=Bird()
lion = Lion()

print(dog.alive)
cat.eat()
bird.sleep()
print(lion.alive)
