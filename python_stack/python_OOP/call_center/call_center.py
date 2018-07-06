# Assignment: Call Center
# Karen Clark
# 2018-07-05

# You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
# You will create two classes. One class should be Call, the other CallCenter.
# Call Class
# * Create your call class with an init method. Each instance of Call() should have:
# Attributes:
# * unique id
# * caller name
# * caller phone number
# * time of call
# * reason for call
# Methods:
# * display: that prints all Call attributes.

class Call(object):
    def __init__(self, uid, name, phone_number, time_of_call, reason):
        self.uid = uid
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason = reason

    def display(self):
        print "=" * 40
        print "Unique id:", self.uid
        print "Caller name:", self.name
        print "Caller phone number:", self.phone_number
        print "Time of call:", self.time_of_call
        print "Reason for call:", self.reason
        return self

# CallCenter Class
# * Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
# Attributes:
# * calls: should be a list of call objects
# * queue size: should be the length of the call list
# Methods:
# * add: adds a new call to the end of the call list
# * remove: removes the call from the beginning of the list (index 0).
# * info: prints the name and phone number for each call in the queue as well as the length of the queue.

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

# Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
    def remove_by_pn(self, pn):
        for call in self.calls:
            if call.phone_number == pn:
                self.calls.remove(call)
                self.queue_size -= 1
        return self

    def info(self):
        for call in self.calls:
            print "|", call.name, "|", call.phone_number, "|"
        print "Queue size:", self.queue_size
        return self

# Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.    
    def sort(self):
        for i in range(0, self.queue_size):
            for j in range(0, self.queue_size - i - 1):
                if self.calls[j].time_of_call > self.calls[j + 1].time_of_call:
                    self.calls[j], self.calls[j + 1] = self.calls[j + 1], self.calls[j]
        return self
  
caller1 = Call(1, "Apple Adams", "650-123-4567", "15:31:13", "computer won't start")
caller2 = Call(2, "Benji Benson", "650-333-4567", "16:11:43", "no internet")
caller3 = Call(3, "Charlie Chap", "650-333-9999", "17:23:54", "overcharged")
caller4 = Call(4, "David Duck", "415-234-7890", "10:01:15", "no internet")


cc1 = CallCenter()
cc1.add(caller3).add(caller1).add(caller4).add(caller2).info()

cc1.remove_by_pn("650-123-4567").info()

# cc1.sort()
# cc1.info()
# cc1.remove().info()

# You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
