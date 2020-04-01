from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def startPage(response):
    return render(response, "startup.html", {})


@login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html', {})

