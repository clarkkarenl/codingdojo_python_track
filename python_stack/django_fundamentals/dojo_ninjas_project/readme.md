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
    2. Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())
    3. Create 3 additional dojos by using Dojo.objects.create
    4. Create 3 ninjas that belong to the first dojo you created.
    5. Create 3 more ninjas and have them belong to the second dojo you created.
    6. Create 3 more ninjas and have them belong to the third dojo you created.
    7. Be able to retrieve all ninjas that belong to the first Dojo
    8. Be able to retrieve all ninjas that belong to the last Dojo
4. Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.