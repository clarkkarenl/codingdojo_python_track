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
4. Using the shell...
    1. Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
    2. Create 5 different authors: Mike, Speros, John, Jadee, Jay
5. Add a new field in the authors table called 'notes'.  Make this a TextField. Successfully create and run the migration files.
6. Using the shell...
    1. Change the name of the 5th book to C#
    2. Change the first_name of the 5th author to Ketul
    3. Assign the first author to the first 2 books
    4. Assign the second author to the first 3 books
    5. Assign the third author to the first 4 books
    6. Assign the fourth author to the first 5 books (or in other words, all the books)
    7. For the 3rd book, retrieve all the authors
    8. For the 3rd book, remove the first author
    9. For the 2nd book, add the 5th author as one of the authors
    10. Find all the books that the 3rd author is part of
    11. Find all the books that the 2nd author is part of