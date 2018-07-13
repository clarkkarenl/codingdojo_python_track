Assignment: Session Words
Karen Clark
2018-07-12

Here's an interesting assignment to help you get more familiar with session, radio buttons, and checkboxes (for the belt exam, you'll be expected to know how to use radio buttons, checkboxes, input, select, and other common elements with your form).

Requirements
1. Create a new app called 'session_words'.
2. Allow the user to add any new word to the session.  The user should be able to specify the color to display the word and whether the word should appear in bigger fonts.  The user should be able to clear the session as well.
3. Show the words stored in the session on the right.

IMPORTANT
Pay attention to where the form is submitted to.  If you're having one method in views.py handle both the template render and the form processing, you're making a common mistake made by lots of developers.  Instead, have the forms be submitted to say 'localhost/session_words/add_word' or 'localhost/session_words/clear' and where the methods that handle the two requests simply redirect back to 'localhost/session_words'.
