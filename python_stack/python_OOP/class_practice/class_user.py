class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name + " is logged in"
        return self

new_user = User("Anna", "anna@anna.com")
print new_user.email

user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email

# instantiate class User
# class User(object):
#     # this method to run every time a new object is instantiated
#     def __init__(self, name, email):
# 	# instance attributes 
#         self.name = name
#         self.email = email
#         self.logged = True
#     # login method changes the logged status for a single instance (the instance calling the method)
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     # logout method changes the logged status for a single instance (the instance calling the method)
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     # print name and email of the calling instance
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self