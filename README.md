Read me:
# SR-Novel-Website
1. Overview 

1.1 Member:    Shipeng Yu, Ruifeng Zhang

1.2 Goal:     Practicing Python, Django, bootstrap and other HTML, CSS design.

1.3 Website purpose:    	A website that allows people share books by uploading chapters of books, and other people can read each chapter of books, instead open a PDF with full book content. 
(Of course , in real life, we can not do this, this is just for practice purpose.)
Due to technique issues, We can not automatically convert a PDF file with chapters of book to  HTML formatting files, therefore, user have to manually upload those chapters. We can do it by develop some applications, but the goal is practicing web development.


1.4 Website Design:	This website build mainly based on Django,bootstrap. The project is not super focus on Front-end part, all the front-end part are based on free templates from online or bootstrap Component related, Details will explained on UI Design part.


2. Project Run requirement

2.1 The latest version of Python3 is prefered

2.2 The latest version of Django is prefered.

2.3 Django Crispy Forms and Pillow are required

3. Project Set up steps, assume your Python and Django are installed

3.1 workon my_django_environment

3.2 Pip install Pillow(first time)

3.3 Pip install django-crispy-forms(first time)

3.4 Py manage.py runserver( in the directory that has manage.py file)

3.5 Enter 127.0.0.1:8000 on browser.


4. Website Features

4.1 User

4.1.1 Sign up

4.1.2 Login in

4.1.3 Forget password/Change password by Email

4.1.4 Create Book/Chapters

4.1.5 Delete Chapters (author required)

4.1.6 Edit Book information/Chapter information(author required)

4.1.7 Add Favorite for book, which is book like number add 1, one of evaluation for ranking.

4.1.8 Add marker for chapters, which allows user mark this chapter and add the link to profile page.

4.1.9 Own Profile Page

4.1.9.1 Username

4.1.9.2 Email address

4.1.9.3 Profile image

4.1.9.4 About me

4.1.9.5 Favorite books including book link

4.1.9.6 Marked Chapters including chapter link

4.1.9.7 Number of Created book


4.2Book

4.2.1Book Chapters/content

4.2.2Book Detail

4.2.2.1Title

4.2.2.2Author

4.2.2.3Genre

4.2.2.4Like Number

4.2.2.5ISBN

4.2.2.6Word Count

4.2.2.7Chapter Count

4.2.2.8Date upload

4.2.2.9Summary




![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/index.png?raw=true)
