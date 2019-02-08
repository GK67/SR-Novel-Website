# SR-Novel-Website
## 1. Overview 

### 1.1 Member:    
        Shipeng Yu, Ruifeng Zhang

### 1.2 Goal:  

Using Python, Django, bootstrap and other HTML, and CSS, to build a website that extends our knowledge of developing websites.

### 1.3 Website purpose:    	
   
As the development of SR-Novel Websit goes, we first have an idea on creating a website, that allows users to share their books by uploading each chapters of books.  After that, users can just read through each chapters of books which they like. Users can enjoy reading through our website.  However, it is not a good idea to just share book directly due to copyright of books.  As result, we decide to focus on a purpose to let users to write and share their own books on our websites. Each user can be a writer. They just write what ever they like.  If one of writer finds a book is interesting, they can just click a like.  As the process goes, our website will develop a new community of new writers for writing books.  It can also be a place to inspire writers with new idea of writing a book.


### 1.4 Website Design:	

This website build mainly based on Django,bootstrap. The project is not super focus on Front-end part, all the front-end part are based on free templates from online or bootstrap Component related, Details will explained on UI Design part.


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

4.2.1 Book Chapters/content

4.2.2 Book Detail

4.2.2.1 Title

4.2.2.2 Author

4.2.2.3 Genre

4.2.2.4 Like Number

4.2.2.5 ISBN

4.2.2.6 Word Count

4.2.2.7 Chapter Count

4.2.2.8 Date upload

4.2.2.9 Summary


5. Details and Design Of Website, like memtioned before we are not super focus on front-end

5.1 Main page

![alt text](https://github.com/GK67/SR-Novel-Website/blob/master/UI/index.png?raw=true)
