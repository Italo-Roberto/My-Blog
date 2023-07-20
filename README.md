<h1>Personal Blog</h1>
<img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" width="580px" height="275px" alt="Django Logo">

<p>This project intention is teach how to build a personal blog with python/ django</p>

<h3>Technologies used:</h3>
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Mysql</li>
    <li>Jquery</li>
</ul>

<p>
    This project to serve for anyone blog project with django. This project uses Django's standard authentication method to create and validate users, store images and relational databases. (MySql). It's used in this project other technnologies from build frontend, like bootstrap, javascript and jquery.
</p>

<h2>Installation instructions</h2>

<p>
    <strong>Requirements:</strong>
    <br>
    <ul>
        <li>Python 3.10.2 (or upper)</li>
        <li>Virtualenv 20.14.0 (or upper)</li>
        <li>Pip 21.2.4 (or upper)</li>
        <li>Mysql Community Server or Workbench 8.0 (or upper)</li>
    </ul>
</p>

  <strong>Installation</strong>
  
  Clone this repository for your machine:      
`git clone https://github.com/Italo-Roberto/novo_blog.git`
  
  After clone this repository, enter in this paste called <strong>myblog</strong> and create a Virtualenv: <br>
 `cd novo_blog/`
 `virtualenv nome_veenv`

  It's necessary active veenv after your creation: <br>
  Linux, MacOS: `source nome_veenv/bin/activate` <br>
  Windows: `nome_veenv/Scripts/Activate`
  
  Now, will be installing all necessary packges for our project through this file: requirements.txt (incluindo o Django) <br>
  `pip install -r requirements.txt`

  After installation and setup Mysql Community Server, create a user to access database: <br>
  `CREATE USER 'nome_usuario'@'localhost' IDENTIFIED BY 'sua_senha';`
  
  Don't forget allow access to this user: <br>
  `GRANT ALL PRIVILEGES ON * . * TO 'nome_usuario'@'localhost';`
  
  Its necessary create a databe with command bellow: <br>
  `CREATE DATABASE db_name;`
 
  For the credentials to save with security, create a file .env in root project folder, include database credentials and SECRET_KEY do Django: <br>
  `touch .env`

  Before start the project, we must to be do initial migration: <br>
  `python manage.py migrate`
 
  It's necessary create a superadmin user for manipulate database (command executed inside this folder /novo_blog): <br>
  `python manage.py createsuperuser`
 
  Start the project and create development server: <br>
  `python manage.py runserver`

<p>
    <strong>Using and CUstomization::</strong>
    <br>
    <p>
        This is a opensource porject, in the other words, you can be editind hows you like, to serve like bootstrap for anyone blog porject.
    </p>
</p>
