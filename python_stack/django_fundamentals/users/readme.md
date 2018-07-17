Assignment: Users
Karen Clark
2018-07-16

Create a new app called 'user_login'. Create a new model called 'User' that has the following fields/attributes

Please do the following

1. Create a new model called 'User' with the information above.
2. Successfully create and run the migration files
    > python manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions, user_login
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying sessions.0001_initial... OK
    Applying user_login.0001_initial... OK

3. Using the shell...
a. Know how to retrieve all users.
    >>> User.objects.all()

b. Know how to get the last user.
    >>> User.objects.last()

c. Create a few records in the users
    >>> User.objects.create(first_name="James", last_name="Jameson", email_address="j@j.com", age=21)
    <User: User object>
    >>> User.objects.create(first_name="Mary", last_name="Lamb", email_address="snow@lamb.com", age=13)
    <User: User object>
    >>> User.objects.create(first_name="Ernie", last_name="Ernieson", email_address="example@test.com", age=32)
    <User: User object>
    >>> User.objects.count()
    3

d. Know how to get the first user.
    >>> user_1 = User.objects.get(id=1)
    >>> user_1.first_name
    u'James'

e. Know how to get the users sorted by their first name (order by first_name DESC)
    >>> for u in User.objects.order_by("first_name"):
    ...     print u.first_name
    ...
    James
    Mary

f. Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
    >>> id3 = User.objects.get(id=3)
    >>> print id3.first_name
    Ernie
    >>> id3 = User.objects.get(id=3)
    >>> id3.first_name="Fred"
    >>> id3.save()
    >>>
    >>> x = User.objects.get(id=3)
    >>> x.first_name
    u'Fred'

g. Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
    >>> for u in User.objects.order_by("first_name"):
    ...     print u.first_name, u.id
    ...
    Fred 3
    James 1
    Mary 2
    Xavier 4
    >>> User.objects.get(id=4).delete()
    (1, {u'user_login.User': 1})
    >>> for u in User.objects.order_by("first_name"):
    ...     print u.first_name, u.id
    ...
    Fred 3
    James 1
    Mary 2

4. (optional) Ninja:
Find a way to validate the data coming in to the shell.  For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.
    I investigated this and discovered two possible ways:
    1. Write a custom serializer that parses the value before it's committed
    2. Use `signals` to put a `pre_save` condition on the submission of the query

    Unfortunately, I wasn't able to get this to work for our use case. I'd love to see a demo of it, so I can make use of this in the future, though!