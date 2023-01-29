from django.shortcuts import render

def indexView(request, *args, **kwargs):
    return render(request, "index.html") 