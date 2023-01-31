django-react-app
----------------------
django-react-app is a react application already configured to be used in a django project as a django application. 


Quick start
-----------

### Install 

```
pip install django-react-app

```



Add "django_react_app" to your INSTALLED_APPS setting like this::

```

    INSTALLED_APPS = [
        ...
        'django_react_app',
    ]

```

Include the django_react_app URLconf in your project urls.py like this:

```
path('', include('django_react_app.urls')),

```

---

# Configuration

### To have django-react-app on your root project 

You will find the django_react_app inside your <virtualenv_name>/lib/<python_ver>/site-packages/ folder move the django_react_app folder to your root project 

### Install React dependencies

Open a terminal and go to the django_react_app folder, to install react dependencies run : 

```
npm install

```
After that to run the React app you can run:

```
npm run dev

```


#### Run your django app

Start your django development server in another terminal and visit http://127.0.0.1:8000/ to view your react app application running 



