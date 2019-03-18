from django.shortcuts import render
from django.http import HttpResponse

from loginapp.forms import Insuranceform

# Create your views here.

def login(request):
    form = Insuranceform()

    if request.method == "POST" :
        form = Insuranceform(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return login_second(request) #changing Password
        else:
            print("ERROR FORM")

    return render(request, 'loginapp/login_page.html',{'form' :form})


def login_second(request):
    return HttpResponse("<h1> Coming soon </h1>")
