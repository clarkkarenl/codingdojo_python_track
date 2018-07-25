Assignment: Login and Registration
Karen Clark
2018-07-24

Rebuild the Login and Registration assignment from the flask chapter, this time using Django.

We’ve learned how to integrate models, validations, and controllers to our projects. Our next goal is to create a fully functional login and registration app! This will combine your knowledge of MVC patterns, validations, and password encryption.

Build the following:
* Show validation error messages if validations fail the following tests
** First Name - Required; No fewer than 2 characters; letters only
** Last Name - Required; No fewer than 2 characters; letters only
** Email - Required; Valid Format
** Password - Required; No fewer than 8 characters in length; matches Password Confirmation
* Bonus: Birthday Field - Before today, or go creative and do it in an age range
* Bonus: Implement Flash Messages