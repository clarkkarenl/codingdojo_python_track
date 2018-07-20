Assignment: Dojo Ninjas
Karen Clark
2018-07-19

Create a new app called 'dojo_ninjas'. For this project, you're going to need the following tables/models. Please see the following diagram and create the necessary model:

* Dojo
** Have it include the name of the dojo and the city and state of each dojo
*** Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
*** Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
*** Have the third dojo be "CodingDojo New York" in "New York", "NY".
* Ninja
** Have it include first_name, last_name of each ninja in the dojo.
** Each dojo can have multiple ninjas and each ninja belongs to a specific dojo.

This is what you'll do:

1. Start a new app (the name of the app should be 'dojo_ninjas')
2. Create appropriate tables/models that allows you to perform tasks such as
    1. Dojo.objects.first().ninjas.all()
    2. Ninja.objects.first().dojo
3. Using Django Shell:
    1. Create 3 dojos
        >>> d1 = Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
        >>> d2 = Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
        >>> d3 = Dojo.objects.create(name="CodingDojo New York", city="New York", state="NY")
    2. Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
        >>> Dojo.objects.all()
        <QuerySet [<Dojo: CodingDojo Silicon Valley>, <Dojo: CodingDojo Seattle>, <Dojo: CodingDojo New York>]>
        >>> Dojo.objects.get(id=1).delete()
        (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
        >>> Dojo.objects.get(id=2).delete()
        (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
        >>> Dojo.objects.get(id=3).delete()
        (1, {u'dojo_ninjas.Ninja': 0, u'dojo_ninjas.Dojo': 1})
        >>> Dojo.objects.all()
        <QuerySet []>

    3. Create 3 additional dojos by using Dojo.objects.create
        >>> d1 = Dojo.objects.create(name="CodingDojo Silicon Valley", city="Mountain Vi
        ew", state="CA")
        >>> d2 = Dojo.objects.create(name="CodingDojo Seattle", city="Seattle", state="W
        A")
        >>> d3 = Dojo.objects.create(name="CodingDojo New York", city="New York", state=
        "NY")
        >>> Dojo.objects.all()
        <QuerySet [<Dojo: CodingDojo Silicon Valley>, <Dojo: CodingDojo Seattle>, <Dojo: CodingDojo New York>]>

    4. Create 3 ninjas that belong to the first dojo you created.
        >>> n1 = Ninja.objects.create(first_name="Goemon", last_name="Ishikawa", dojo=d1)
        >>> n2  = Ninja.objects.create(first_name="Hanzo", last_name="Hattori", dojo=d1)
        >>> n3 = Ninja.objects.create(first_name="Sandayu", last_name="Momochi", dojo=d1)
        >>> d1.__str__
        <bound method Dojo.__str__ of <Dojo: <built-in function id> CodingDojo Silicon Valley>>
        >>> d1.ninjas.all()
        <QuerySet [<Ninja: Hattori>, <Ninja: Ishikawa>, <Ninja: Momochi>]>

    5. Create 3 more ninjas and have them belong to the second dojo you created.
        >>> djs = Dojo.objects.all().values_list('id', flat=True)
        >>> print djs
        <QuerySet [13, 14, 15]>
        >>> d2 = Dojo.objects.get(id=14)
        >>> n4 = Ninja.objects.create(first_name="Chiyome", last_name="Mochizuki", dojo=d2)
        >>> n5 = Ninja.objects.create(first_name="Kotaro", last_name="Fuma", dojo=d2)
        >>> n6 = Ninja.objects.create(first_name="Jinichi", last_name="Kawakami", dojo=d2)
        >>> Ninja.objects.filter(dojo=d2)
        <QuerySet [<Ninja: Mochizuki>, <Ninja: Fuma>, <Ninja: Kawakami>]>

    6. Create 3 more ninjas and have them belong to the third dojo you created.
        >>> n7 = Ninja.objects.create(first_name="Nagato", last_name="Fujibayashi", dojo=d3)
        >>> n8 = Ninja.objects.create(first_name="Yasutake", last_name="Fujibayashi", dojo=d3)
        >>> n9 = Ninja.objects.create(first_name="Kido", last_name="Yazaemon", dojo=d3)
        >>> Ninja.objects.filter(dojo=d3)
        <QuerySet [<Ninja: Fujibayashi>, <Ninja: Fujibayashi>, <Ninja: Yazaemon>]>

    7. Be able to retrieve all ninjas that belong to the first Dojo
        >>> Ninja.objects.filter(dojo=d1)
        <QuerySet [<Ninja: Hattori>, <Ninja: Ishikawa>, <Ninja: Momochi>]>

    8. Be able to retrieve all ninjas that belong to the last Dojo
        >>> Ninja.objects.filter(dojo=d3)
        <QuerySet [<Ninja: Fujibayashi>, <Ninja: Fujibayashi>, <Ninja: Yazaemon>]>

4. Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.
    > python manage.py makemigrations
    You are trying to add a non-nullable field 'desc' to dojo without a default; we can't do that (the database needs something to popula
    te existing rows).
    Please select a fix:
     1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
     2) Quit, and let me add a default in models.py
    > Select an option: 1
    Please enter the default value now, as valid Python
    The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
    Type 'exit' to exit this prompt
    >>> ''
    Migrations for 'dojo_ninjas':
        apps\dojo_ninjas\migrations\0002_dojo_desc.py
            - Add field desc to dojo
    > python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, dojo_ninjas, sessions
    Running migrations:
        Applying dojo_ninjas.0002_dojo_desc... OK
    >>> Dojo.objects.get(id=14)
    <Dojo: <built-in function id> CodingDojo Seattle>
    >>> Dojo.objects.filter(id=15)
    <QuerySet [<Dojo: <built-in function id> CodingDojo New York>]>
    >>> dj.__dict__
    {'city': u'Mountain View', 'name': u'CodingDojo Silicon Valley', '_state': <django.db.models.base.ModelState object at 0x0000000004CF5940>, 'state': u'CA', 'id': 13, 'desc': u''}
    >>> n10.__dict__
    {'first_name': 'Karen', 'last_name': 'Clark', 'dojo_id': 13, '_state': <django.db.models.base.ModelState object at 0x0000000004CF56A0>, '_dojo_cache': <Dojo: <built-in function id> CodingDojo Silicon Valley>, 'id': 11}
