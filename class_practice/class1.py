my_list = ['thing1', 100, {'my_key': 'my_val'}]
# for item in my_list:
#     if isinstance(item, str):
#         print item
#     elif isinstance(item, dict):
#         print "it's a dict"
#     else:
#         print "that's something else"
#     print "This always prints"
my_dict = {
    'some_key' : 'some_val',
    'other_key' : my_list
}

my_tuple = ('thing1', 100, ['thing in list', 'other thing in list'])
# my_tuple[0] = 'changed'
my_tuple = 'hello'
# print my_tuple

users = [
    {
        'name' : 'Wes',
        'height' : "5\'1\""
    },
        {
        'name' : 'Todd',
        'height' : "5\'11\""
    },
        {
        'name' : 'Mark',
        'height' : "6\'1\""
    },
        {
        'name' : 'Mary',
        'height' : "5\'4\""
    }
]

# print range(0, len(users), 1)
# for i in range(len(users)):
#     print users[i]
# for user in users:
#     print user
# tuple_to_unpack = ('foo', 'bar')
# str1, str2 = tuple_to_unpack
# print str1, str2
# for user in users:
#     for key, value in user.iteritems():
#         print key, value
# for user in users:
#     for key in user.iterkeys():
#         print key

# print type(tuple_to_unpack)
# print type(str1)
# print str1, str2

my_int= 10
my_float = 10.25
my_sum = my_int + my_float


# print "Isinstance float: "
# print isinstance(my_sum, float)
# print "Type: "
# print type(my_sum)
# print "Isinstance object: "
# print isinstance(my_sum, object)

def my_func(arg1, arg2='world'):
    return str(arg1) + str(arg2)

print my_func(my_int)
print my_func(my_int, my_float)

print "This is not a love song"
print "Not a love song"

def my_doop(arg1)