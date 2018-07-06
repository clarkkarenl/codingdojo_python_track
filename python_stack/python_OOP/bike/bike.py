# Assignment: Bike
# Karen Clark
# 2018-07-05
 
# Create a new class called Bike with the following properties/attributes:
# price
# max_speed
# miles
# Create 3 instances of the Bike class.
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
# Add the following functions to this class:
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# What would you do to prevent the instance from having negative miles?
# Which methods can return self in order to allow chaining methods?

class Bike(object):
    def __init__(self, name, price, max_speed):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print self.name, "info: price = ", self.price, ", max_speed = ", self.max_speed, ", miles = ", self.miles
        return self

    def ride(self):
        self.miles += 10
        print "Riding"
        return self    

    def reverse(self):
        if self.miles > 5:
            self.miles -= 5
            print "Reversing"
        else:
            print "Cannot go lower than", self.miles, "miles"
        return self

# Have the first instance ride three times, reverse once and have it displayInfo(). 
bike1 = Bike("bike1", 200, "25mph")
bike1.ride().ride().ride().reverse().displayinfo()

# Have the second instance ride twice, reverse twice and have it displayInfo(). 
bike2 = Bike("bike2", 450, "38mph")
bike2.ride().ride().reverse().reverse().displayinfo()

# Have the third instance reverse three times and displayInfo().
bike3 = Bike("bike3", 150, "20mph")
bike3.reverse().reverse().reverse().displayinfo()
