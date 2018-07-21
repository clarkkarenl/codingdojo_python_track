Assignment: Books and Authors
Karen Clark
2018-07-21

Create a new app called 'book_authors' in the same project where you did the previous assignment: Dojo Ninjas.  You'll use this assignment as well as the previous assignment to learn about Ajax.

Please do the following
1. Create a new model called 'Book' with the information above.
2. Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the following:
    1. Book.objects.first().authors
    2. Author.objects.first().books
3. Successfully create and run the migration files
    > python manage.py makemigrations
        Migrations for 'books_authors':
            apps\books_authors\migrations\0001_initial.py
                - Create model Author
                - Create model Book
                - Add field books to author
    (djangoEnv)
    > python manage.py migrate
        Operations to perform:
            Apply all migrations: admin, auth, books_authors, contenttypes, dojo_ninjas, sessions
        Running migrations:
            Applying books_authors.0001_initial... OK

4. Using the shell...
    1. Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
        >>> b1 = Book.objects.create(name="C Sharp", desc='')
        >>> b2 = Book.objects.create(name="Java", desc='')
        >>> b3 = Book.objects.create(name="Python", desc='')
        >>> b4 = Book.objects.create(name="PHP", desc='')
        >>> b5 = Book.objects.create(name="Ruby", desc='')
        >>> Book.objects.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: PHP>, <Book: Ruby>]>

    2. Create 5 different authors: Mike, Speros, John, Jadee, Jay
        >>> a1 = Author.objects.create(first_name="Mike", last_name="Mike", email="m@m.com")
        >>> a2 = Author.objects.create(first_name="Speros", last_name="Speros", email="s@s.com")
        >>> a3 = Author.objects.create(first_name="John", last_name="John", email="jo@jo.com")
        >>> a4 = Author.objects.create(first_name="Jadee", last_name="Jadee", email="ja@ja.com")
        >>> a5 = Author.objects.create(first_name="Jay", last_name="Jay", email="jay@jay.com")
        >>> Author.objects.all()
        <QuerySet [<Author: Mike>, <Author: Speros>, <Author: John>, <Author: Jadee>, <Author: Jay>]>

5. Add a new field in the authors table called 'notes'.  Make this a TextField. Successfully create and run the migration files.
    > python manage.py makemigrations
        You are trying to add a non-nullable field 'desc' to author without a default; we can't do that (the database needs something to populate existing rows).
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        2) Quit, and let me add a default in models.py
        Select an option: 1
        Please enter the default value now, as valid Python
        The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
        Type 'exit' to exit this prompt
        >>> ''
        Migrations for 'books_authors':
            apps\books_authors\migrations\0002_author_desc.py
                - Add field desc to author
    > python manage.py migrate
        Operations to perform:
            Apply all migrations: admin, auth, books_authors, contenttypes, dojo_ninjas, sessions
            Running migrations:
                Applying books_authors.0002_author_desc... OK

6. Using the shell...
    1. Change the name of the 5th book to C#
        >>> b5 = Book.objects.get(id=5)
        >>> b5.name
        'Ruby'
        >>> b5.name="C#"
        >>> b5.save()
        >>> b5.name
        'C#'

    2. Change the first_name of the 5th author to Ketul
        >>> a5 = Author.objects.get(id=5)
        >>> a5.first_name="Ketul"
        >>> a5.save()
        >>> a5.first_name
        'Ketul'

    3. Assign the first author to the first 2 books
        >>> a1 = Author.objects.get(id=1)
        >>> b1 = Book.objects.get(id=1)
        >>> b2 = Book.objects.get(id=2)
        >>> a1, b1, b2
        (<Author: Mike>, <Book: C Sharp>, <Book: Java>)
        >>> b1.author_set.all()
        <QuerySet []>
        >>> b2.author_set.all()
        <QuerySet []>
        >>> a1.books.add(b1)
        >>> b1.author_set.all()
        <QuerySet [<Author: Mike>]>
        >>> a1.books.add(b2)
        >>> b2.author_set.all()
        <QuerySet [<Author: Mike>]>
        >>> a1.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>]>

    4. Assign the second author to the first 3 books
        >>> a2 = Author.objects.get(id=2)
        >>> b3 = Book.objects.get(id=3)
        >>> a2.books.add(b1, b2, b3)
        >>> a2.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>]>

    5. Assign the third author to the first 4 books
        >>> b4 = Book.objects.get(id=4)
        >>> a3 = Author.objects.get(id=3)
        >>> a3.books.add(b1, b2, b3, b4)
        >>> a3.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: PHP>]>

    6. Assign the fourth author to the first 5 books (or in other words, all the books)
        >>> b5 = Book.objects.get(id=5)
        >>> a4 = Author.objects.get(id=4)
        >>> a4.books.add(b1, b2, b3, b4, b5)
        >>> a4.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: PHP>, <Book: C#>]>

    7. For the 3rd book, retrieve all the authors
        >>> b3.author_set.all()
        <QuerySet [<Author: Speros>, <Author: John>, <Author: Jadee>]>

    8. For the 3rd book, remove the first author
        >>> b3.author_set.first()
        <Author: Speros>
        >>> a2.books.remove(b3)
        >>> a2.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>]>
        >>> b3.author_set.all()
        <QuerySet [<Author: John>, <Author: Jadee>]>

    9. For the 2nd book, add the 5th author as one of the authors
        >>> a5.books.add(b2)
        >>> b2.author_set.all()
        <QuerySet [<Author: Mike>, <Author: John>, <Author: Jadee>, <Author: Jay>]>

    10. Find all the books that the 3rd author is part of
        >>> Book.objects.filter(author=3)
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: PHP>]>
        >>> a3.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>, <Book: Python>, <Book: PHP>]>

    11. Find all the books that the 2nd author is part of
        >>> a2.books.all()
        <QuerySet [<Book: C Sharp>, <Book: Java>]>