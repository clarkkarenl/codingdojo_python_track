# Assignment: Foo and Bar (optional)
# Karen Clark
# 2018-06-04

# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect 
# squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is
#  prime or a perfect square. If it is a prime number, print "Foo". If it is 
# a perfect square, print "Bar". If it is neither, print "FooBar". Do not use 
# the python math library for this exercise. For example, if the number you 
# are evaluating is 25, you will have to figure out if it is a perfect 
# square. It is, so print "Bar".
def foo_and_bar():

    def is_prime(n):
        count = 0
        for i in range(2, n):
            if n % i == 0:
                count += 1

        if count > 0:   
            return False
        else:
            return True

    def integer_sqrt(n):
        # Calculation uses Babylonian Method to test for perfect square
        # Adapted from a blog post about Babylonian Method from: http://www.koderdojo.com/blog/python-program-square-roots-babylonian-method
        # The calling function is pre-populated with non-negative values between 100 and 99999, so no need to test 
        guess = 5
        epsilon = 0.001

        while True:
            difference = guess**2 - n
            if abs(difference) <= epsilon:
                break
            guess = (guess + n / guess) / 2.0

        return round(guess,4)

    # Print the appropriate messages based on result
    for i in range(100,100000):
        if is_prime(i):
            print "Foo"
        elif (i / integer_sqrt(i)) == integer_sqrt(i):
            print "Bar"
        else:
            print "FooBar"