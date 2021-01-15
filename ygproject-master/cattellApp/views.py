from django.shortcuts import render

def home(request):
    template_name = "cattellApp/home.html"
    return render(request, template_name)


