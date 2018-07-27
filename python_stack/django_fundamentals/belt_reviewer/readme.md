Assignment: Belt Reviewer
Karen Clark
2018-07-27

Using the below wireframe, create a Django application where logged in users can view and add book reviews. A user should also be able to delete his/her own reviews.

* Welcome - landing page
** Login (validated)
** Registration (validated)
* Books Home - Main page for books
** List of recent book reviews - last 3 are shown
*** Book title is a hyperlink to the book page
*** Reviewer name is a hyperlink to the reviewing user
** Other Books widget
*** Displays the list of books with existing reviews (each title is a hyperlink to book page)
** Add Book and Review link
*** Directs to books/add page
** Logout link
*** Log out user and return to Welcome page
* Add Book and Review - input page
** Fields to create a new book and add a review
** Link to return to home
** Link to log out
* Book Detail page
** Details of book
** Last three reviews for the book
** User can add a new review
** User can delete their own review
** Link to return to home
** Link to log out
* Users page
** Information about the user
** Count of reviews given
** Links to books & the reviews posted on them by the current user
** Link to return to home
** Link to log out
