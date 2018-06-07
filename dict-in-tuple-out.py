# Assignment: Dictionary in, tuples out
# Karen Clark
# 2018-06-06

# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns 
# a list of tuples where the first tuple item is the key and 
# the second is the value.
# Expected output:
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), 
# ("Jay", "(777) 777-7777")]

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_in_tuple_out(d):
    print [(k, v) for k, v in d.iteritems()]

dict_in_tuple_out(my_dict)