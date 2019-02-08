Read me:
# SR-Novel-Website
1.Overview 
Member:    Shipeng Yu, Ruifeng Zhang
Goal:     Practicing Python, Django, bootstrap and other HTML, CSS design.
Website purpose:    	A website that allows people share books by uploading chapters of books, and other people can read each chapter of books, instead open a PDF with full book content. 
 (Of course , in real life, we can not do this, this is just for practice purpose.)

Due to technique issues, We can not automatically convert a PDF file with chapters of book to  HTML formatting files, therefore, user have to manually upload those chapters. We can do it by develop some applications, but the goal is practicing web development.

Website Design:	This website build mainly based on Django,bootstrap. The project is not super focus on Front-end part, all the front-end part are based on free templates from online or bootstrap Component related, Details will explained on UI Design part.

2. Project Run requirement
The latest version of Python3 is prefered
The latest version of Django is prefered. 
Django Crispy Forms and Pillow are required

3. Project Set up steps, assume your Python and Django are installed
workon my_django_environment
Pip install Pillow(first time)
Pip install django-crispy-forms(first time)
Py manage.py runserver( in the directory that has manage.py file)
Enter 127.0.0.1:8000 on browser.

4. Website Features
User
Sign up
Login in
Forget password/Change password
Create Book/Chapters
Delete Chapters (author required)
Edit Book information/Chapter information(author required)
Add Favorite for book, which is book like number add 1, one of evaluation for ranking.
Add marker for chapters, which allows user mark this chapter and add the link to profile page.
Own Profile Page
Username
Email address
Profile image
About me
Favorite books including book link
Marked Chapters including chapter link
Number of Created book
Book
Book Chapters/content
Book Detail
Title
Author
Genre
Like Number
ISBN
Word Count
Chapter Count
Date upload
Summary



![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/index.png?raw=true)
