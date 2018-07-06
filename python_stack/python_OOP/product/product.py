# Assignment: Product
# Karen Clark
# 2018-07-05

# The owner of a store wants a program to track products. Create a product class to fill the following requirements.
# Product Class:
# Attributes:
# * Price
# * Item Name
# * Weight
# * Brand
# * Status: default "for sale"
# Methods:
# * Sell: changes status to "sold"
# * Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# * Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
# * Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        self.tax += 1
        self.price = self.tax * self.price
        return self

    def return_product(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason == "in box":
            self.status = "for sale"
        elif self.reason == "open box":
            self.status = "used"
            self.price = self.price * .8
        else:
            print "Please enter a valid reason from: defective, in box, open box, used"
        return self

    def display_info(self):
        print "+" * 25
        print "Price: $%.2f" % self.price
        print "Name:", self.name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

product1 = Product(50, "Doll", "3lb", "Mattel")
product1.display_info()
product1.return_product("open box").display_info() 
product1.add_tax(.15).sell().display_info()
