from django.urls import path
from .views import indexView 


# add your react routes paths here
REACT_ROUTES = [
    'home', #like this
]

urlpatterns = [
    path('', indexView,name="index"), 
]

for route in REACT_ROUTES:
    urlpatterns += [
        path(f"{route}", indexView, name="index")
    ]