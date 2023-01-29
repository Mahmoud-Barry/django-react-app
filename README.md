=====
Django React App
=====

a react application already configured to be used in a django project as a django application.

<!-- Detailed documentation is in the "docs" directory. -->

Quick start
-----------

1. Add "django_react_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_react_app',
    ]

2. Include the django_react_app URLconf in your project urls.py like this::

    path('', include('django_react_app.urls')),

3. Move to the django_react_app directory and run ``npm install``  to install dependences.

4. And Run ``npm run dev``  to run the react app .

4. Start your django development server in another terminal and visit http://127.0.0.1:8000/
   to view your react app application running 
