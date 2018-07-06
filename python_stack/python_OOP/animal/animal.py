# Assignment: Animal
# Karen Clark
# 2018-07-05

# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.
# Objective
# The objective of this assignment is to help you understand inheritance.
# Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. 
# Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call.
# As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.
# Animal Class
# Attributes:
# * name
# * health
# Methods:
# * walk: decreases health by one
# * run: health decreases by five
# * display health: print to the terminal the animal's health.

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.name, "health is", self.health
        return self

# Dog Class
# * inherits everything from Animal
# Attributes:
# * default health of 150
# Methods:
# * pet: increases health by 5
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.name = name
        self.health = 150

    def pet(self):
        self.health += 5
        return self

# Dragon Class
# * inherits everything from Animal
# Attributes:
# * default health of 170
# Methods:
# * fly: decreases health by 10
# * display health: prints health by calling the parent method and prints "I am a Dragon"
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.name = name
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        Animal.display_health(self) 
        print " I am a Dragon"
        return self

# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
animal1 = Animal("cat", 100)
animal1.walk().walk().walk().run().run().display_health()

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
animal2 = Dog("dog", 100)
animal2.walk().walk().walk().run().run().pet().display_health()

animal3 = Dragon("dragon", 50)
# animal3.run().pet().display_health()
animal3.run().fly().display_health()
# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
animal4 = Animal("cat", 100)
# animal4.walk().run().pet().display_health()
# animal4.walk().run().fly().display_health()
animal4.walk().walk().walk().run().run().display_health()