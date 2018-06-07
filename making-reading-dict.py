# Assignment: Making and Reading from Dictionaries
# Karen Clark
# 2018-06-06 

# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language

info = {'name': 'Karen', 'age': 'NaN', 'country of birth' : 'the United States', 'favorite language' : 'Python'}

def read_dict(dict_in):
    for k, v in dict_in.iteritems():
        print "My " + str(k) + " is " + str(v)

read_dict(info)