# Kent Denver Code-a-thon Django Starter Code

## Introduction

This repository is designed to act as a springboard for your first significant web application. [Django](https://www.djangoproject.com/) acts as a full-stack, interacting with (and creating) a database for you, rendering and serving webpages, and handling user interaction.

Throughout this simple example you will find comments in the code. In python comments look like this:
```python
# This is a comment, it will tell you about the line below it.
# Here we give the variable x the value 5
x = 5
```
You should be able to use the comments to help you understand what the code is doing, then you should change it, break it, fix it, make it better.

## Getting Started

#### Getting pip

Unfortunately, this repository is not the only thing you need to get started. In order to install Django and any other programs you might need we are going to use **pip**. You will need to install pip by downloading this file: [get-pip.py](https://bootstrap.pypa.io/get-pip.py). Please right click that link and say "Save Link As..." Put it in your **downloads folder**.

You will then run that file by using Terminal (OSX) or Command Prompt (Windows). To launch these programs do the following:
 - **On Windows**: Hit the windows key and type "Command Prompt"
 - **On OSX**: Use spotlight (the magnifying glass) to find "Terminal"

Then run these commands:

**OSX**
```
cd Downloads
sudo -H python get-pip.py
```
On OSX, you will need to type your computer password at the prompt (no characters will show, but it is working).

**Windows**
```
cd Downloads
python get-pip.py
```


This means that you can now use the command `pip`, hurrah!

#### Getting a copy of this project

You are now ready to grab your very own copy of this project. If you know how to use git, feel free to clone this repo. If that last sentence didn't make any sense, don't worry. You can just download the .zip of this entire project from that big green button in the upper right like this:

![zip download](https://github.com/MrClement/KDS-Code2016-DjangoStarter/raw/master/resources/clone.png "How to download a zip archive")

If you downloaded the zip file, unzip it and move it out of your downloads folder. You will be working from that folder for the rest of this project, so keep it accessible.

#### Installing requirements

You now need to install the requirements for this project. It is simple now that you have `pip`. In terminal (or command prompt) run the command:

**OSX**
```
sudo -H pip install django
```

**Windows**
```
pip install django
```

You should be able to verify that that command worked by running:
```
python -m django --version
```

This command asks your computer what version of Django it has installed, it should tell you something like `1.10.2`.

## Start Using Django

#### A quick overview

You should now have a folder somewhere on your computer called **KDS-Code2016-DjangoStarter**. Inside it there are the following files and folders (this is not a complete list):

```
├── README.md
├── resources
│   └── clone.png
└── server
    ├── db.sqlite3
    ├── firstapp <-- This is the important folder
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── admin.py
    │   ├── admin.pyc
    │   ├── apps.py
    │   ├── apps.pyc
    │   ├── migrations
    │   ├── models.py
    │   ├── models.pyc
    │   ├── static
    │   │   └── firstapp
    │   │       ├── script.js
    │   │       └── style.css
    │   ├── templates
    │   │   └── firstapp
    │   │       ├── base.html
    │   │       ├── detail.html
    │   │       ├── index.html
    │   │       └── new.html
    │   ├── tests.py
    │   ├── urls.py
    │   ├── urls.pyc
    │   ├── views.py
    │   └── views.pyc
    ├── manage.py
    └── server
        ├── __init__.py
        ├── __init__.pyc
        ├── settings.py
        ├── settings.pyc
        ├── urls.py
        ├── urls.pyc
        ├── wsgi.py
        └── wsgi.pyc
```

This might seem a little overwhelming, but **to start you will only need to worry about the folder firstapp**. This is because Django is designed to run multiple *apps* with the same *project*. In this example our project is called server and our app is called firstapp:

```
├── __init__.py
├── admin.py
├── apps.py
├── migrations
├── models.py <-- Database models go here
├── static <-- CSS and JS go here
│   └── firstapp
│       ├── script.js
│       └── style.css
├── templates <-- HTML templates go here
│   └── firstapp
│       ├── base.html
│       ├── detail.html
│       ├── index.html
│       └── new.html
├── tests.py
├── urls.py <-- URL routing is done here
├── views.py
```

#### The Model-View-Controller (MVC) framework

Django is built on the Model-View-Controller framework. What this means is that we specify what sort of data our server should store in the `models.py` file. We design the page that our users should see in the templates directory. We control the rendering of that view and handle user input in the 'views.py' file.

#### Running the example code

You can start the server by running the command:

```python manage.py runserver```

You can stop it by pressing **Ctrl-C**.
If you want to play around more with Django's commands feel free to ask for help with:

```python manage.py help```

##### Admin panel

Once the server is running, you can interact directly with everything in the database using the admin panel. For this demo, there is an existing admin account for you to use. The username is *admin* and the password is *DjangoAdmin*.

## Get hacking

Start changing the code. Break it, improve it, make it your own. Don't forget to ask for help if you need it or consult [Django's great documentation](https://docs.djangoproject.com/en/1.10/).

#### A few last hints:

- If you need to update or create a new model you will find the procedure laid out [here](https://docs.djangoproject.com/en/1.10/intro/tutorial02/) quite useful.
- There are fairly extensive comments in the code that describe what is happening
 - In python (files that end in .py) comments start with the `#` symbol
 - In HTML (files that end with .html) comments start with `<!--`
- If you change the models in models.py you will need to update the database schema. Django will do this for you and migrate any data as well. You just need to run the following commands:
```
python manage.py makemigrations <app name>
python manage.py sqlmigrate <app name> <migration number>
python manage.py migrate
```
